"""
BackfillEngine

Carrega ticks históricos do MetaTrader5 de forma eficiente
e os publica no TickBus para processamento.

Características:

• leitura em chunks grandes (100k ticks)
• proteção contra duplicação
• compatível com TickBus
• inserção em batch no SQLite
• sem barra de progresso (CLI acessível)
• baixo uso de memória
"""

import datetime
import MetaTrader5 as mt5

from mtcli.logger import setup_logger

logger = setup_logger(__name__)


class BackfillEngine:
    """
    Engine responsável pelo carregamento histórico de ticks.

    O BackfillEngine baixa ticks históricos diretamente do MT5
    utilizando janelas grandes e publica os ticks no TickBus,
    permitindo que múltiplos subscribers processem os dados.

    Tipicamente os subscribers incluem:

    - TickWriter (persistência em banco)
    - plugins de análise
    - geradores de estruturas derivadas (Renko, bars, etc)

    Fluxo arquitetural:

        MetaTrader5
            ↓
        BackfillEngine
            ↓
        TickBus
            ↓
        Subscribers
            ↓
        SQLite / Plugins
    """

    CHUNK_SIZE = 100_000

    def __init__(self, symbol, tick_bus, repository):
        """
        Parameters
        ----------
        symbol : str
            Símbolo a carregar (ex: WINJ26)

        tick_bus : TickBus
            Event bus responsável pela distribuição dos ticks.

        repository : TickRepository
            Repositório responsável pela persistência.
        """

        self.symbol = symbol
        self.tick_bus = tick_bus
        self.repository = repository

        self.last_time_msc = None

    # ---------------------------------------------------------
    # util
    # ---------------------------------------------------------

    def _get_last_stored(self):
        """
        Consulta o último tick armazenado no banco.

        Returns
        -------
        int or None
            Timestamp em milissegundos do último tick armazenado.
        """

        last = self.repository._get_last_tick_msc(self.symbol)

        if last:
            logger.info(
                "Backfill retomando do último tick armazenado: %s",
                last,
            )

        return last

    # ---------------------------------------------------------
    # main
    # ---------------------------------------------------------

    def run(self, days=5):
        """
        Executa o processo de backfill.

        Parameters
        ----------
        days : int
            Número de dias de histórico caso não exista
            histórico local no banco.

        Notes
        -----
        O processo é incremental:

        - se o banco possuir ticks, continua a partir do último
        - caso contrário inicia no passado definido por `days`
        """

        logger.info(
            "Backfill iniciado (%s) — até %s dias de histórico",
            self.symbol,
            days,
        )

        if not mt5.initialize():
            logger.error("Falha ao inicializar MetaTrader5")
            return

        mt5.symbol_select(self.symbol, True)

        now = datetime.datetime.utcnow()

        last = self._get_last_stored()

        if last:
            start = datetime.datetime.fromtimestamp(last / 1000)
            self.last_time_msc = last
        else:
            start = now - datetime.timedelta(days=days)

        total_loaded = 0

        while True:

            ticks = mt5.copy_ticks_from(
                self.symbol,
                start,
                self.CHUNK_SIZE,
                mt5.COPY_TICKS_ALL,
            )

            if ticks is None or len(ticks) == 0:
                break

            # ---------------------------------------------
            # filtro de duplicação (vetorizado numpy)
            # ---------------------------------------------

            if self.last_time_msc:

                mask = ticks["time_msc"] > self.last_time_msc
                ticks = ticks[mask]

                if len(ticks) == 0:
                    break

            # ---------------------------------------------
            # publica no event bus
            # ---------------------------------------------

            for i in range(len(ticks)):
                self.tick_bus.publish(ticks[i])

            # ---------------------------------------------
            # grava no banco
            # ---------------------------------------------

            inserted = self.repository.insert_ticks(
                self.symbol,
                ticks
            )

            total_loaded += inserted

            # último tick do chunk
            self.last_time_msc = int(ticks["time_msc"][-1])

            # próximo ponto de leitura
            start = datetime.datetime.fromtimestamp(
                self.last_time_msc / 1000
            )

            if len(ticks) < self.CHUNK_SIZE:
                break

        logger.info(
            "Backfill concluído (%s) — %s ticks inseridos",
            self.symbol,
            f"{total_loaded:,}",
        )

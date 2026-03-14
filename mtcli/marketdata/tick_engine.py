"""
TickEngine

Captura ticks continuamente do MetaTrader5
e publica no TickBus.

Fluxo:

MT5
 ↓
TickEngine
 ↓
TickBus
 ↓
Subscribers (TickWriter, plugins, etc)
"""

import time
import logging
from datetime import datetime, timedelta

import MetaTrader5 as mt5


logger = logging.getLogger(__name__)


class TickEngine:
    """
    Engine de captura contínua de ticks do MetaTrader5.
    """

    def __init__(self, symbol, tick_bus, poll_interval=0.2):
        """
        Parameters
        ----------
        symbol : str
            Símbolo a capturar.
        tick_bus : TickBus
            Event bus de ticks.
        poll_interval : float
            Intervalo entre consultas ao MT5.
        """
        self.symbol = symbol
        self.tick_bus = tick_bus
        self.poll_interval = poll_interval

        self.running = False
        self.last_time_msc = None

    # ---------------------------------------------------------
    # Sync inicial
    # ---------------------------------------------------------

    def _initial_sync(self):
        """
        Busca ticks recentes para evitar gaps na inicialização.
        """

        start = datetime.now() - timedelta(minutes=5)
        end = datetime.now()

        logger.info("TickEngine initial sync %s", self.symbol)

        ticks = mt5.copy_ticks_range(
            self.symbol,
            start,
            end,
            mt5.COPY_TICKS_ALL,
        )

        if ticks is None or len(ticks) == 0:
            logger.warning("Nenhum tick encontrado no sync inicial")
            return

        logger.info("Sync inicial carregou %s ticks", len(ticks))

        for tick in ticks:
            self.tick_bus.publish(tick)

        self.last_time_msc = ticks[-1].time_msc

    # ---------------------------------------------------------
    # Loop principal
    # ---------------------------------------------------------

    def start(self):
        """
        Inicia captura contínua de ticks.
        """

        logger.info("TickEngine start %s", self.symbol)

        self.running = True

        self._initial_sync()

        while self.running:

            if self.last_time_msc is None:
                from_time = datetime.now() - timedelta(seconds=10)
            else:
                from_time = datetime.fromtimestamp(self.last_time_msc / 1000)

            ticks = mt5.copy_ticks_from(
                self.symbol,
                from_time,
                1000,
                mt5.COPY_TICKS_ALL,
            )

            if ticks is None or len(ticks) == 0:

                logger.debug(
                    "Nenhum tick retornado para %s",
                    self.symbol,
                )

                time.sleep(self.poll_interval)
                continue

            logger.debug(
                "Recebidos %s ticks de %s",
                len(ticks),
                self.symbol,
            )

            for tick in ticks:

                if (
                    self.last_time_msc is not None
                    and tick.time_msc <= self.last_time_msc
                ):
                    continue

                self.tick_bus.publish(tick)

                self.last_time_msc = tick.time_msc

            time.sleep(self.poll_interval)

    # ---------------------------------------------------------

    def stop(self):
        """
        Solicita parada do engine.
        """

        logger.info("TickEngine stop solicitado")

        self.running = False

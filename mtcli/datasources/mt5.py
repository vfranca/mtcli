from mtcli.logger import setup_logger
from mtcli.data import mt5  # importa o módulo MT5 que você já usa hoje

log = setup_logger(__name__)


class MT5DataSource:
    """
    DataSource baseado no MetaTrader 5.

    Encapsula o acesso ao MT5 e retorna cotações
    no formato bruto esperado pelo RateDTO.
    """

    def get_rates(self, symbol: str, period: str, count: int) -> list[list]:
        """
        Obtém cotações do MT5.

        Args:
            symbol (str): Ativo (ex: WING26)
            period (str): Timeframe (ex: m1, m5, d1)
            count (int): Quantidade de barras

        Returns:
            list[list]:
                [
                    [datetime_iso, open, high, low, close, tick_volume, real_volume]
                ]
        """
        log.info(
            "MT5DataSource | symbol=%s period=%s count=%s",
            symbol, period, count
        )

        # 🔴 AQUI É O PONTO DE ADAPTAÇÃO
        # Use exatamente a função que você já tem hoje
        rates = mt5.get_rates(
            symbol=symbol,
            period=period,
            count=count,
        )

        if not rates:
            log.warning(
                "MT5DataSource | nenhuma cotação retornada | symbol=%s",
                symbol
            )

        return rates

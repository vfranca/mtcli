import MetaTrader5 as mt5
from .base import DataSourceBase
from datetime import datetime


class MT5DataSource(DataSourceBase):
    """Fonte de dados via API do MetaTrader 5."""

    def get_data(self, symbol, period):
        tf_map = {
            "M1": mt5.TIMEFRAME_M1,
            "M5": mt5.TIMEFRAME_M5,
            "M15": mt5.TIMEFRAME_M15,
            "H1": mt5.TIMEFRAME_H1,
            "D1": mt5.TIMEFRAME_D1,
        }

        if period not in tf_map:
            raise ValueError(f"Timeframe '{period}' inválido.")

        if not mt5.initialize():
            raise ConnectionError(
                f"Erro ao conectar ao MetaTrader 5: {mt5.last_error()}"
            )

        rates = mt5.copy_rates_from_pos(symbol, tf_map[period], 0, 500)
        mt5.shutdown()

        if rates is None:
            raise ValueError("Nenhum dado retornado da API MT5.")

        result = []
        for r in rates:
            result.append(
                {
                    "time": datetime.fromtimestamp(r["time"]),
                    "open": r["open"],
                    "high": r["high"],
                    "low": r["low"],
                    "close": r["close"],
                    "volume": r["tick_volume"],
                }
            )

        return result

"""Módulo fonte de dados via API do MetaTrader 5."""

import MetaTrader5 as mt5

from mtcli.logger import setup_logger
from mtcli.mt5_context import mt5_conexao

from .base import DataSourceBase

log = setup_logger()


class MT5DataSource(DataSourceBase):
    """Fonte de dados via API do MetaTrader 5."""

    def get_data(self, symbol, period, count=100):
        """Retorna uma lista de lista de cotações do MetaTrader."""
        period = period.upper()
        log.info(
            f"Iniciando coleta de dados via API MT5: {symbol} no timeframe {period}"
        )
        tf_map = {
            "M1": mt5.TIMEFRAME_M1,
            "M2": mt5.TIMEFRAME_M2,
            "M3": mt5.TIMEFRAME_M3,
            "M4": mt5.TIMEFRAME_M4,
            "M5": mt5.TIMEFRAME_M5,
            "M6": mt5.TIMEFRAME_M6,
            "M10": mt5.TIMEFRAME_M10,
            "M12": mt5.TIMEFRAME_M12,
            "M15": mt5.TIMEFRAME_M15,
            "M20": mt5.TIMEFRAME_M20,
            "M30": mt5.TIMEFRAME_M30,
            "H1": mt5.TIMEFRAME_H1,
            "H2": mt5.TIMEFRAME_H2,
            "H3": mt5.TIMEFRAME_H3,
            "H4": mt5.TIMEFRAME_H4,
            "H6": mt5.TIMEFRAME_H6,
            "H8": mt5.TIMEFRAME_H8,
            "H12": mt5.TIMEFRAME_H12,
            "D1": mt5.TIMEFRAME_D1,
            "W1": mt5.TIMEFRAME_W1,
            "MN1": mt5.TIMEFRAME_MN1,
        }

        if period.upper() not in tf_map:
            log.error(f"Timeframe inválido: {period}.")
            raise ValueError(f"Timeframe '{period}' inválido.")

        corretoras_b3 = [
            "clear",
            "xp",
            "rico",
            "modal",
            "terra",
            "btg",
            "toro",
        ]

        with mt5_conexao():
            for corretora in corretoras_b3:
                symbol = (
                    symbol.upper()
                    if corretora in mt5.account_info().company.lower()
                    else symbol
                )
            log.info(
                f"Finalizada verificacao da corretora para tratar symbol: {symbol}."
            )

            rates = mt5.copy_rates_from_pos(symbol, tf_map[period], 0, count)

        if rates is None:
            log.warning("Nenum dado retornado da API MT5.")
            raise ValueError("Nenhum dado retornado da API MT5.")

        result = []
        for r in rates:
            dt_str = (
                r["time"].astype("datetime64[s]").item().strftime("%Y.%m.%d %H:%M:%S")
            )
            result.append(
                [
                    dt_str,
                    r["open"],
                    r["high"],
                    r["low"],
                    r["close"],
                    r["tick_volume"],
                    r["real_volume"],
                ]
            )

        log.info("Coleta de dados via API MT5 finalizada.")
        return result

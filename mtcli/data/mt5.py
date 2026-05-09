"""
Módulo fonte de dados via API do MetaTrader 5.
"""

from datetime import datetime

import MetaTrader5 as mt5

from mtcli.logger import setup_logger
from mtcli.mt5_context import mt5_conexao
from .base import DataSourceBase

log = setup_logger(__name__)


# ---------------------------------------------------------
# Timeframes suportados (constante global)
# ---------------------------------------------------------

TF_MAP = {
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


# ---------------------------------------------------------
# DataSource
# ---------------------------------------------------------

class MT5DataSource(DataSourceBase):
    """Fonte de dados via API do MetaTrader 5."""

    CORRETORAS_B3 = (
        "clear",
        "xp",
        "rico",
        "modal",
        "terra",
        "btg",
        "toro",
    )

    def _normalize_symbol(self, symbol: str) -> str:
        """
        Normaliza símbolo dependendo da corretora.
        """
        info = mt5.account_info()

        if info is None:
            log.warning("Não foi possível obter account_info do MT5.")
            return symbol

        company = (info.company or "").lower()

        if any(c in company for c in self.CORRETORAS_B3):
            return symbol.upper()

        return symbol

    def _convert_time(self, timestamp) -> str:
        """
        Converte timestamp do MT5 para string padrão mtcli.
        """
        # MT5 geralmente retorna epoch (int)
        if isinstance(timestamp, (int, float)):
            dt = datetime.fromtimestamp(timestamp)
        else:
            # fallback seguro
            dt = datetime.fromtimestamp(int(timestamp))

        return dt.strftime("%Y.%m.%d %H:%M:%S")

    def get_data(self, symbol, period, count=100):
        """
        Retorna uma lista de listas no formato padrão mtcli.
        """

        period = period.upper()

        if period not in TF_MAP:
            log.error("Timeframe inválido: %s", period)
            raise ValueError(f"Timeframe '{period}' inválido.")

        log.info(
            "MT5 | coleta iniciada | symbol=%s period=%s count=%s",
            symbol,
            period,
            count,
        )

        with mt5_conexao():
            symbol_normalized = self._normalize_symbol(symbol)

            log.info("MT5 | símbolo normalizado: %s", symbol_normalized)

            rates = mt5.copy_rates_from_pos(
                symbol_normalized,
                TF_MAP[period],
                0,
                count,
            )

            if rates is None:
                error = mt5.last_error()
                log.error("MT5 | erro ao obter dados: %s", error)
                raise RuntimeError(f"Erro MT5: {error}")

        result = []

        for r in rates:
            try:
                result.append(
                    [
                        self._convert_time(r["time"]),
                        float(r["open"]),
                        float(r["high"]),
                        float(r["low"]),
                        float(r["close"]),
                        int(r["tick_volume"]) if r["tick_volume"] is not None else None,
                        int(r["real_volume"]) if r["real_volume"] is not None else None,
                    ]
                )
            except Exception:
                log.exception("Erro ao converter rate: %s", r)
                continue

        log.info("MT5 | coleta finalizada | %s registros", len(result))

        return result

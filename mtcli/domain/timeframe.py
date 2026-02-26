"""
Enum de Timeframes suportados pelo MTCLI Renko.

Fornece:
- Conversão amigável (m5, 5m, h1, 1h)
- Mapeamento para constante MT5
- Lista de valores válidos para CLI
"""

from enum import Enum
import MetaTrader5 as mt5


class Timeframe(Enum):
    """
    Representa timeframes suportados pelo MT5.
    """

    M1 = ("m1", mt5.TIMEFRAME_M1)
    M2 = ("m2", mt5.TIMEFRAME_M2)
    M3 = ("m3", mt5.TIMEFRAME_M3)
    M4 = ("m4", mt5.TIMEFRAME_M4)
    M5 = ("m5", mt5.TIMEFRAME_M5)
    M10 = ("m10", mt5.TIMEFRAME_M10)
    M15 = ("m15", mt5.TIMEFRAME_M15)
    M30 = ("m30", mt5.TIMEFRAME_M30)

    H1 = ("h1", mt5.TIMEFRAME_H1)
    H2 = ("h2", mt5.TIMEFRAME_H2)
    H3 = ("h3", mt5.TIMEFRAME_H3)
    H4 = ("h4", mt5.TIMEFRAME_H4)
    H6 = ("h6", mt5.TIMEFRAME_H6)
    H8 = ("h8", mt5.TIMEFRAME_H8)
    H12 = ("h12", mt5.TIMEFRAME_H12)

    D1 = ("d1", mt5.TIMEFRAME_D1)
    W1 = ("w1", mt5.TIMEFRAME_W1)
    MN1 = ("mn1", mt5.TIMEFRAME_MN1)

    def __init__(self, label: str, mt5_const: int):
        self.label = label
        self.mt5_const = mt5_const

    @classmethod
    def from_string(cls, value: str) -> "Timeframe":
        """
        Converte string amigável para Enum Timeframe.

        Aceita:
            m5, 5m
            h1, 1h
            d1, 1d
        """

        value = value.strip().lower()

        # Aliases humanos
        aliases = {
            "1m": "m1",
            "5m": "m5",
            "15m": "m15",
            "30m": "m30",
            "1h": "h1",
            "4h": "h4",
            "1d": "d1",
            "1w": "w1",
            "1mo": "mn1",
        }

        if value in aliases:
            value = aliases[value]

        for tf in cls:
            if tf.label == value:
                return tf

        raise ValueError(
            f"Timeframe inválido: {value}. "
            f"Use: {', '.join(cls.valid_labels())}"
        )

    @classmethod
    def valid_labels(cls):
        """
        Retorna lista de labels válidos.
        """
        return [tf.label for tf in cls]

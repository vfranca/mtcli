"""Módulo da classe model para saldo da agressão."""

from mtcli import conf


class AgressaoModel:
    """Classe model do saldo da agressao."""

    def __init__(self, bars, type="tick", count=5):
        """Construtor do saldo da agressão."""
        self.bars = bars[-count:]
        self.type = type
        self.count = count
        self.volume_comprador = self.__get_volume_comprador()
        self.volume_vendedor = self.__get_volume_vendedor()

    def __get_volume_comprador(self):
        """Obtem o volume comprador."""
        volume = 0
        for bar in self.bars:
            if (bar.trend == conf.alta and bar.body > 50) or bar.bottom > 50:
                volume += bar.volume if self.type == "tick" else bar.volume_real
        return volume

    def __get_volume_vendedor(self):
        """Obtem o volume vendedor."""
        volume = 0
        for bar in self.bars:
            if (bar.trend == conf.baixa and bar.body > 50) or bar.top > 50:
                volume += bar.volume if self.type == "tick" else bar.volume_real
        return volume

    def get_saldo(self):
        """Calcula o saldo da agressão."""
        return (
            self.volume_comprador,
            self.volume_vendedor,
            self.volume_comprador - self.volume_vendedor,
        )

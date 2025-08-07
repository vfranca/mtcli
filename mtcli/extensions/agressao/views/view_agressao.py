"""Módulo da classe da view saldo da agressão."""

from mtcli import conf


class AgressaoView:
    """Classe da view do saldo da agressao."""

    def __init__(self, saldo_agressao):
        """Construtor da view saldo da agressao."""
        self.agressao = saldo_agressao

    def view(self):
        """View do saldo da agressão."""
        return "%i %i %i" % (self.agressao[0], self.agressao[1], self.agressao[2])

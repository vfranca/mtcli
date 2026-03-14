"""
TickBus

Sistema simples de pub/sub para distribuição
de ticks em memória.

Todos os componentes podem se registrar
para receber eventos de ticks.
"""


class TickBus:

    def __init__(self):

        self.subscribers = []

    # -----------------------------------------------------

    def subscribe(self, handler):

        if handler not in self.subscribers:
            self.subscribers.append(handler)

    # -----------------------------------------------------

    def unsubscribe(self, handler):

        if handler in self.subscribers:
            self.subscribers.remove(handler)

    # -----------------------------------------------------

    def publish(self, symbol, ticks):

        for handler in list(self.subscribers):
            handler(symbol, ticks)

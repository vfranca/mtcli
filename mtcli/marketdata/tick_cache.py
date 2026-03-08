"""
Cache de ticks em memória.

Mantém uma janela recente de ticks para acesso rápido
sem necessidade de consultar o banco SQLite.
"""

from collections import deque


class TickCache:
    """
    Mantém uma janela deslizante de ticks em memória.

    Parameters
    ----------
    max_size : int
        Número máximo de ticks armazenados no cache.
    """

    def __init__(self, max_size=10000):
        self.buffer = deque(maxlen=max_size)

    def add_many(self, ticks):
        """
        Adiciona múltiplos ticks ao cache.
        """

        for t in ticks:
            self.buffer.append(t)

    def add(self, tick):
        """
        Adiciona um único tick ao cache.
        """

        self.buffer.append(tick)

    def get_all(self):
        """
        Retorna todos os ticks do cache.
        """

        return list(self.buffer)

    def get_last(self):
        """
        Retorna o último tick armazenado.
        """

        if self.buffer:
            return self.buffer[-1]

        return None

    def clear(self):
        """
        Limpa o cache.
        """

        self.buffer.clear()

"""
Cache de ticks em memória.
"""

from collections import deque


class TickCache:
    """
    Mantém janela recente de ticks em memória.
    """

    def __init__(self, max_size=10000):
        self.buffer = deque(maxlen=max_size)

    def add_many(self, ticks):
        for t in ticks:
            self.buffer.append(t)

    def get_all(self):
        return list(self.buffer)

    def clear(self):
        self.buffer.clear()

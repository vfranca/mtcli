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

    def add(self, tick):

        self.buffer.append(tick)

    def get_all(self):

        return list(self.buffer)

    def get_last(self):

        if self.buffer:
            return self.buffer[-1]

        return None

    def clear(self):

        self.buffer.clear()

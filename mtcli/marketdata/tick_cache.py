"""
Cache de ticks em memória.

Mantém uma janela recente de ticks para acesso rápido
sem necessidade de consultar o banco SQLite.

Este cache é usado principalmente por:

- plugins em tempo real
- cálculos de indicadores
- geração de renko
- tape reading
- consultas recentes

A estrutura utiliza `collections.deque`, que oferece:

- inserção O(1)
- remoção automática quando atinge max_size
- excelente performance para streams de dados
"""

from collections import deque
from typing import Iterable, Iterator, Any, List


class TickCache:
    """
    Mantém uma janela deslizante de ticks em memória.

    Parameters
    ----------
    max_size : int
        Número máximo de ticks armazenados no cache.
    """

    def __init__(self, max_size: int = 10000):

        self.buffer: deque = deque(maxlen=max_size)

    # ==========================================================
    # INSERÇÃO
    # ==========================================================

    def add(self, tick: Any) -> None:
        """
        Adiciona um único tick ao cache.

        Parameters
        ----------
        tick : Any
            Tick a ser armazenado.
        """

        self.buffer.append(tick)

    # ----------------------------------------------------------

    def add_many(self, ticks: Iterable[Any]) -> None:
        """
        Adiciona múltiplos ticks ao cache.

        Parameters
        ----------
        ticks : iterable
            Coleção de ticks.
        """

        for t in ticks:
            self.buffer.append(t)

    # ==========================================================
    # CONSULTA
    # ==========================================================

    def get_last(self) -> Any:
        """
        Retorna o último tick armazenado.

        Returns
        -------
        tick ou None
        """

        if self.buffer:
            return self.buffer[-1]

        return None

    # ----------------------------------------------------------

    def get_last_n(self, n: int) -> List[Any]:
        """
        Retorna os últimos N ticks do cache.

        Parameters
        ----------
        n : int
            Número de ticks desejados.

        Returns
        -------
        list
            Lista contendo os últimos ticks.
        """

        if n <= 0:
            return []

        return list(self.buffer)[-n:]

    # ----------------------------------------------------------

    def get_all(self) -> List[Any]:
        """
        Retorna todos os ticks armazenados no cache.

        Returns
        -------
        list
        """

        return list(self.buffer)

    # ==========================================================
    # UTILIDADES
    # ==========================================================

    def clear(self) -> None:
        """
        Limpa completamente o cache.
        """

        self.buffer.clear()

    # ----------------------------------------------------------

    def __len__(self) -> int:
        """
        Retorna o número atual de ticks armazenados.

        Permite uso de:

        len(cache)
        """

        return len(self.buffer)

    # ----------------------------------------------------------

    def __iter__(self) -> Iterator[Any]:
        """
        Permite iterar diretamente sobre o cache.

        Exemplo:

        for tick in cache:
            ...
        """

        return iter(self.buffer)

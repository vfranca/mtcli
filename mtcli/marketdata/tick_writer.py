"""
TickWriter

Subscriber do TickBus responsável por persistir ticks no banco.
"""

import logging


logger = logging.getLogger(__name__)


class TickWriter:
    """
    Recebe ticks do TickBus e grava no banco via TickRepository.
    """

    def __init__(self, repository):
        """
        Parameters
        ----------
        repository : TickRepository
            Repositório de persistência de ticks.
        """
        self.repository = repository

    # ---------------------------------------------------------

    def __call__(self, tick):
        """
        Método chamado pelo TickBus ao publicar um tick.
        """

        try:
            self.repository.insert_tick(tick)

        except Exception as e:
            logger.exception("Erro ao gravar tick: %s", e)

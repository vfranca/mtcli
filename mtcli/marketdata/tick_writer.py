"""
TickWriter

Subscriber do TickBus responsável por persistir ticks no banco.
"""

from mtcli.logger import setup_logger

logger = setup_logger(__name__)


class TickWriter:
    """
    Recebe ticks do TickBus e grava no banco via TickRepository.
    """

    def __init__(self, symbol, repository):

        self.symbol = symbol
        self.repository = repository

    # ---------------------------------------------------------

    def __call__(self, ticks):
        """
        Chamado pelo TickBus ao publicar ticks.
        """

        try:

            inserted = self.repository.insert_ticks(
                self.symbol,
                ticks
            )

            logger.debug(
                "TickWriter inseriu %s ticks (%s)",
                inserted,
                self.symbol
            )

        except Exception:

            logger.exception("Erro ao gravar ticks")

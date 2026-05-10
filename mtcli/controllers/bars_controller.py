"""
Controller do comando `bars`.

Orquestra o fluxo principal:
- coleta dados via DataSource
- converte para DTO
- transforma em BarsModel
- delega renderização para View

Não contém lógica de apresentação nem acesso direto à CLI.
"""

from ..logger import setup_logger
from ..models.rate_model import RateDTO
from ..models.bars_model import BarsModel
from ..views.factory_view import ViewFactory
from ..data.base import DataSourceBase

log = setup_logger(__name__)


class BarsController:
    """
    Controller responsável pela execução do comando `bars`.
    """

    def __init__(self, data_source: DataSourceBase):
        """
        Args:
            data_source (DataSourceBase): Fonte de dados (MT5, CSV, etc)
        """
        self.data_source = data_source

    def execute(
        self,
        symbol: str,
        period: str,
        count: int,
        date: str | None,
        view: str,
        numerator: bool,
        show_date: bool,
        volume: str | None,
    ) -> list[str]:
        """
        Executa o fluxo completo do comando.

        Returns:
            list[str]: Linhas prontas para impressão
        """
        log.info(
            "bars | symbol=%s period=%s count=%s view=%s date=%s",
            symbol,
            period,
            count,
            view,
            date,
        )

        raw_rates = self.data_source.get_data(symbol, period, count)

        rates = [RateDTO.from_list(rate) for rate in raw_rates]

        bars = BarsModel(rates, date_filter=date).build()

        view_instance = ViewFactory.create(
            name=view,
            bars=bars,
            period=period,
            numerator=numerator,
            show_date=show_date,
            volume=volume,
        )

        return view_instance.render()

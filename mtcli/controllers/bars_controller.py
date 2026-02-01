from mtcli.logger import setup_logger
from mtcli.models.rate import RateDTO
from mtcli.models.bars import BarsModel
from mtcli.views.factory import ViewFactory
from mtcli.data.base import DataSourceBase

log = setup_logger(__name__)


class BarsController:
    """
    Controller do comando bars.

    Responsável por orquestrar:
    - coleta de dados (DataSource)
    - conversão para models
    - renderização via View
    """

    def __init__(self, data_source: DataSourceBase):
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
        log.info(
            "bars | symbol=%s period=%s count=%s view=%s",
            symbol,
            period,
            count,
            view,
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


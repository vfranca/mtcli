from mtcli.logger import setup_logger
from mtcli.models.rates_model import RatesModel

from .model import MediaMovelModel

logger = setup_logger()


def obter_media_movel(symbol, period, limit, tipo, inicio, fim, linhas=5):
    logger.info(
        f"Iniciando cálculo da média móvel: ativo {symbol} período {period} períodos {periodos} tipo {tipo} limite {limit}"
    )

    rates = RatesModel(symbol, period).get_data()
    closes = [r[4] for r in rates]
    datas = [r[0] for r in rates]

    if len(closes) < limit:
        logger.warning("Dados insuficientes para calcular a média.")
        raise ValueError("Dados insuficientes para calcular a média.")

    model_mm = MediaMovelModel(closes, limit)
    if tipo == "sma":
        medias = model_mm.calcula_sma()
    else:
        medias = model_mm.calcula_ema()

    datas = datas[limit - 1 :]

    # Filtro por data/hora
    dt_inicio = datetime.fromisoformat(inicio) if inicio else None
    dt_fim = datetime.fromisoformat(fim) if fim else None

    # formato compatível com '2023.08.31 00:00:00'
    formato = "%Y.%m.%d %H:%M:%S"

    filtrado = []
    for d, m in zip(datas, medias):
        dt = datetime.strptime(d, formato)
        if (not dt_inicio or dt >= dt_inicio) and (not dt_fim or dt <= dt_fim):
            filtrado.append((d, m))

    return filtrado

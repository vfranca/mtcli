"""
Gerencia configurações
"""

import click
import dotenv
import os
import MetaTrader5 as mt5


fconf = "mtcli.ini"
dotenv.load_dotenv(fconf)
digitos = int(os.getenv("DIGITOS", 2))
lateral = os.getenv("LATERAL", "DOJI")
alta = os.getenv("ALTA", "VERDE")
baixa = os.getenv("BAIXA", "VERMELHO")
rompimento_alta = os.getenv("ROMPIMENTO_ALTA", "C")
rompimento_baixa = os.getenv("ROMPIMENTO_BAIXA", "V")
percentual_doji = os.getenv("PERCENTUAL_DOJI", 60)
percentual_rompimento = float(os.getenv("PERCENTUAL_ROMPIMENTO", 50))
up_bar = os.getenv("UP_BAR", "ASC")
down_bar = os.getenv("DOWN_BAR", "DESC")
inside_bar = os.getenv("INSIDE_BAR", "IB")
outside_bar = os.getenv("OUTSIDE_BAR", "OB")
toptail = os.getenv("TOPTAIL", "TOP")
bottomtail = os.getenv("BOTTOMTAIL", "BOTTOM")
notail = os.getenv("NOTAIL", "")

mt5.initialize()
info = mt5.terminal_info()
csv_path = info.data_path + "/MQL5/Files"
mt5.shutdown()
csv_path = os.getenv("MT5_PASTA", csv_path)
csv_path = csv_path.replace("\\", "/")
csv_path += "/"


@click.command()
@click.option("--digitos", "-d", help="Digitos da moeda.")
@click.option("--lateral", "-l", help="Nome da barra doji.")
@click.option("--alta", "-a", help="Nome da barra de alta.")
@click.option("--baixa", "-b", help="Nome da barra de baixa.")
@click.option(
    "--rompimento-alta", "-ra", help="Abreviatura da barra de rompimento de alta."
)
@click.option(
    "--rompimento-baixa", "-rb", help="Abreviatura da barra de rompimento de baixa."
)
@click.option("--percentual-doji", "-pd", help="Percentual do corpo da barra doji.")
@click.option(
    "--percentual-rompimento", "-pr", help="Percentual do corpo da barra de rompimento."
)
@click.option("--mt5-pasta", "-mp", help="Caminho da pasta do MetaTrader 5.")
def conf(**kwargs):
    """Gerencia configuracoes."""
    res = False
    # Altera os dígitos da moeda
    if kwargs["digitos"]:
        res = dotenv.set_key(fconf, "DIGITOS", kwargs["digitos"])
    # Altera o nome da barra lateral
    if kwargs["lateral"]:
        res = dotenv.set_key(fconf, "LATERAL", kwargs["lateral"].upper())
    # Altera o nome da barra de alta
    if kwargs["alta"]:
        res = dotenv.set_key(fconf, "ALTA", kwargs["alta"].upper())
    # Altera o nome da barra de baixa
    if kwargs["baixa"]:
        res = dotenv.set_key(fconf, "BAIXA", kwargs["baixa"].upper())
    # Altera a abreviatura da barra de rompimento de alta
    if kwargs["rompimento_alta"]:
        res = dotenv.set_key(
            fconf, "ROMPIMENTO_ALTA", kwargs["rompimento_alta"].upper()
        )
    # Altera a abreviatura da barra de rompimento de baixa
    if kwargs["rompimento_baixa"]:
        res = dotenv.set_key(
            fconf, "ROMPIMENTO_BAIXA", kwargs["rompimento_baixa"].upper()
        )
    # Altera o percentual do corpo da barra doji
    if kwargs["percentual_doji"]:
        res = dotenv.set_key(fconf, "PERCENTUAL_DOJI", kwargs["percentual_doji"])
    # Altera o percentual do corpo da barra de rompimento
    if kwargs["percentual_rompimento"]:
        res = dotenv.set_key(
            fconf, "PERCENTUAL_ROMPIMENTO", kwargs["percentual_rompimento"]
        )
    # Altera o caminho da pasta do MT5
    if kwargs["mt5_pasta"]:
        res = dotenv.set_key(fconf, "MT5_PASTA", kwargs["mt5_pasta"])
    if res:
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Lista as variáveis disponíveis
    vars = dotenv.dotenv_values(fconf)
    for var in vars.items():
        click.echo("%s=%s" % (var[0], var[1]))


if __name__ == "__main__":
    conf()

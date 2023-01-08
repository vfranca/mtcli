# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click
from dotenv import dotenv_values, set_key


# Cria o comando set
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
def set(**kwargs):
    """Manipula as variáveis de ambiente."""
    # Define o arquivo de variáveis
    env_file = ".mtcli"
    # Altera os dígitos da moeda
    if kwargs["digitos"]:
        res = set_key(env_file, "DIGITOS", kwargs["digitos"])
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera o nome da barra lateral
    if kwargs["lateral"]:
        res = set_key(env_file, "LATERAL", kwargs["lateral"].upper())
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera o nome da barra de alta
    if kwargs["alta"]:
        res = set_key(env_file, "ALTA", kwargs["alta"].upper())
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera o nome da barra de baixa
    if kwargs["baixa"]:
        res = set_key(env_file, "BAIXA", kwargs["baixa"].upper())
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera a abreviatura da barra de rompimento de alta
    if kwargs["rompimento_alta"]:
        res = set_key(env_file, "ROMPIMENTO_ALTA", kwargs["rompimento_alta"].upper())
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera a abreviatura da barra de rompimento de baixa
    if kwargs["rompimento_baixa"]:
        res = set_key(env_file, "ROMPIMENTO_BAIXA", kwargs["rompimento_baixa"].upper())
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera o percentual do corpo da barra doji
    if kwargs["percentual_doji"]:
        res = set_key(env_file, "PERCENTUAL_DOJI", kwargs["percentual_doji"])
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera o percentual do corpo da barra de rompimento
    if kwargs["percentual_rompimento"]:
        res = set_key(
            env_file, "PERCENTUAL_ROMPIMENTO", kwargs["percentual_rompimento"]
        )
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera o caminho da pasta do MT5
    if kwargs["mt5_pasta"]:
        res = set_key(env_file, "MT5_PASTA", kwargs["mt5_pasta"])
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Lista as variáveis disponíveis
    vars = dotenv_values(env_file)
    for var in vars.items():
        click.echo("%s=%s" % (var[0], var[1]))


if __name__ == "__main__":
    set()

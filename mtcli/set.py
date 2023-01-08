# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click
from dotenv import dotenv_values, set_key


# Cria o comando set
@click.command()
@click.option("--digits", "-d")
@click.option("--lateral", "-l")
@click.option("--alta", "-a")
@click.option("--baixa", "-b")
@click.option("--rompimento-alta", "-ra")
@click.option("--rompimento-baixa", "-rb")
def set(**kwargs):
    """Manipula as variáveis de ambiente."""
    # Define o arquivo de variáveis
    env_file = ".mtcli"
    # Altera os dígitos da moeda
    if kwargs["digits"]:
        res = set_key(env_file, "DIGITS", kwargs["digits"])
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
    # Lista as variáveis disponíveis
    vars = dotenv_values(env_file)
    for var in vars.items():
        click.echo("%s=%s" % (var[0], var[1]))


if __name__ == "__main__":
    set()

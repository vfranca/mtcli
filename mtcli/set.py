# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click
from dotenv import dotenv_values, set_key


# Cria o comando set
@click.command()
@click.option("--digits", "-d")
@click.option("--alta", "-a")
@click.option("--baixa", "-b")
def set(digits, alta, baixa):
    """Manipula as variáveis de ambiente."""
    # Define o arquivo de variáveis
    env_file = ".mtcli"
    # Altera os dígitos da moeda
    if digits:
        res = set_key(env_file, "DIGITS", digits)
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera o nome da barra de alta
    if alta:
        res = set_key(env_file, "ALTA", alta.upper())
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Altera o nome da barra de alta
    if baixa:
        res = set_key(env_file, "BAIXA", baixa.upper())
        click.echo("%s=%s" % (res[1], res[2]))
        return 0
    # Lista as variáveis disponíveis
    vars = dotenv_values(env_file)
    for var in vars.items():
        click.echo("%s=%s" % (var[0], var[1]))


if __name__ == "__main__":
    set()

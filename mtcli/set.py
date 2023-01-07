# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click
from dotenv import dotenv_values


# Cria o comando set
@click.command()
@click.option("--chave", "-c", help="")
@click.option("--valor", "-v", help="")
def set(chave, valor):
    """Manipula as variáveis de ambiente."""
    # Lista as variáveis disponíveis
    vars = dotenv_values(".mtcli")
    for var in vars.items():
        click.echo("%s=%s" % (var[0], var[1]))


if __name__ == "__main__":
    set()

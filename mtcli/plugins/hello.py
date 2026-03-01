"""
Plugin interno de exemplo para mtcli.

Este plugin demonstra como criar um comando interno simples.
"""

import click

def register(cli):
    """
    Registra o comando `hello` no CLI principal.

    Args:
        cli (click.Group): grupo principal do Click (`mt`)
    """
    @cli.command()
    @click.option("--name", "-n", default="Mundo", help="Nome para saudação")
    def hello(name):
        """Exibe uma saudação simples."""
        click.echo(f"Olá, {name}! Este é um plugin interno de exemplo.")

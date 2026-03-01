"""
Registro de plugins internos do mtcli.
"""

from mtcli.plugins import hello

def register(cli):
    """
    Registra todos os plugins internos no CLI principal.

    Args:
        cli (click.Group): grupo Click principal (`mt`)
    """
    hello.register(cli)

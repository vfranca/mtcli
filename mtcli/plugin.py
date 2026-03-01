"""
Registro de plugins internos do mtcli.
"""

from mtcli.plugins import media_movel
from mtcli.plugins import range_medio
from mtcli.plugins import volume_medio

def register(cli):
    """
    Registra todos os plugins internos no CLI principal.

    Args:
        cli (click.Group): grupo Click principal (`mt`)
    """
    media_movel.register(cli)
    range_medio.register(cli)
    volume_medio.register(cli)

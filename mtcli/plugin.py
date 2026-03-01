<<<<<<< HEAD
# from .plugins.media_movel.cli import mm
# from .plugins.range_medio.cli import rm
# from .plugins.volume_medio.cli import vm
=======
"""
Registro de plugins internos do mtcli.
"""
>>>>>>> master

from mtcli.plugins import media_movel
from mtcli.plugins import range_medio
from mtcli.plugins import volume_medio

def register(cli):
<<<<<<< HEAD
    pass
    # cli.add_command(mm, name="mm")
    # cli.add_command(rm, name="rm")
    # cli.add_command(vm, name="vm")
=======
    """
    Registra todos os plugins internos no CLI principal.

    Args:
        cli (click.Group): grupo Click principal (`mt`)
    """
    media_movel.register(cli)
    range_medio.register(cli)
    volume_medio.register(cli)
>>>>>>> master

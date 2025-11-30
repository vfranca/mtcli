from .plugins.media_movel.cli import mm
from .plugins.range_medio.cli import rm
from .plugins.volume_medio.cli import vm


def register(cli):
    cli.add_command(mm, name="mm")
    cli.add_command(rm, name="rm")
    cli.add_command(vm, name="vm")

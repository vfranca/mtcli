from mtcli.commands.bars import bars
from mtcli.commands.conf import conf
from mtcli.commands.logs import logs


def register(cli):
    cli.add_command(bars)
    cli.add_command(conf)
    cli.add_command(logs)

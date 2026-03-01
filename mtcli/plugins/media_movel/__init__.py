from .cli import mm


def register(cli):
    cli.add_command(mm, name="mm")

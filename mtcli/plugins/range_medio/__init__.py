from .cli import rm


def register(cli):
    cli.add_command(rm, name="rm")

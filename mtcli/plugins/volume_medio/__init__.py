from .cli import vm


def register(cli):
    cli.add_command(vm, name="vm")

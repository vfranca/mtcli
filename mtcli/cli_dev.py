import click
from .commands_dev.migrate import migrate

@click.group()
def cli():
    pass

cli.add_command(migrate)

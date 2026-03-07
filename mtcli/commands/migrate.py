import click
from mtcli.database import get_connection
from mtcli.migrations.runner import run_migrations


@click.command()
def migrate():

    conn = get_connection()

    run_migrations(conn)

    print("Migrations concluídas.")

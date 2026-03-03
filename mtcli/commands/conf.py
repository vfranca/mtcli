"""
Comando para exibir configurações disponíveis.
"""

import click

from mtcli.config_registry import registry
from mtcli.conf import conf


@click.command()
@click.argument("section", required=False)
def conf_cmd(section):
    """
    Exibe configurações disponíveis.

    Exemplos:

        mt conf
        mt conf renko
    """

    if section:
        options = registry.get_section(section)
    else:
        options = registry.get_all()

    if not options:
        click.echo("Nenhuma configuração registrada.")
        return

    for opt in options:

        value = conf.get(opt.name, section=opt.section, default=opt.default)

        click.echo(
            f"{opt.section}.{opt.name} = {value} "
            f"(default={opt.default})"
        )

        if opt.description:
            click.echo(f"  {opt.description}")

        click.echo()

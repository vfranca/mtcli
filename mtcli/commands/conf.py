"""Gerencia configurações registradas no mtcli.ini."""

import click

from mtcli.models.conf_model import ConfModel


@click.command(
    "conf",
    help="Gerencia as configurações salvas no arquivo mtcli.ini (adicionar, editar, listar).",
)
@click.option("--list", "list_", is_flag=True, help="Lista todas as configurações.")
@click.option("--set", "set_", nargs=2, help="Define o valor de uma configuração.")
@click.option("--get", help="Exibe o valor de uma configuração.")
@click.option("--reset", is_flag=True, help="Redefine as configurações padrão.")
def conf(list_, set_, get, reset):
    """Gerencia configurações registradas no mtcli.ini."""
    conf = ConfModel("mtcli.ini")
    config = conf.carregar()

    if list_:
        for key in config["DEFAULT"]:
            click.echo(f"{key} = {config['DEFAULT'][key]}")

    elif set_:
        chave, valor = set_
        config["DEFAULT"][chave] = valor
        conf.salvar(config)
        click.echo(f"Configuração '{chave}' definida como '{valor}'.")

    elif get:
        valor = config["DEFAULT"].get(get)
        if valor is not None:
            click.echo(f"{get} = {valor}")
        else:
            click.echo(f"Configuração '{get}' não encontrada.")

    elif reset:
        config["DEFAULT"].clear()
        conf.salvar(config)
        click.echo("Configurações redefinidas.")

    else:
        click.echo(
            "Nenhuma opção fornecida. Use --help para ver as opções disponíveis."
        )


if __name__ == "__main__":
    conf()

"""Módulo principal do aplicativo."""

import click

try:
    from importlib.metadata import entry_points
except ImportError:
    from importlib_metadata import entry_points  # Para Python < 3.8


@click.group()
@click.version_option(package_name="mtcli")
def mt():
    """Exibe o grafico do MetaTrader 5 em texto."""
    pass


def load_plugins():
    eps = entry_points()
    plugins = (
        eps.select(group="mtcli.plugins")
        if hasattr(eps, "select")
        else eps.get("mtcli.plugins", [])
    )

    for ep in plugins:
        plugin = ep.load()

        # Caso seja uma função register(cli)
        if callable(plugin) and not isinstance(plugin, click.Command):
            plugin(mt)  # chama register(cli)
        # Caso seja um comando Click diretamente
        elif isinstance(plugin, click.Command):
            mt.add_command(plugin)
        else:
            raise TypeError(
                f"Plugin {ep.name} inválido: não é um comando nem função register."
            )


load_plugins()


if __name__ == "__main__":
    mt()

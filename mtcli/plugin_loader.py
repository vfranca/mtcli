"""
Sistema de carregamento de plugins do mtcli.

Este módulo carrega automaticamente:

1. Plugins internos localizados em `mtcli.plugins`
2. Plugins externos registrados via entry points `mtcli.plugins`

Plugins devem expor uma função:

    register(cli)

onde `cli` é o grupo principal do Click.
"""

import importlib
import pkgutil

import click

try:
    from importlib.metadata import entry_points
except ImportError:  # Python < 3.10
    from importlib_metadata import entry_points

import mtcli.plugins


def load_internal_plugins(cli: click.Group) -> None:
    """
    Carrega plugins internos do pacote `mtcli.plugins`.

    Cada módulo encontrado deve expor a função:

        register(cli)

    Args:
        cli: grupo principal do Click.
    """

    for module_info in pkgutil.iter_modules(mtcli.plugins.__path__):

        module_name = f"mtcli.plugins.{module_info.name}"

        module = importlib.import_module(module_name)

        if hasattr(module, "register"):
            module.register(cli)


def load_external_plugins(cli: click.Group) -> None:
    """
    Carrega plugins externos instalados via entry points.

    Os plugins devem declarar no pyproject.toml:

        [project.entry-points."mtcli.plugins"]
        nome = "pacote.plugin:register"

    Args:
        cli: grupo principal do Click.
    """

    eps = entry_points()

    plugins = (
        eps.select(group="mtcli.plugins")
        if hasattr(eps, "select")
        else eps.get("mtcli.plugins", [])
    )

    for ep in plugins:

        plugin = ep.load()

        if callable(plugin) and not isinstance(plugin, click.Command):
            plugin(cli)

        elif isinstance(plugin, click.Command):
            cli.add_command(plugin)

        else:
            raise TypeError(
                f"Plugin {ep.name} inválido: deve ser um comando Click ou função register."
            )


def load_plugins(cli: click.Group) -> None:
    """
    Carrega todos os plugins (internos e externos).

    Args:
        cli: grupo principal do Click.
    """

    load_internal_plugins(cli)
    load_external_plugins(cli)

"""
Módulo responsável pelo carregamento de plugins do mtcli.

Carrega plugins internos (via mtcli.plugin.register) e plugins externos
registrados via entry points (`mtcli.plugins`).
"""

import click

try:
    from importlib.metadata import entry_points
except ImportError:
    from importlib_metadata import entry_points  # Para Python < 3.8

from mtcli import plugin as internal_plugin


def load_plugins(cli: click.Group):
    """
    Carrega todos os plugins (internos e externos) e registra-os no CLI.

    Args:
        cli (click.Group): grupo Click principal (ex.: `mt`).

    Comportamento:
        - Plugins internos são registrados via `mtcli.plugin.register(cli)`.
        - Plugins externos são carregados via entry points `mtcli.plugins`.
          - Se o entry point for uma função, chama `plugin(cli)`.
          - Se for um `click.Command`, adiciona diretamente com `cli.add_command()`.
          - Caso contrário, lança TypeError.
    """
    # --- Carrega plugins internos ---
    internal_plugin.register(cli)

    # --- Carrega plugins externos via entry points ---
    eps = entry_points()
    plugins = (
        eps.select(group="mtcli.plugins")
        if hasattr(eps, "select")
        else eps.get("mtcli.plugins", [])
    )

    for ep in plugins:
        try:
            plugin_obj = ep.load()
        except Exception as e:
            raise RuntimeError(f"Falha ao carregar plugin {ep.name}: {e}") from e

        if callable(plugin_obj) and not isinstance(plugin_obj, click.Command):
            # função register(cli)
            plugin_obj(cli)
        elif isinstance(plugin_obj, click.Command):
            cli.add_command(plugin_obj)
        else:
            raise TypeError(
                f"Plugin {ep.name} inválido: não é um comando nem função register."
            )

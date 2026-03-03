"""
Carregador de plugins do mtcli.

Responsável por descobrir e registrar plugins internos e externos
utilizando entry points.

Plugins podem expor:

1. função register(cli)
2. objeto click.Command
"""

import logging
import click

try:
    from importlib.metadata import entry_points
except ImportError:  # pragma: no cover
    from importlib_metadata import entry_points


logger = logging.getLogger(__name__)


def load_plugins(cli):
    """
    Descobre e carrega plugins registrados via entry points.

    Args:
        cli (click.Group): CLI principal.
    """

    try:
        eps = entry_points()

        plugins = (
            eps.select(group="mtcli.plugins")
            if hasattr(eps, "select")
            else eps.get("mtcli.plugins", [])
        )

    except Exception as exc:
        logger.error("Erro ao descobrir plugins: %s", exc)
        return

    loaded = set()

    for ep in plugins:

        if ep.name in loaded:
            logger.warning("Plugin duplicado ignorado: %s", ep.name)
            continue

        try:

            plugin = ep.load()

            # função register(cli)
            if callable(plugin) and not isinstance(plugin, click.Command):
                plugin(cli)

            # comando click direto
            elif isinstance(plugin, click.Command):
                cli.add_command(plugin)

            else:
                raise TypeError(
                    "Plugin não é comando Click nem função register(cli)"
                )

            loaded.add(ep.name)

            logger.debug("Plugin carregado: %s", ep.name)

        except Exception as exc:

            logger.error(
                "Falha ao carregar plugin '%s': %s",
                ep.name,
                exc,
            )

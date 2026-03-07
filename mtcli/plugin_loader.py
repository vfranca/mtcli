"""
Sistema de carregamento de plugins do mtcli.

Descobre e registra plugins instalados via entry points.

Plugins devem declarar:

    [project.entry-points."mtcli.plugins"]
    nome = "pacote.plugin:register"

O plugin pode fornecer:

1. register(cli)
2. um objeto click.Command
"""

from __future__ import annotations

from typing import Iterable, List

import click

try:
    from importlib.metadata import EntryPoint, entry_points
except ImportError:  # pragma: no cover
    from importlib_metadata import EntryPoint, entry_points

from mtcli.logger import setup_logger


logger = setup_logger(__name__)

PLUGIN_GROUP = "mtcli.plugins"


def discover_plugins() -> Iterable[EntryPoint]:
    """
    Descobre plugins registrados via entry points.

    Returns
    -------
    Iterable[EntryPoint]
        Entry points encontrados.
    """

    try:
        eps = entry_points()

        if hasattr(eps, "select"):
            plugins = eps.select(group=PLUGIN_GROUP)
        else:
            plugins = eps.get(PLUGIN_GROUP, [])

        logger.debug("Plugins descobertos: %s", [ep.name for ep in plugins])

        return plugins

    except Exception as exc:
        logger.exception("Erro ao descobrir plugins: %s", exc)
        return []


def register_plugin(cli: click.Group, ep: EntryPoint) -> None:
    """
    Carrega e registra um plugin individual.
    """

    logger.debug("Carregando plugin: %s -> %s", ep.name, ep.value)

    plugin = ep.load()

    if callable(plugin) and not isinstance(plugin, click.Command):

        plugin(cli)

        logger.info("Plugin registrado via register(): %s", ep.name)

    elif isinstance(plugin, click.Command):

        cli.add_command(plugin)

        logger.info("Plugin registrado como comando: %s", ep.name)

    else:

        raise TypeError(
            f"Plugin '{ep.name}' inválido: "
            "não é click.Command nem função register(cli)"
        )


def load_plugins(cli: click.Group) -> List[str]:
    """
    Descobre e carrega todos os plugins instalados.
    """

    loaded: List[str] = []
    seen = set()

    for ep in discover_plugins():

        if ep.name in seen:
            logger.warning("Plugin duplicado ignorado: %s", ep.name)
            continue

        try:

            register_plugin(cli, ep)

            seen.add(ep.name)
            loaded.append(ep.name)

        except Exception as exc:

            logger.exception(
                "Falha ao carregar plugin '%s': %s",
                ep.name,
                exc,
            )

    logger.info("Total de plugins carregados: %d", len(loaded))

    return loaded

"""
Comando principal do mtcli.
"""

import click
from mtcli.plugin_loader import load_plugins

# --- CLI principal ---
@click.group(context_settings={"max_content_width": 120})
@click.version_option(package_name="mtcli")
def mt():
    """
    MTCLI - CLI para gráficos candlestick screen reader friendly.

    Comandos disponíveis:
        - Subcomandos (bars, conf, logs)
        - Plugins internos e externos
    """
    pass

# --- Carrega subcomandos do mt e plugins ---
# Os comandos do diretório commands são registrados aqui diretamente
from mtcli.commands import bars

mt.add_command(bars.bars, name="bars")

# --- Carrega plugins internos e externos via plugin_loader ---
load_plugins(mt)

# --- Entry point para execução direta ---
if __name__ == "__main__":
    mt()

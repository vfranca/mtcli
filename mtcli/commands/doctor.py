"""
Comando de diagnóstico do mtcli.

Este comando executa uma série de verificações básicas para ajudar
a identificar problemas de instalação, configuração ou carregamento
de plugins no ambiente do mtcli.

As verificações incluem:

- Versão do Python
- Instalação do mtcli
- Fonte de dados configurada
- Caminho de dados CSV
- Conexão com MetaTrader5
- Descoberta e carregamento de plugins

Caso algum plugin falhe ao carregar, o erro é exibido e registrado
no sistema de logs.
"""

import sys
import click
import traceback

from importlib.metadata import version, PackageNotFoundError

import MetaTrader5 as mt5

from mtcli.logger import setup_logger
from mtcli.conf import conf, DATA_SOURCE_NAME
from mtcli.mt5_context import mt5_conexao
from mtcli.plugin_loader import discover_plugins


logger = setup_logger(__name__)


def status(ok: bool) -> str:
    """
    Retorna um marcador visual simples de status.

    Parameters
    ----------
    ok : bool
        Indica se o teste foi bem sucedido.

    Returns
    -------
    str
        Texto representando o status.
    """
    return "OK " if ok else "ERRO"


@click.command()
def doctor():
    """
    Executa diagnóstico do ambiente mtcli.

    O comando verifica se os componentes essenciais do ambiente
    estão funcionando corretamente e apresenta um relatório simples
    no terminal.
    """

    click.echo("Diagnóstico do ambiente mtcli\n")

    # ---------------------------------------------------------
    # Python
    # ---------------------------------------------------------

    python_ok = sys.version_info >= (3, 10)

    click.echo(f"{status(python_ok)} Python: {sys.version.split()[0]}")

    if not python_ok:
        click.echo("   Versão mínima recomendada: Python 3.10")

    # ---------------------------------------------------------
    # mtcli
    # ---------------------------------------------------------

    try:

        mtcli_version = version("mtcli")

        click.echo(f"{status(True)} mtcli: {mtcli_version}")

    except PackageNotFoundError:

        click.echo(f"{status(False)} mtcli não encontrado")

        logger.error("Pacote mtcli não encontrado no ambiente.")

    # ---------------------------------------------------------
    # Fonte de dados
    # ---------------------------------------------------------

    click.echo(f"{status(True)} Data source: {DATA_SOURCE_NAME}")

    # ---------------------------------------------------------
    # CSV path
    # ---------------------------------------------------------

    try:

        path = conf.get_csv_path()

        click.echo(f"{status(True)} CSV path: {path}")

    except Exception as exc:

        click.echo(f"{status(False)} CSV path inválido")

        logger.exception("Erro ao obter CSV path: %s", exc)

    # ---------------------------------------------------------
    # MT5 conexão
    # ---------------------------------------------------------

    try:

        with mt5_conexao():

            info = mt5.terminal_info()

            if info:

                click.echo(f"{status(True)} MetaTrader5 conectado")

            else:

                click.echo(f"{status(False)} MetaTrader5 não respondeu")

    except Exception as exc:

        click.echo(f"{status(False)} Falha na conexão MT5")

        logger.exception("Erro ao conectar MT5: %s", exc)

    # ---------------------------------------------------------
    # Plugins
    # ---------------------------------------------------------

    click.echo("\nPlugins:")

    try:

        entry_points = list(discover_plugins())

        if not entry_points:

            click.echo("   Nenhum plugin encontrado.")
            return

        ok_count = 0
        fail_count = 0

        for ep in entry_points:

            plugin_name = ep.name

            try:

                ep.load()

                click.echo(f"   OK  {plugin_name}")

                ok_count += 1

            except Exception as exc:

                click.echo(f"   ERRO {plugin_name}")

                click.echo(f"       {exc}")

                logger.error(
                    "Erro ao carregar plugin %s\n%s",
                    plugin_name,
                    traceback.format_exc(),
                )

                fail_count += 1

        click.echo(
            f"\nResumo: {ok_count} plugins OK | {fail_count} com erro"
        )

    except Exception as exc:

        click.echo(f"{status(False)} Falha ao descobrir plugins")

        logger.exception("Erro ao descobrir plugins: %s", exc)

    click.echo("\nDiagnóstico concluído.")

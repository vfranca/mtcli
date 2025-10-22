"""Comando logs para exibição dos logs."""

import os

import click

from mtcli.logger import setup_logger


@click.command("logs", help="Exibe ou limpa os logs de execução do mtcli.")
@click.option("--clear", is_flag=True, help="Limpa o arquivo de log.")
@click.option("--tail", default=0, type=int, help="Mostra apenas as últimas N linhas.")
@click.option("--grep", default="", help="Filtra o log por uma palavra-chave.")
def logs(clear, tail, grep):
    """Exibe ou limpa os registros de log do mtcli."""
    logger = setup_logger()
    log_file = logger.handlers[0].baseFilename

    if clear:
        if os.path.exists(log_file):
            open(log_file, "w", encoding="utf-8").close()
            click.echo("Log limpo com sucesso.")
        else:
            click.echo("Nenhum log para limpar.")
        return

    if not os.path.exists(log_file):
        click.echo("Nenhum log encontrado.")
        return

    with open(log_file, encoding="utf-8", errors="ignore") as f:
        linhas = f.readlines()

    if tail > 0:
        linhas = linhas[-tail:]
    if grep:
        linhas = [linha for linha in linhas if grep.lower() in linha.lower()]

    if not linhas:
        click.echo("Nenhuma linha encontrada com os filtros aplicados.")
    else:
        click.echo_via_pager("".join(linhas))

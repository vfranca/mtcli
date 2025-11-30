import click

from .conf import DIGITOS


def exibir_media_movel(resultado, linhas):
    if not resultado:
        click.echo("Nenhum dado no intervalo especificado.")
        return

    if linhas > 0:
        resultado = resultado[-linhas:]

    for dt, valor in resultado:
        click.echo(f"{round(valor, DIGITOS)}    {dt}")

"""
Comando CLI para execução das migrations do banco de dados.

Este comando aplica todas as migrations pendentes no banco
utilizado pelo mtcli.

Fluxo de execução:

1. Abre conexão com o banco SQLite
2. Executa o migration runner
3. Aplica migrations ainda não executadas

Uso:

    mtcli migrate

Este comando é implementado utilizando o framework
:contentReference[oaicite:1]{index=1} para construção de aplicações CLI.
"""

import click

from mtcli.database import get_connection
from mtcli.migrations.runner import run_migrations


@click.command()
def migrate():
    """
    Executa as migrations pendentes do banco de dados.

    O comando conecta ao banco configurado no mtcli
    e executa o migration runner responsável por:

    - detectar migrations disponíveis
    - identificar a versão atual do schema
    - aplicar migrations pendentes
    - registrar migrations aplicadas

    Este comando é normalmente executado:

    - na primeira inicialização do sistema
    - após atualização de versão do mtcli
    """

    conn = get_connection()

    run_migrations(conn)

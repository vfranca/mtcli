=========
cli-trade
=========

.. image:: https://img.shields.io/pypi/v/cli_trade.svg
        :target: https://pypi.python.org/pypi/cli_trade

.. image:: https://img.shields.io/travis/vfranca/cli_trade.svg
        :target: https://travis-ci.org/vfranca/cli_trade

.. image:: https://readthedocs.org/projects/cli-trade/badge/?version=latest
        :target: https://cli-trade.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Provê uma interface de linha de comando para ler gráficos de preços gerados pelo MetaTrader 5.

* Free software: MIT license
* Documentation: https://cli-trade.readthedocs.io.

Pré-requisitos
--------

* MetaTrader 5
* Python 3

Exemplos de Comandos
--------

> py reader.py winq19daily.csv 20  

Exibe as últimas 20 barras do diário do winq19.

> py reader.py winq19daily.csv ch 20  

Exibe o canal das últimas 20 barras do diário do winq19.

> py reader.py winq19daily.csv o 20  

Exibe o preço de abertura das últimas 20 barras do diário do winq19.

> py reader.py winq19daily.csv c 20  

Exibe o preço de fechamento das últimas 20 barras do diário do winq19.

> py reader.py winq19daily.csv h 20  

Exibe o preço máximo das últimas 20 barras do diário do winq19.

> py reader.py winq19daily.csv l 20  

Exibe o preço mínimo das últimas 20 barras do diário do winq19.

> py reader.py winq19daily.csv r 20  

Exibe o range das últimas 20 barras do diário do winq19.

> py reader.py winq19daily.csv vol 20  

Exibe o volume das últimas 20 barras do diário do winq19.

> py atr.py winq19daily  

Exibe o ATR(14) do diário do winq19.

> py atr.py winq19 20  

Exibe o ATR(20) do diário do winq19.

> py sma.py 20 winq19daily.csv  

Exibe a média móvel aritmética de 20 períodos do diário do winq19.

> py ema.py 20 winq19daily.csv  

Exibe a média móvel exponencial de 20 períodos do diário do winq19.

> py fibo.py 103900 102100 h  

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta.

> py fibo.py 103900 102100 l  

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa.

Variáveis de ambiente
--------

Para abreviar os comandos e evitar repetições são definidas variáveis de ambiente no Windows:  
* %t% - Ticker do ativo  
* %d% - Data do gráfico  

Essas variáveis também podem ser definidas executando o arquivo setenv.bat

Aliases
--------

Os aliases de comandos são arquivos em lote como forma de viabilizar uma digitação mais rápida para execução dos comandos.  

Exemplos:  

h1 - py reader.py winq19h1.csv  

h1 ch - py reader.py winq19h1.csv   ch  

h1 vol 20 - py reader.py winq19h1.csv   vol 20  

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

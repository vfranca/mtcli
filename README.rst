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

> bars winq19 -p daily -c 20  

Exibe as últimas 20 barras do diário do winq19.

> bars winq19 -p daily -v ch -c 20  

Exibe o canal das últimas 20 barras do diário do winq19.

> bars winq19 -p daily -v c -c 20  

Exibe o preço de fechamento das últimas 20 barras do diário do winq19.

> bars winq19 -p daily -v h -c 20  

Exibe o preço máximo das últimas 20 barras do diário do winq19.

> bars winq19 -p daily -v l -c 20  

Exibe o preço mínimo das últimas 20 barras do diário do winq19.

> bars winq19 -p daily -v r -c 20  

Exibe o range das últimas 20 barras do diário do winq19.

> bars winq19 -p daily -v vol -c 20  

Exibe o volume das últimas 20 barras do diário do winq19.

> atr winq19 -p daily  

Exibe o ATR(14) do diário do winq19.

> atr winq19 -p daily -c 20  

Exibe o ATR(20) do diário do winq19.

> sma winq19 -p daily -c 20  

Exibe a média móvel aritmética de 20 períodos do diário do winq19.

> ema winq19 -p daily -c 20  

Exibe a média móvel exponencial de 20 períodos do diário do winq19.

> fib 103900 102100 h  

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta.

> fib 103900 102100 l  

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa.


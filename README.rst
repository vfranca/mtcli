=========
ChartCLI
=========

.. image:: https://img.shields.io/pypi/v/chartcli.svg
        :target: https://pypi.python.org/pypi/chartcli

.. image:: https://img.shields.io/travis/vfranca/chartcli.svg
        :target: https://travis-ci.org/vfranca/chartcli

.. image:: https://readthedocs.org/projects/chartcli/badge/?version=latest
        :target: https://chartcli.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Utilitário de linha de comando para leitura de gráficos do MetaTrader 5.

* Free software: MIT license
* Documentation: https://chartcli.readthedocs.io.

Pré-requisitos
--------

* MetaTrader 5
* EA GeraCSV.ex5
* Python


Instalação
--------

> git clone git@github.com:vfranca/charcli.git

Faz o clone do repositório.

> cd chartcli

> py -m venv venv

Cria um ambiente virtual do Python.

> venv\scripts\activate

Ativa o ambiente virtual do Python.


> pip install -r requirements_dev.txt

Instala as dependências de desenvolvimento.

> make test

Executa a suíte de testes.

> make build

Gera o build da aplicação.

> make install

Instala o pacote no ambiente virtual.


Execute o GeraCSV.ex5 com o MetaTrader 5 aberto com um gráfico e anexe esse expert advisor.


Comandos
--------

> cc bars winq19 -p daily -c 20  

Exibe as últimas 20 barras do diário do winq19.

> cc bars winq19 -p daily -v ch -c 20  

Exibe o canal das últimas 20 barras do diário do winq19.

> cc bars winq19 -p daily -v c -c 20  

Exibe o preço de fechamento das últimas 20 barras do diário do winq19.

> cc bars winq19 -p daily -v h -c 20  

Exibe o preço máximo das últimas 20 barras do diário do winq19.

> cc bars winq19 -p daily -v l -c 20  

Exibe o preço mínimo das últimas 20 barras do diário do winq19.

> cc bars winq19 -p daily -v r -c 20  

Exibe o range das últimas 20 barras do diário do winq19.

> cc bars winq19 -p daily -v vol -c 20  

Exibe o volume das últimas 20 barras do diário do winq19.

> cc atr winq19 -p daily  

Exibe o ATR(14) do diário do winq19.

> cc atr winq19 -p daily -c 20  

Exibe o ATR(20) do diário do winq19.

> cc sma winq19 -p daily -c 20  

Exibe a média móvel aritmética de 20 períodos do diário do winq19.

> cc ema winq19 -p daily -c 20  

Exibe a média móvel exponencial de 20 períodos do diário do winq19.

> cc fib 103900 102100 h  

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta.

> cc fib 103900 102100 l  

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa.


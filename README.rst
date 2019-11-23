=========
chartcli
=========

.. image:: https://img.shields.io/pypi/v/chartcli.svg
        :target: https://pypi.python.org/pypi/chartcli

.. image:: https://img.shields.io/travis/vfranca/chartcli.svg
        :target: https://travis-ci.org/vfranca/chartcli

.. image:: https://readthedocs.org/projects/chartcli/badge/?version=latest
        :target: https://chartcli.readthedocs.io/en/latest/?badge=latest
        :alt: Status da Documentação

Utilitário de linha de comando para leitura de gráficos do MetaTrader 5.

* Free software: MIT license
* Documentação: https://chartcli.readthedocs.io.

Pré-requisitos
---------------

* MetaTrader 5
* EA GeraCSV.ex5
* Python


Instalacao
-----------

Seguem abaixo instruções de instalação para desenvolvimento:


Faça o clone do repositório:  

> git clone git@github.com:vfranca/charcli.git  

Altere para o diretório do repositório:  

> cd chartcli  

Crie um ambiente virtual do Python:  

> python -m venv venv  

Ative o ambiente virtual do Python:  

> venv\scripts\activate  

Instale as dependências de desenvolvimento:  

> pip install -r requirements_dev.txt  


Uso do make  
--------------

Remove os artefatos de compilação:  

> make clean  

Executa os testes:  

> make test  

Compila o pacote para distribuição:  

> make build  

Faz o deploy no PyPI:  

> make deploy 

Faz a instalação do pacote:  

> make install  

Executa todas as tasks:  

> make  


Procedimento no MetaTrader 5
-----------------------------

Execute o GeraCSV.ex5 com o MetaTrader 5 aberto com um gráfico e anexe esse expert advisor. 

Uso  
---

Exibe as últimas 20 barras do diário do winq19:  

> cc bars winq19 -p daily -c 20  

Exibe o canal das últimas 20 barras do diário do winq19:  

> cc bars winq19 -p daily -v ch -c 20  

Exibe o preço de fechamento das últimas 20 barras do diário do winq19:  

> cc bars winq19 -p daily -v c -c 20  

Exibe o preço máximo das últimas 20 barras do diário do winq19:  

> cc bars winq19 -p daily -v h -c 20  

Exibe o preço mínimo das últimas 20 barras do diário do winq19  

> cc bars winq19 -p daily -v l -c 20  

Exibe o range das últimas 20 barras do diário do winq19:

> cc bars winq19 -p daily -v r -c 20  

Exibe o volume das últimas 20 barras do diário do winq19:  

> cc bars winq19 -p daily -v vol -c 20  

Exibe o ATR(14) do diário do winq19:  

> cc atr winq19 -p daily  

Exibe o ATR(20) do diário do winq19:  

> cc atr winq19 -p daily -c 20  

Exibe a média móvel aritmética de 20 períodos do diário do winq19:  

> cc sma winq19 -p daily -c 20  

Exibe a média móvel exponencial de 20 períodos do diário do winq19:  

> cc ema winq19 -p daily -c 20  

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta:  

> cc fib 103900 102100 h  

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa:  

> cc fib 103900 102100 l  


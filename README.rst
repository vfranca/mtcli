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


Faça o clone do repositório e alterne para seu diretório:

.. code-block:: console

    > git clone git@github.com:vfranca/charcli.git
    > cd chartcli

Crie um ambiente virtual do Python e ative-o:

.. code-block:: console

    > python -m venv venv
    > venv\scripts\activate

Instale as dependências de desenvolvimento:

.. code-block:: console

    > pip install -r requirements_dev.txt


Uso do make
--------------

Remove os artefatos de compilação:

.. code-block:: console

    > make clean

Executa a suíte de testes:

.. code-block:: console

    > make test

Compila o pacote para distribuição:

.. code-block:: console

    > make build

Faz o deploy no PyPI:

.. code-block:: console

    > make deploy

Faz a instalação do pacote:

.. code-block:: console

    > make install

Executa todas as tasks:

.. code-block:: console

    > make


Procedimento no MetaTrader 5
-----------------------------

Execute o GeraCSV.ex5 com o MetaTrader 5 aberto com um gráfico e anexe esse expert advisor.

Uso
---

Exibe as últimas 20 barras do diário do winq19:

.. code-block:: console

    > chart bars winq19 -p daily -c 20

Exibe o canal das últimas 20 barras do diário do winq19:

.. code-block:: console

    > chart bars winq19 -p daily -v ch -c 20

Exibe o preço de fechamento das últimas 20 barras do diário do winq19:

.. code-block:: console

    > chart bars winq19 -p daily -v c -c 20

Exibe o preço máximo das últimas 20 barras do diário do winq19:

.. code-block:: console

    > chart bars winq19 -p daily -v h -c 20

Exibe o preço mínimo das últimas 20 barras do diário do winq19

.. code-block:: console

    > chart bars winq19 -p daily -v l -c 20

Exibe o range das últimas 20 barras do diário do winq19:

.. code-block:: console

    > chart bars winq19 -p daily -v r -c 20

Exibe o volume das últimas 20 barras do diário do winq19:

.. code-block:: console

    > chart bars winq19 -p daily -v vol -c 20

Exibe o ATR(14) do diário do winq19:

.. code-block:: console

    > chart atr winq19 -p daily

Exibe o ATR(20) do diário do winq19:

.. code-block:: console

    > chart atr winq19 -p daily -c 20

Exibe a média móvel aritmética de 20 períodos do diário do winq19:

.. code-block:: console

    > chart sma winq19 -p daily -c 20

Exibe a média móvel exponencial de 20 períodos do diário do winq19:

.. code-block:: console

    > chart ema winq19 -p daily -c 20

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta:

.. code-block:: console

    > chart fib 103900 102100 h

Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa:

.. code-block:: console

    > chart fib 103900 102100 l


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

.. code-block:: console

    pip install https://github.com/vfranca/chartcli/archive/master.tar.gz

Procedimento no MetaTrader 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute o GeraCSV.ex5 com o MetaTrader 5 aberto com um gráfico e anexe esse expert advisor.

Uso
---

Para exibir as últimas 20 barras do diário do winq19:

.. code-block:: console

    mt bars winq19 -p daily -c 20

Para exibir o canal das últimas 20 barras do diário do winq19:

.. code-block:: console

    mt bars winq19 -p daily -v ch -c 20

Para exibir o preço de fechamento das últimas 20 barras do diário do winq19:

.. code-block:: console

    mt bars winq19 -p daily -v c -c 20

Para exibir o preço máximo das últimas 20 barras do diário do winq19:

.. code-block:: console

    mt bars winq19 -p daily -v h -c 20

Para exibir o preço mínimo das últimas 20 barras do diário do winq19

.. code-block:: console

    mt bars winq19 -p daily -v l -c 20

Para exibir o range das últimas 20 barras do diário do winq19:

.. code-block:: console

    mt bars winq19 -p daily -v r -c 20

Para exibir o volume das últimas 20 barras do diário do winq19:

.. code-block:: console

    mt bars winq19 -p daily -v vol -c 20

Para exibir o ATR(14) do diário do winq19:

.. code-block:: console

    mt atr winq19 -p daily

Para exibir o ATR(20) do diário do winq19:

.. code-block:: console

    mt atr winq19 -p daily -c 20

Para exibir a média móvel aritmética de 20 períodos do diário do winq19:

.. code-block:: console

    mt sma winq19 -p daily -c 20

Para exibir a média móvel exponencial de 20 períodos do diário do winq19:

.. code-block:: console

    mt ema winq19 -p daily -c 20

Para exibir as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta:

.. code-block:: console

    mt fib 103900 102100 h

Para exibir as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa:

.. code-block:: console

    mt fib 103900 102100 l

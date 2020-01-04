=========
mtcli
=========

.. image:: https://img.shields.io/pypi/v/mtcli.svg
        :target: https://pypi.python.org/pypi/mtcli

.. image:: https://readthedocs.org/projects/mtcli/badge/?version=latest
        :target: https://mtcli.readthedocs.io/en/latest/?badge=latest
        :alt: Status da Documentação


Utilitário de linha de comando para leitura de gráficos do MetaTrader 5.

* Free software: MIT license
* Documentação: https://mtcli.readthedocs.io.

Pré-requisitos
---------------

* `MetaTrader 5`_ - plataforma de trading.
* `GeraCSV.ex5`_ - robô executado no MetaTrader 5.

.. _MetaTrader 5: https://www.metatrader5.com/
.. _GeraCSV.ex5: https://drive.google.com/open?id=1jSSCRJnRg8Ag_sX_ZZAT4YJ2xnncSSAe

Instalação
-----------

.. code-block:: console

    pip install mtcli

Procedimento no MetaTrader 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Faça o download do `GeraCSV.ex5`_.

1. Execute o MetaTrader 5 e abra um gráfico.
2. Execute o GeraCSV.ex5.
3. Selecione a opção "anexar ao gráfico" no menu de contexto do GeraCSV.ex5.

.. _GeraCSV.ex5: https://drive.google.com/open?id=1jSSCRJnRg8Ag_sX_ZZAT4YJ2xnncSSAe


Arquivo .env
~~~~~~~~~~~~~


Crie um arquivo .env na pasta raiz do Windows com o conteúdo abaixo:

DIGITS="2"

CSV_PATH=[caminho_dos_arquivos_do_metatrader5]


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

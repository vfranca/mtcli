
.. highlight:: shell

=============
Contribuindo
=============

Contribuições são bem-vindas e são muito apreciadas! Cada trecho ajuda e sempre será dado crédito.

Você pode contribuir de várias maneiras:

Formas de Contribuição
-----------------------

Relatar Bugs
~~~~~~~~~~~~~

Relate bugs em https://github.com/vfranca/mtcli/issues.

Quando você estiver relatando um bug inclua:

* O nome e a versão do seu sistema operacional.
* Quaisquer detalhes sobre a configuração local que possam ser úteis na solução de problemas.
* Passos detalhados para reproduzir o bug.

Correção de Bugs
~~~~~~~~~~~~~~~~~

Procure nos issues do GitHub por bugs. Qualquer coisa marcada com "bug" e "help wanted"estará aberto a quem quiser implementá-lo.

Implementar Features
~~~~~~~~~~~~~~~~~~~~~

Procure nos issues do GitHub para obter features. Qualquer coisa marcada com "enhancement" e "help wanted" está aberta para quem quiser implementá-la.

Escrever Documentação
~~~~~~~~~~~~~~~~~~~~~~

O mtcli sempre poderá usar mais documentação, seja como parte dos
documentos oficiais de mtcli, em docstrings ou até na web em postagens de blog,
artigos e afins.

Enviar Feedback
~~~~~~~~~~~~~~~~

A melhor maneira de enviar feedback é registrar um issue em https://github.com/vfranca/mtcli/issues.

Se você estiver propondo uma feature:

* Explique em detalhes como funcionaria.
* Mantenha o escopo o mais estreito possível afim de facilitar a implementação.
* Lembre-se de que este é um projeto conduzido por voluntários e que as contribuições são bem-vindas.

Começando!
-----------

Pronto para contribuir? Veja como configurar o `mtcli` para desenvolvimento local.

1. Bifurque o repositório `mtcli` no GitHub.
2. Clone seu fork localmente::

.. code-block:: console

    git clone git@github.com:seu_usuario/mtcli.git

3. Instale sua cópia local em um virtualenv. Supondo que você tenha o virtualenvwrapper instalado, é assim que você configura seu fork para desenvolvimento local::

.. code-block:: console

    mkvirtualenv mtcli
    cd mtcli /
    poetry install

4. Crie um branch para desenvolvimento local:

.. code-block:: console

    git checkout -b nome-do-seu-bugfix-ou-feature

Agora você pode fazer suas alterações localmente.

5. Quando terminar de fazer as alterações, verifique se as alterações passam no flake8 e nos testes:

.. code-block:: console

    flake8 mtcli tests
    pytest

6. Comite suas alterações e envie seu branch para o GitHub:

.. code-block:: console

    git add .
    git commit -m "Descrição detalhada de suas alterações."
    git push origin nome-do-seu-bugfix-ou-feature

7. Envie um pull request pelo site do GitHub.

Diretrizes de Pull Request
---------------------------

Antes de enviar um pull request, verifique se ele atende a estas diretrizes:

1. O pull request deve incluir testes.
2. Se o pull request adicionar uma funcionalidade, os documentos deverão ser atualizados. Colocar sua nova funcionalidade em uma função com uma string e adicione-o para a lista em README.rst.

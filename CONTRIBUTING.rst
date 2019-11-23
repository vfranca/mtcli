.. highlight:: shell

=============
Contribuição
=============

Contribuições são bem-vindas e são muito apreciadas! Cada trecho ajuda e sempre será dado crédito.

Você pode contribuir de várias maneiras:

Formas de Contribuição
-----------------------

Relatar Bugs
~~~~~~~~~~~~~

Relate bugs em https://github.com/vfranca/chartcli/issues.

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

O chartcli sempre poderá usar mais documentação, seja como parte dos
documentos oficiais de chartcli, em docstrings ou até na web em postagens de blog,
artigos e afins.

Enviar Feedback
~~~~~~~~~~~~~~~~

A melhor maneira de enviar feedback é registrar um issue em https://github.com/vfranca/chartcli/issues.

Se você estiver propondo uma feature:

* Explique em detalhes como funcionaria.
* Mantenha o escopo o mais estreito possível afim de facilitar a implementação.
* Lembre-se de que este é um projeto conduzido por voluntários e que as contribuições são bem-vindas.

Começando!
-----------

Pronto para contribuir? Veja como configurar o `chartcli` para desenvolvimento local.

1. Bifurque o repositório `chartcli` no GitHub.
2. Clone seu fork localmente::

    $ git clone git@github.com:seu_usuario/chartcli.git

3. Instale sua cópia local em um virtualenv. Supondo que você tenha o virtualenvwrapper instalado, é assim que você configura seu fork para desenvolvimento local::

    > mkvirtualenv chartcli
    > cd chartcli /
    > python setup.py develop

4. Crie um branch para desenvolvimento local:

    > git checkout -b nome-do-seu-bugfix-ou-feature

   Agora você pode fazer suas alterações localmente.

5. Quando terminar de fazer as alterações, verifique se as alterações passam no flake8 e nos testes, incluindo o teste de outras versões do Python com o tox:

    > flake8 chartcli tests
    > python setup.py test ou py.test
    > tox

   Para obter flake8 e tox, basta instalá-los no seu virtualenv.

6. Comite suas alterações e envie seu branch para o GitHub:

    > git add .
    > git commit -m "Descrição detalhada de suas alterações."
    > git push origin nome-do-seu-bugfix-ou-feature

7. Envie um pull request pelo site do GitHub.

Diretrizes de Pull Request
---------------------------

Antes de enviar um pull request, verifique se ele atende a estas diretrizes:

1. O pull request deve incluir testes.
2. Se o pull request adicionar uma funcionalidade, os documentos deverão ser atualizados. Colocar sua nova funcionalidade em uma função com uma string e adicione-o para a lista em README.rst.
3. O pull request deve funcionar no Python 2.7, 3.4, 3.5 e 3.6 e no PyPy. Acesse https://travis-ci.org/vfranca/chartcli/pull_requests e verifique se os testes são aprovados para todas as versões suportadas do Python.

Dicas
-----

Para executar um subconjunto de testes:

    > python -m unittest tests.test_chartcli

Deploy
-------

Um lembrete para os mantenedores sobre como fazer o deploy.

Verifique se todas as suas alterações foram comitadas (incluindo uma entrada em HISTORY.rst).

Então execute::

> bumpversion patch # provavelmente: major / minor / patch
> git push
> git push --tags

O Travis fará o deploy no PyPI se os testes passarem.

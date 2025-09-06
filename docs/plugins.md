Plugins



O mtcli é extensível via plugins.



Criando um plugin



1\. Defina o ponto de entrada no pyproject.toml:



toml

\[project.entry-points."mtcli.plugins"]

meu\_plugin = "meu\_modulo:funcao"





2\. Implemente a função:



python

def funcao():

&nbsp;   print("Plugin executado.")





3\. Instale:



bash

pip install .





O mtcli detectará o plugin automaticamente.





---



📄 `docs/contribute.md`



markdown

Contribuindo



Contribuições são bem-vindas!



1\. Clone o repositório



bash

git clone https://github.com/vfranca/mtcli.git

cd mtcli





2\. Instale dependências de desenvolvimento



bash

pip install -e ".\[dev]"





3\. Testes



bash

pytest





4\. Estilo



\- Use black, ruff e mypy




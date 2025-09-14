# mtcli
  
*mtcli* é um aplicativo de linha de comando (CLI) acessível para leitura e análise de gráficos do MetaTrader 5, desenvolvido com foco em acessibilidade para usuários com deficiência visual.  
  
O projeto é modular e extensível por meio de plugins.
  
---
  
## Instalação
  
Você pode instalar o `mtcli` diretamente via *pip*:
  
```bash
pip install mtcli
```
  
Ou diretamente a partir do código-fonte:
  
```bash
git clone https://github.com/vfranca/mtcli.git
cd mtcli
pip install .
```
  
---
  
## Como usar
  
Após a instalação, o comando principal é:
  
```bash
mt
```
  
Você verá uma lista de comandos e plugins disponíveis.
  
Para executar um plugin específico, use:
  
```bash
mt nome-do-plugin [opções]
```
  
Exemplo com o plugin de média móvel:
  
```bash
mt mm --symbol WIN$N --periodo 14
```
  
---
  
## Documentação
  
A documentação completa está disponível em:
  
*https://vfranca.github.io/mtcli*
  
Inclui guias de uso, instalação de plugins, exemplos e estrutura do projeto.
  
---
  
## Como contribuir
  
Contribuições são bem-vindas!
  
Clonar o repositório
  
```bash
git clone https://github.com/vfranca/mtcli.git
cd mtcli
```
  
Instalar dependências para desenvolvimento
  
```bash
pip install -e ".[dev]"
```
Rodar os testes
  
```bash
pymake test
```
  
Estilo de código
  
- `black` para formatação
- `isort` para ordenação de imports
- `pydocstyle` para formatação de docstrings
- `ruff` e `mypy` para linting e verificação estática
  
---
  
## Criando plugins para o mtcli
  
Plugins permitem estender a funcionalidade do `mtcli`.
  
Estrutura básica de um plugin
  
```toml
pyproject.toml
[project.entry-points."mtcli.plugins"]
nome_do_plugin = "modulo.caminho:funcao_principal"
```
  
Exemplo
  
```toml
[project.entry-points."mtcli.plugins"]
volume_medio = "mtcli.plugins.volume_medio:vm"
```
  
No código Python:
  
```python

def vm():
    print("Plugin de volume médio executado.")
```
  
Como empacotar
  
Crie um projeto separado com sua lógica e registre o plugin no `pyproject.toml` ou `setup.py` como acima.
  
Depois, instale com:
  
```bash
pip install .
```
  
O `mtcli` reconhecerá o plugin automaticamente.
  
---
  
## Contato
  
Autor: *Valmir França da Silva*  
  
Email: vfranca3@gmail.com  
  
GitHub: [@vfranca](https://github.com/vfranca)
  
---
  
## Licença
  
Distribuído sob a licença GPL-3.0. Veja `LICENSE` para mais informações.

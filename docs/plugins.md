# Plugins
  
O mtcli é extensível via plugins.
  
## Criando um plugin
  
1. Defina o ponto de entrada no pyproject.toml:
  
```toml
[project.entry-points."mtcli.plugins"]
meu_plugin = "meu_modulo:funcao"
```
  
2. Implemente a função:
  
```python
@click.command()
def funcao():
    click.echo("Plugin executado.")
```
  
3. Instale:
  
```bash
pip install .
```
  
O mtcli detectará o plugin automaticamente.

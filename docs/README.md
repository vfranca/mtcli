# mtcli  
  
Aplicativo de Linha de comando para converter dados do MetaTrader 5 para formato TXT.  
O formato TXT é especialmente acessado por tecnologias assistivas para cegos.  

[mtcli no PyPI](https://pypi.python.org/pypi/mtcli)  
  
## Pré-requisitos  

1. Windows 10 ou 11 com conta Administrador ativada
2. Leitor de tela NVDA instalado
  
Para ativar a conta administrador execute o seguinte comando no terminal CMD:
```CMD
> net user Administrador /active:yes
```


## Instalação  

### MetaTrader 5 (mt5)

Faça o download do MetaTrader 5 e execute o instalador.  
[clique aqui para baixar o instalador MT5para Windows](https://www.metatrader5.com/pt)  

### Indicador mtcli
Faça o download do indicador mtcli e anexe a um gráfico  no MetaTrader 5.  
[Clique aqui para baixar o indicador mtcli](https://tinyurl.com/vfranca-mtcli)  

### Python
Instale o interpretador de comandos Python.  
Existem 3 opções para instalar o Python:  
1. Instalar pelo terminal Windows com o gerenciador de pacotes winget
2. Instalar pelo terminal Windows com o gerenciador de pacotes chocolatey
3. Instalar manualmente pelo instalador Python

#### winget
```CMD
> winget install --scope machine Python.Python.3.11
```

#### chocolatey
[Clique aqui para a página de instalação do chocolatey(https://chocolatey.org/install)  

#### instalador Python
[Clique aqui para baixar o instalador Python](https://www.python.org/downloads/windows)  

### mtcli:

Instale o mtcli pelo CMD do Windows.  
Execute o seguinte comando para instalar o mtcli:  

```CMD
> pip install mtcli
```


## Comandos  
  
```CMD
> mt bars <codigo_do_ativo> 
```
Exibe as últimas 40 barras diárias  do ativo.  
Digite mt bars --help para ver as opções.  

```CMD
> mt mm <codigo_do_ativo>
```
Exibe a média móvel simples das últimas 20 barras diárias do ativo.  
Digite mt mm --help para ver as opções.  


```CMD
> mt rm <codigo_do_ativo>
```
Exibe o range médio das últimas 14 barras diárias do ativo.  
Digite mt rm --help para ver as opções.  

```CMD
> mt ma <codigo_do_ativo>
```
Exibe as médias móveis das 20 barras diárias do código conforme exportadas pelo indicador MA_TXT.  
Digite mt ma --help para ver as opções.  
[Clique aqui para baixar o indicador MA_TXT](https://tinyurl.com/vfranca-ma-txt)  

Observação: é necessário anexar o indicador MA_TXT ao gráfico e configurar para exportar as 20 barras do diário.  


## Agradecimentos  
  
Ao @MaiconBaggio fornecedor do primeiro EA exportador das cotações para CSV.  
Ao Claudio Garini que transferiu a exportação das cotações para um indicador.  

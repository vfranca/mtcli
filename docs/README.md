# mtcli  
  
Aplicativo de Linha de comando para converter dados do MetaTrader 5 para formato TXT.  
O formato TXT é especialmente acessado por tecnologias assistivas para cegos.  

[mtcli no PyPI](https://pypi.python.org/pypi/mtcli)  
  
## Pré-requisitos  

* [MetaTrader 5](https://www.metatrader5.com/pt) - Plataforma de trading.  
* [Indicador mtcli](https://tinyurl.com/vfranca-mtcli) - programa MQL5 executado no MetaTrader 5.  
* [Python](https://www.python.org/downloads/windows) - Interpretador de comandos.  


## Instalação  

1. Instalar o MetaTrader 5.  
2. Executar o indicador mtcli.ex5 e anexar a um gráfico.  
3. Instalar o Python:

```cmd
winget install python
```

4. Instalar o mtcli:

```cmd
pip install mtcli
```



Opcionalmente baixe a pasta mtcli e descompacte os arquivos em C:\mtcli.  
[clique aqui para fazer o download](https://tinyurl.com/vfranca-mtcli-pasta)

## Comandos  
  
```cmd
mt bars <codigo_do_ativo> 
```
Exibe as últimas 40 barras diárias  do ativo.  
Digite mt bars --help para ver as opções.  

```cmd
mt mm <codigo_do_ativo>
```
Exibe a média móvel simples das últimas 20 barras diárias do ativo.  
Digite mt mm --help para ver as opções.  


```cmd
mt rm <codigo_do_ativo>
```
Exibe o range médio das últimas 14 barras diárias do ativo.  
Digite mt rm --help para ver as opções.  

```cmd
mt ma <codigo_do_ativo>
```
Exibe as médias móveis das 20 barras diárias do código conforme exportadas pelo indicador MA_TXT.  
Digite mt ma --help para ver as opções.  
[Clique aqui para baixar o indicador MA_TXT](https://tinyurl.com/vfranca-ma-txt)  
Observação: é necessário anexar o indicador MA_TXT ao gráfico e configurar para exportar as 20 barras do diário.  


## Agradecimentos  
  
Ao @MaiconBaggio fornecedor do primeiro EA exportador das cotações para CSV.  
Ao Claudio Garini que transferiu a exportação das cotações para um indicador.  

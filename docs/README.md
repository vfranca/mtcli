# mtcli  
  
Aplicativo de Linha de comando para converter dados do MetaTrader 5 para formato TXT.  
O formato TXT é especialmente acessado por tecnologias assistivas para cegos.  

[mtcli no PyPI](https://pypi.python.org/pypi/mtcli)  
  
## Pré-requisitos  

1. Windows 10 ou 11 com conta Administrador ativada.  
2. Leitor de tela NVDA instalado.  
  
Para ativar a conta administrador execute o seguinte comando no terminal CMD:  
```CMD
net user Administrador /active:yes
```
    
O mtcli não foi testado com outros leitores de tela além do NVDA.  
  

## Instalação  

### MetaTrader 5 (mt5)
Faça o download do MT5 e execute o instalador.  
[clique aqui para baixar o instalador MT5para Windows](https://www.metatrader5.com/pt)  
  
### Indicador mtcli
Faça o download do indicador mtcli e anexe a um gráfico  no MetaTrader 5.  
[Clique aqui para baixar o indicador mtcli](https://tinyurl.com/vfranca-mtcli)  
  
### Python
Instale o interpretador de comandos Python.  
Execute o comando abaixo no CMD do Windows:  
```CMD
winget install --scope machine Python.Python.3.11
```

[Clique aqui para ver outras formas de instalar o Python](python.md)


### mtcli

Execute o comando abaixo no CMD do Windows para instalar o mtcli:  
```CMD
pip install mtcli
```

## Comandos  
  
comando | descrição
:----- | :------
[mt bars](bars.md) | exibe barras do gráfico de candles
[mt mm](mm.md) | exibe a média móvel simples
[mt rm](rm.md) | exibe o range médio 
  
Digite a opção --help para exibir um resumo das opções.  

## abreviaturas  

[Clique aqui para ver uma lista de abreviaturas exibidas nas barras](abreviaturas.md)  

## Agradecimentos  
  
Ao @MaiconBaggio fornecedor do primeiro EA exportador das cotações para CSV.  
Ao Claudio Garini que transferiu a exportação das cotações para um indicador.  

# mtcli  
  
Aplicativo de Linha de comando para exibir gráficos do MetaTrader 5 em texto.  
O formato texto pode ser lido pelo leitor de telas NVDA.  
O mtcli é um produto para deficientes visuais e foi feito por um deficiente visual.  
  
## Pré-requisitos  

* Windows 10 ou 11 com conta Administrador ativada.  
* Leitor de tela NVDA.  
* Plataforma de negociação MetaTrader 5.  
* Python disponível no prompt de comando.  
    
Para ativar a conta administrador execute o seguinte comando no terminal CMD:  
```CMD
net user Administrador /active:yes
```
      
obs.: O mtcli não foi testado com outros leitores de tela além do NVDA.  
    

## Instalação  

### Indicador mtcli
Faça o download do indicador mtcli e anexe a um gráfico  no MetaTrader 5.  
[Clique aqui para baixar o indicador mtcli](https://tinyurl.com/vfranca-mtcli)  
  
### mtcli

Execute o comando abaixo no prompt do Windows para instalar o mtcli:  
```CMD
pip install mtcli
```
  
## Comandos  
  
| Comando | Descrição | Exemplo |
| :----- | :------ | :---- |
| [mt bars](bars.md) | Exibe o gráfico de candlestick. | mt bars IBOV |
| [mt mm](mm.md) | Calcula a média móvel simples. | mt mm IBOV |
| [mt rm](rm.md) | Calcula o tamanho médio das barras.| mt rm IBOV |
| mt conf | Gerencia configurações do mtcli | mt conf |
  
## abreviaturas  

[Clique aqui para ver uma lista de abreviaturas exibidas nas barras](abreviaturas.md)  

## Agradecimentos  
  
Ao @MaiconBaggio fornecedor do primeiro EA exportador das cotações para CSV.  
Ao Claudio Garini que transferiu a exportação das cotações para um indicador.  

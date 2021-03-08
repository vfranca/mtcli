# mtcli  
  
Ferramenta de linha de comando para leitura de gráficos do MetaTrader 5 para deficientes visuais.  
  
[PyPI](https://pypi.python.org/pypi/mtcli)  
[Documentação](https://vfranca.github.io/mtcli)  
  
------------

## Pré-requisitos  

* [MetaTrader5](https://www.metatrader5.com/pt) - Plataforma de trading.  
* [Python](https://www.python.org/downloads/windows) - Interpretador de comandos disponível no prompt de comando.  


## Instalação  

1. Instale o Python. Obtenha o instalador em https://www.python.org/downloads/windows. Durante a instalação marque a opção para ficar disponível no path do Windows.

2. No prompt de comando execute:
```
> pip install mtcli
```
3. Instale o MetaTrader 5. De preferência obtenha o instalador no site da sua corretora, caso contrário o instalador está disponível para download no site oficial do MetaTrader.  
4. Baixe no link abaixo o arquivo contendo os arquivos de trabalho do mtcli:  
https://drive.google.com/file/d/1olFEKJnnunBI1SDoW7QoMT9p6_yRQyhp/view?usp=sharing  
5. Descompacte o arquivo mtcli-workspace.zip e renomeie para um nome da sua preferência. Essa pasta deverá ser usada para executar os atalhos de comandos do mtcli. Além disso nela estarão os expert advisors que deverão ser anexados ao s gráficos do MetaTrader 5 e o arquivo .env com variáveis de configuração.  
6. Copie o arquivo .env para c:\.env e altere a variável CSV_PATH com o caminho da pasta de arquivos do MetaTrader 5.  
7. Anexe um dos  expert advisors ao gráfico do MetaTrader 5.  

Pronto! O mtcli está pronto para ser usado.  


## Comandos  
  
* [mt bars](https://github.com/vfranca/mtcli/blob/master/docs/chart.md) - Exibe as barras do gráfico.  
* [mt sma](https://github.com/vfranca/mtcli/blob/master/docs/chart.md) - Exibe a média móvel simples.  
* [mt ema](https://github.com/vfranca/mtcli/blob/master/docs/chart.md) - Exibe a média móvel exponencial.  
* [mt atr](https://github.com/vfranca/mtcli/blob/master/docs/chart.md) - Exibe average true range.  
* [mt fib](https://github.com/vfranca/mtcli/blob/master/docs/chart.md) - Exibe retrações e projeções de fibonacci.  

------------
  
  ## Agradecimentos  
  
Agradecimentos:  
Ao @MaiconBaggio desenvolvedor do PyMQL5 que faz uma comunicação com o MetaTrader5 e fornecedor do primeiro EA exportador das cotações.  
Ao Claudio Garini que transferiu a geração das cotações para um indicador.  


------------
  
## Licenciamento  

Este aplicativo está licenciado sob os termos da [GPL](../LICENSE).  

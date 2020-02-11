# mtcli  
  
Utilitário de linha de comando para leitura de gráficos do MetaTrader 5.  
  
[PyPI](https://pypi.python.org/pypi/mtcli)  
[Documentação](https://vfranca.github.io/mtcli)  
  
------------

## Pré-requisitos  

* [MetaTrader5](https://www.metatrader5.com/pt) - Plataforma de trading.  
* [GeraCSV.ex5](https://drive.google.com/file/d/1ijglZp05ZI29VzrMKTbKrQFO6CYPznyp/view?usp=sharing) - Expert advisor executando no MetaTrader5.  
* [Python](https://www.python.org/) - Interpretador de comandos disponível no prompt de comando.  


## Instalação

```
> pip install mtcli
```

### Arquivo .env  
  
Crie um arquivo .env na pasta raiz do Windows com o conteúdo abaixo:  
  
```
DIGITS="2"  
CSV_PATH=<caminho_dos_arquivos_do_metatrader5>  
```
  
  
### Arquivos mtcli  

Uma pasta compactada está disponível para download contendo os arquivos acima descritos para uso com o mtcli bem como instruções de como usá-los.  
Segue o link para download: https://drive.google.com/open?id=1olFEKJnnunBI1SDoW7QoMT9p6_yRQyhp  
  
  
## Comandos  
  
* [mt bars](chart.md) - Exibe as barras do gráfico.  
* [mt sma](chart.md) - Exibe a média móvel simples.  
* [mt ema](chart.md) - Exibe a média móvel exponencial.  
* [mt atr](chart.md) - Exibe average true range.  
* [mt fib](chart.md) - Exibe retrações e projeções de fibonacci.  

------------
  
  ## Agradecimentos  
  
Agradecimentos ao @MaiconBaggio desenvolvedor do PyMQL5 que faz uma comunicação com o MetaTrader5 e fornecedor do robô que faz a geração automática dos arquivos CSV.  

------------
  
## Licenciamento  

Este pacote é software livre e está licenciado sob os termos da [MIT](../LICENSE).  

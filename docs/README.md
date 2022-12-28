# mtcli  
  
Ferramenta de linha de comando para usuários cegos do MetaTrader 5.
  
[PyPI](https://pypi.python.org/pypi/mtcli)  
[Documentação](https://vfranca.github.io/mtcli)  
  
------------

## Pré-requisitos  

* [MetaTrader 5](https://www.metatrader5.com/pt) - Plataforma de trading.  
* [Indicador mtcli](https://drive.google.com/open?id=1yKYI873r_liiexugqisgc-OeVc_5IlGH&authuser=vfranca3%40gmail.com&usp=drive_fs) -programa MQL5 executado no MetaTrader 5.  
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



Opcionalmente baixe a pasta mtcli e descompacte os arquivos.
https://drive.google.com/file/d/1olFEKJnnunBI1SDoW7QoMT9p6_yRQyhp/view?usp=sharing  


## Comandos  
  
```cmd
mt bars <ticker_de_ativo> 
```
Exibe as barras do gráfico do ticker de ativo.

```cmd
mt mm <ticker_de_ativo>
```
Exibe a média móvel simples dos últimos 20 períodos do ticker de ativo.

```cmd
mt rm <ticker_de_ativo>
```
Exibe o range médio dos últimos 14 períodos do ticker_de_ativo.

------------
 
  ## Agradecimentos  
  
Ao @MaiconBaggio desenvolvedor do PyMQL5 que faz uma comunicação com o MetaTrader5 e fornecedor do primeiro EA exportador das cotações.  
Ao Claudio Garini que transferiu a geração das cotações para um indicador.  

# mtcli  
  
Utilitário de linha de comando para leitura de gráficos do MetaTrader 5.  
  
[PyPI](https://pypi.python.org/pypi/mtcli)  
[Documentação](https://vfranca.github.io/mtcli)  
  
## Pré-requisitos  
  
* [MetaTrader 5](https://www.metatrader5.com/) - plataforma de trading.  
* [GeraCSV.ex5](https://drive.google.com/open?id=1jSSCRJnRg8Ag_sX_ZZAT4YJ2xnncSSAe) - robô executado no MetaTrader 5.  
  
## Instalação
  
```
pip install mtcli
```
  
  
### Procedimento no MetaTrader 5  
  
1. Faça o download do GeraCSV.ex5.  
2. Execute o MetaTrader 5 e abra um gráfico.  
3. Execute o GeraCSV.ex5.  
4. Selecione a opção "anexar ao gráfico" no menu de contexto do GeraCSV.ex5.  
  
  
### Arquivo .env  
  
Crie um arquivo .env na pasta raiz do Windows com o conteúdo abaixo:  
  
```
DIGITS="2"  
CSV_PATH=<caminho_dos_arquivos_do_metatrader5>  
```
  
  
### Arquivos mtcli  

Uma pasta compactada está disponível para download contendo os arquivos acima descritos necessários para uso com o mtcli bem como instruções de como usá-los.  
Segue o link para download: https://drive.google.com/open?id=1olFEKJnnunBI1SDoW7QoMT9p6_yRQyhp  
  
  
## Exemplos de Uso  
  
```
Para exibir as últimas 20 barras do diário do winq19:  
mt bars winq19 -p daily -c 20  

Para exibir o canal das últimas 20 barras do diário do winq19:  
mt bars winq19 -p daily -v ch -c 20  

Para exibir o preço de fechamento das últimas 20 barras do diário do winq19:  
mt bars winq19 -p daily -v c -c 20  

Para exibir o preço máximo das últimas 20 barras do diário do winq19:  
mt bars winq19 -p daily -v h -c 20  

Para exibir o preço mínimo das últimas 20 barras do diário do winq19  
mt bars winq19 -p daily -v l -c 20

Para exibir o range das últimas 20 barras do diário do winq19:  
mt bars winq19 -p daily -v r -c 20  

Para exibir o volume das últimas 20 barras do diário do winq19:  
mt bars winq19 -p daily -v vol -c 20  

Para exibir o ATR(14) do diário do winq19:  
mt atr winq19 -p daily  

Para exibir o ATR(20) do diário do winq19:  
mt atr winq19 -p daily -c 20  

Para exibir a média móvel aritmética de 20 períodos do diário do winq19:  
mt sma winq19 -p daily -c 20  

Para exibir as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta:  
mt fib 103900 102100 h  

Para exibir as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa:  
mt fib 103900 102100 l  
```
  
Agradecimentos ao @MaiconBaggio, que além de outras importantes contribuições, gentilmente forneceu o expert advisor GeraCSV.ex5 do MetaTrader 5.  
  
Este pacote é software livre e está licensiado sob os termos da [MIT](../LICENSE).  

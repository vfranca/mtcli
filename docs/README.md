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

5. Descompacte o arquivo mtcli.zip. Uma pasta mtcli será criada. Essa pasta deverá ser usada para executar os atalhos de comandos do mtcli. Além disso nela estará o indicador mtcli.ex5 que deverá ser anexados ao gráfico do MetaTrader 5.
 
6. No MetaTrader 5 abra a pasta de dados (CTRL+SHIFT+D) e copie o camimnho da pasta mql5/Files para a área de transferência.

7. Configure o mtcli com o caminho copiado da pasta do MetaTrader 5:
```cmd
> cd mtcli
> conf CSV_PATH <cole-aqui-o-caminho-da-pasta>
```

8. Anexe o indicador mtcli.ex5 ao gráfico do MetaTrader 5.  

Pronto! O mtcli estará pronto para ser usado.  


## Comandos  
  
```cmd
mt bars <ativo> - Exibe as barras do gráfico do ativo especificado.
mt mm <ativo> - Exibe a média móvel simples dos últimos 20 períodos do ativo.
mt rm <ativo> - Exibe o range médio dos últimos 14 períodos do ativo.
```

------------
  
  ## Agradecimentos  
  
Ao @MaiconBaggio desenvolvedor do PyMQL5 que faz uma comunicação com o MetaTrader5 e fornecedor do primeiro EA exportador das cotações.  
Ao Claudio Garini que transferiu a geração das cotações para um indicador.  


------------
  
## Licenciamento  

Este aplicativo está licenciado sob os termos da [GPL](../LICENSE).  

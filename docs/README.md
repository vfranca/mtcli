# mtcli

Aplicativo CLI acessível para leitura de gráficos do MetaTrader 5 em formato de texto.  
  
O mtcli foi desenvolvido por uma pessoa com deficiência visual, com foco em acessibilidade e autonomia. Permite a leitura de cotações e indicadores via terminal, com formatação adequada para leitores de tela como o NVDA.
  
---
  
## Pré-requisitos

- Plataforma de negociação MetaTrader 5 instalada.
- Leitor de tela NVDA (não testado com outros leitores).
  
---
  
## Instalação
  
### Versão portable
  
[▶ Clique aqui para baixar o executável](https://bit.ly/mtcli)
  
Descompacte a pasta baixada e execute os comandos abaixo:
  
```cmd
cd mtcli
mt --version
```
  
A saída deverá ser algo como:  
mtcli 1.14.1  
  
A pasta também contem o indicador *Mtcli.ex5*: exporta as cotações em CSV, necessário para comandos como `mt bars`.
Deve ser adicionado ao gráfico no MetaTrader 5 para que o mtcli no modo CSV funcione corretamente.  
  
Para ajuda geral:  

```cmd
mt --help
```
  
Para ajuda específica:  
  
```cmd
mt <subcomando> --help
```
  
---
  
### Python (via PyPI)
  
Você também pode instalar o mtcli com pip:
  
```cmd
pip install mtcli
```
  
---
  
## Comandos
  
| Comando       | Descrição                                      | Exemplo       |
|---------------|------------------------------------------------|---------------|
| [mt bars](bars.md) | Exibe o gráfico de barras em texto             | mt bars IBOV |
| mt conf     | Gerencia configurações do mtcli                 | mt conf      |
  
---
  
## Comandos extras
  
  | Comando | Descrição | Exemplo |
| :----- | :------ | :---- |
| [mt mm](mm.md) | Calcula a média móvel (tipo sma ou ema). | mt mm WINQ25 --tipo ema |
| [mt rm](rm.md) | Calcula a média móvel do range.| mt rm WINQ25 |
| [mt vm](vm.md) | Calcula a média móvel do volume (tipo tick ou real). | mt vm WINQ25 --tipo real |
  
---
  
## Abreviaturas

[▶ Clique aqui para ver a lista de abreviaturas exibidas nas barras](abreviaturas.md)
  
---
  
## Acessibilidade
  
O mtcli é totalmente compatível com leitores de tela. A saída é formatada para facilitar a leitura por voz, permitindo análise técnica básica sem uso de interfaces gráficas.
  
---
  
## Agradecimentos
  
- Ao @MaiconBaggio, criador do primeiro EA exportador de cotações em CSV.
- Ao Claudio Garini, que transferiu a exportação para um indicador, melhorando a integração.
  

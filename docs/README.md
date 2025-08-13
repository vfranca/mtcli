# mtcli
  
Aplicativo CLI acessível para leitura de gráficos do MetaTrader 5 em formato de texto.  
  
Desenvolvido por uma pessoa com deficiência visual, o `mtcli` foca em acessibilidade e autonomia, permitindo a leitura de cotações e indicadores diretamente no terminal, com formatação compatível com leitores de tela como o NVDA.  
  
---
  
## Pré-requisitos
  
- Plataforma MetaTrader 5 instalada.
- Python disponível no prompt de comando.
- Leitor de tela NVDA (não testado com outros).
  
---
  
## Instalação
  
### Via PyPI (Python)
  
Se tiver o Python instalado:
  
```cmd
pip install mtcli
```
  
Para atualizar:
  
```cmd
pip install --upgrade mtcli
```
  
---
  
### Versão Executável (Portable)
  
[Download do executável](https://bit.ly/mtcli)
Após extrair a pasta:
  
```cmd
cd mtcli
mt --version
```
  
Saída esperada:
  

mtcli 1.14.1
  

Observação: A pasta contém o indicador Mtcli.ex5, que exporta cotações em CSV. Ele deve ser anexado ao gráfico no MetaTrader 5.
  
---
  
### Ajuda
  
Ajuda geral:
  
```cmd
mt --help
```
  
Ajuda por subcomando:
  
```cmd
mt <subcomando> --help
```
  
---
  
## Comandos principais
  
| Comando           | Descrição                                   | Exemplo            |
|-------------------|---------------------------------------------|--------------------|
| [mt bars](bars.md) | Exibe gráfico de barras em texto            | mt bars IBOV     |
| mt conf           | Gerencia configurações do mtcli           | mt conf          |
  
---
  
Comandos adicionais
  
| Comando          | Descrição                                     | Exemplo                       |
|------------------|-----------------------------------------------|-------------------------------|
| [mt mm](mm.md)   | Calcula a média móvel (SMA ou EMA)            | mt mm WINQ25 --tipo ema     |
| [mt rm](rm.md)   | Calcula a média do range                      | mt rm WINQ25                |
| mt vm            | Calcula a média do volume (tick ou real)      | mt vm WINQ25 --tipo real    |
  
---
  
## Abreviaturas
[Ver lista de abreviaturas](abreviaturas.md)
  
---

## Acessibilidade
  
- Totalmente compatível com leitores de tela.
- Saída textual otimizada para navegação por voz.
- Permite análise técnica sem interface gráfica.
  
---
  
## Agradecimentos

- @MaiconBaggio: Criador do primeiro EA exportador em CSV.
- Claudio Garini: Responsável pela implementação via indicador .ex5.
  

# `Subcomando `bars`
  
O subcomando `bars` é o coração do `mtcli`, responsável por exibir gráficos do MetaTrader 5 no terminal, de forma acessível.
  
## Sintaxe
  
```bash
mt bars [OPÇÕES]
```
  
Opções principais
  
- `symbol` ou `-a`: Símbolo do ativo (ex: WIN, PETR4)
- `--period` ou `-p`: Período dos candles (ex: M1, H1, D1)
- `--view` ou `-v`: Formato de saída (`f` full, `m` min, `r` range, etc.)
- `--inicio` e `--fim`: Intervalo de datas
- `--count` ou `-c`: Número de candles
  
Exemplo
  
```bash
mt bars WIN$N --period M5 --count 10 --view f
```
Exibe os 10 últimos candles do mini-índice em formato completo.
 
Subcomando `bars`



O subcomando `bars` é o coração do `mtcli`, responsável por exibir gráficos do MetaTrader 5 no terminal, de forma acessível.



Sintaxe



bash

mt bars \[OPÇÕES]





Opções principais



\- `--ativo` ou `-a`: Símbolo do ativo (ex: WIN, PETR4)

\- `–periodo` ou `-p`: Período dos candles (ex: M1, H1, D1)

\- `–formato` ou `-f`: Formato de saída (`text`, `table`, `json`, etc.)

\- `–inicio` e `–fim`: Intervalo de datas

\- `–count`: Número de candles



Exemplo



“`bash

mt bars -a WIN -p M5 --count 10 --formato table





Exibe os 10 últimos candles do mini-índice em formato de tabela.






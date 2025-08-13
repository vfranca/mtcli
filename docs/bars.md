# bars
  
Exibe o gráfico da plataforma de negociação.  
  
---
  
## Sintaxe

```cmd
mt bars [--period <período>] [--count <quantidade_de_períodos>] [--view <formato_de_exibição>] [--date <data_intraday>] [--volume <tipo_de_volume>] [--show date] [--numerator] <símbolo>
```
  
---
  
### Opções
  
`--period`, `-p`

Define o timeframe (período gráfico).

| Valor | Descrição   |
|-------|-------------|
| M1    | 1 minuto    |
| M2    | 2 minutos   |
| M3    | 3 minutos   |
| M4    | 4 minutos   |
| M5    | 5 minutos   |
| M6    | 6 minutos   |
| M10   | 10 minutos  |
| M12   | 12 minutos  |
| M15   | 15 minutos  |
| M20   | 20 minutos  |
| M30   | 30 minutos  |
| H1    | 1 hora      |
| H2    | 2 horas     |
| H3    | 3 horas     |
| H4    | 4 horas     |
| H6    | 6 horas     |
| H8    | 8 horas     |
| H12    | 12 horas     |
| D1    | Diário      |
| W1    | Semanal     |
| MN1   | Mensal      |
  
*Exemplo:*
  
```cmd
mt bars --period D1 WINQ25
```
  
---
  
`--count`, `-c`
  
Define a quantidade de períodos a serem exibidos.  
  
*Exemplo:*
  
```cmd
mt bars --count 100WINQ25
```
  
---
  
`--view`, `-v`
  
Define o formato de exibição dos períodos.
  
| Valor   | Descrição              |
|---------|------------------------|
| f | Completo               |
| m ou ch      (padrão) | Mínimo                 |
| r       | Ranges                 |
| v       | volumes                |
| c       | Fechamentos            |
| l       | Mínimas                |
| h       | Máximas                |
| a       | aberturas                |
| va     | Variação percentual    |
| oh      | OHLC                   |
  
*Exemplo:*
  
```cmd
mt bars --view m WINQ25
```
  
---
  
`--date`, `-d`
  
Filtra os períodos de um pregão específico  (no formato AAAA-MM-DD).
  
*Exemplo:*

```cmd
mt bars --date 2025-08-01 WINQ25
```
  
---
  
`--show-date`, `-sd`
  
Ativa a exibição da data/hora.  
  
*Exemplo:*
  
```cmd
mt bars --show-date WINQ25
```
  
---
  
`--volume`, `-vo`
  
Define o tipo de volume exibido na view volume (tick ou real).  
  
*Exemplo:*
  
```cmd
mt bars --view v --volume real WINQ25
```
  
---
  
`--numerator`, `-n`
  
Ativa a numeração dos períodos.    
  
*Exemplo:*
  
```cmd
mt bars --numerator WINQ25
```


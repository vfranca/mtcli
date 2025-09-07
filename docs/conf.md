# `Subcomando conf`
  
O subcomando conf gerencia as configurações do mtcli, como preferências de ativo, fonte de dados e opções de exibição.

  

## Sintaxe

  

```bash
mt conf [OPERAÇÃO] [OPÇÕES]

```

  

### Operações disponíveis

  

* --set: Define ou altera uma configuração
* --get: Exibe o valor atual de uma configuração
* --list: Lista todas as configurações atuais
* --reset: Restaura os valores padrão

  

## Exemplos

  

Definir dígitos da moeda do ativo
  
```bash
mt conf --set digitos 2
```
  
Ver ativo configurado
  
```bash
mt conf --get digitos
```
  
Listar tudo
  
```bash
mt conf --list
```
  
Restaurar padrão
  
```bash
mt conf --reset
```

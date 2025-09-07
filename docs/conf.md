\# `Subcomando conf`

&nbsp; 

O subcomando conf gerencia as configurações do mtcli, como preferências de ativo, período padrão e layout.

&nbsp; 

\## Sintaxe

&nbsp; 

```bash
mt conf \[OPERAÇÃO] \[OPÇÕES]

```

&nbsp; 

\### Operações disponíveis

&nbsp; 

* set: Define ou altera uma configuração
* get: Exibe o valor atual de uma configuração
* list: Lista todas as configurações atuais
* reset: Restaura os valores padrão

&nbsp; 

\## Exemplos

&nbsp; 

Definir ativo padrão

&nbsp; 

```bash
mt conf set ativo WIN$

```

&nbsp; 

Ver ativo configurado

&nbsp; 

```bash
mt conf get ativo

```

&nbsp; 

Listar tudo

&nbsp; 

```bash
mt conf list

```

&nbsp; 

Restaurar padrão

&nbsp; 

```bash
mt conf reset

```




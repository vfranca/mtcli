Subcomando conf

O subcomando conf gerencia as configurações do mtcli, como preferências de ativo, período padrão e layout.

Sintaxe

bash
mt conf [OPERAÇÃO] [OPÇÕES]


Operações disponíveis

- set: Define ou altera uma configuração
- get: Exibe o valor atual de uma configuração
- list: Lista todas as configurações atuais
- reset: Restaura os valores padrão

Exemplos

Definir ativo padrão

bash
mt conf set ativo WIN$


Ver ativo configurado

bash
mt conf get ativo


Listar tudo

bash
mt conf list


Restaurar padrão

bash
mt conf reset

# Registro do ciclo de TDD

## Comportamento escolhido

[Cobrar taxa inicial para distancia até 3 km.]

## Red

**Teste criado:** [test_taxa_ate_tres_quilometros]

**Motivo da falha:** [falta de retorno dos dados esperados]

## Green

**Implementacao realizada:** [implementação do 'return']

## Refactor

**Melhoria realizada:** [Remoção de uma variavel de taxa e implementação de 'return']

**Resultado final:** [Teste aprovado]


## Comportamento escolhido

[Acima de 3 km, devem ser acrescentados R$ 2,00 por quilômetro excedente.]

## Red

**Teste criado:** [test_taxa_acima_de_tres_quilometros]

**Motivo da falha:** [Calculo incorreto do valor excedente de taxa]

## Green

**Implementacao realizada:** [Cálculo correto do valor excedente]

## Refactor

**Melhoria realizada:** [Correção da lógica do cálculo do valor excedente]

**Resultado final:** [Teste aprovado]



## Comportamento escolhido

[Pedidos a partir de R$ 100,00 possuem entrega gratuita.]

## Red

**Teste criado:** [test_entrega_gratuita_para_pedidos_altos]

**Motivo da falha:** [Ordem dos 'if']

## Green

**Implementacao realizada:** [Troca dos condicionais if/elif]

## Refactor

**Melhoria realizada:** [Lógica da ordem condicional]

**Resultado final:** [Teste aprovado]
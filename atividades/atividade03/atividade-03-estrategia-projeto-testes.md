# Atividade 3: Estratégia e Projeto de Testes do LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** [Qualidade de Software 26/2 manhã]  
**Equipe:** [preencher, se aplicável]  
**Data:** [dd/mm/aaaa]

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| [Pedro Guterres Jaeger Livi] | [@PedroLivi2005] |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

[Expliquem brevemente o que a equipe pretende verificar com os testes.]

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| [Pedro] | [Fazer pedido] | [Todas as etapas para realizar um pedido] |

> Acrescentem ou removam linhas conforme o número de integrantes.

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| [Busca] | [Número de integrantes do grupo] |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | [Testes de Aceitação] | [Para verificar se os requisitos de negócio foram atendidos para entrega ao cliente.] |
| Tipos de teste | [Funcionais] | [Validar se o software faz o que deveria fazer.] |
| Perspectiva caixa-preta ou caixa-branca | [Caixa-Preta] | [Foco no ponto de vista do usuário final ou do cliente que consome o requisito.] |
| Técnicas de teste | [Transição de Estados] | [Testa mudanças de estado do sistema] |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | [Localhost da aplicação e hardware compatível com acesso a internet] |
| Responsáveis pelo planejamento | [Líder de QA] |
| Responsáveis pela especificação dos casos | [Analistas de Teste] |
| Responsáveis pela futura execução | [Desenvolvedores] |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | [O que precisa estar disponível antes do início dos testes? Código da funcionalidade finalizado e integrado para a execução no ambiente de teste.] |
| Saída | [O que precisa ser atendido para considerar os testes concluídos? Ter 100% dos casos de teste planejados executados e documentação de evidências de teste concluída.] |
| Suspensão | [Em quais situações os testes deverão ser interrompidos? Os testes podem ser interronpidos por diverços motivos, entre eles a indisponibilidade do ambiente de testes, falhas críticas que impeçam o acesso ao sistema, identificação de bug que inviabilize a continuidade dos fluxos dependentes.] |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

> Cada integrante deve analisar pelo menos um risco relacionado à funcionalidade escolhida. No trabalho individual, devem ser analisados dois riscos.

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | [Pedro] | [Fazer pedido] | [o pagamento do pedido não foi processado] | [cliente/restaurante pois um não recebe e o outro não vende o produto] | [Médio] | [Alto] | [Alta] | [As chances de acontecer não são altas, porém caso aconteça pode gerar impactos consideraveis aos clientes, levandos a desistir de realizar um pedido.] |

| R02 | [Pedro] | [Fazer pedido] | [o cliente realizar um pedido de um item que está fora de estoque ou indisponivel] | [o cliente pela quebra de expectativa ao pensar que o item desejado estivesse dísponivel.] | [Baixa] | [Baixo] | [Baixa] | [É algo com chances baixas de acontecer que pode ser resolvido com comunicação/organização.] |

> Acrescentem as linhas necessárias e mantenham identificadores únicos: R01, R02, R03 etc.

### 3.2 Aplicação das técnicas

> Cada integrante deve aplicar pelo menos uma técnica adequada à funcionalidade e ao risco analisado. A equipe deve utilizar, no conjunto da atividade, pelo menos duas técnicas diferentes.

#### Análise do integrante 1

**Integrante:** [Pedro]  
**Funcionalidade:** [Fazer pedido]  
**Risco relacionado:** [R01]  
**Técnica escolhida:** [transição de estados]

**Por que a técnica foi escolhida:**  
[Permite controlar e acompanhar o ciclo de vida de um processo dentro do sistema, assim, visualizando de forma clara a estrutura do progresso de cada item.]

**Aplicação da técnica:**  
[Apresentem as classes, limites, combinações ou transições identificadas. Utilizem uma tabela ou lista quando necessário.]

| Estado | Esvento |
|---|---|
| Criado | [Pedido submetido pelo cliente, aguardando resposta da cobrança.] |
| Confirmado | [Pagamento aprovado.] |
| Em preparação | [Restaurante aceitou e iniciou o preparo do pedido.] |
| Concluído | [Pedido entregue ao cliente.] |

**Casos derivados:** [CT01 e CT02]

#### Análise do integrante 2

**Integrante:** [nome]  
**Funcionalidade:** [preencher]  
**Risco relacionado:** [R02]  
**Técnica escolhida:** [preencher]

**Por que a técnica foi escolhida:**  
[preencher]

**Aplicação da técnica:**  
[preencher]

**Casos derivados:** [preencher]

> Repitam ou removam a seção de análise conforme o número de integrantes.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

> No trabalho individual, elabore três casos. No trabalho em equipe, cada integrante deve elaborar pelo menos dois casos relacionados à própria funcionalidade.

### CT01: [Título do caso]

**Integrante responsável:** [nome]  
**Funcionalidade:** [preencher]  
**Risco ou requisito relacionado:** [R01 ou descrição do requisito]  
**Técnica utilizada:** [preencher]

**Pré-condição:**  
[O que precisa existir ou estar preparado antes da execução.]

**Dados de entrada:**  
[Valores ou dados necessários. Caso não sejam necessários, registrem “Não se aplica”.]

**Passos:**

1. [Primeiro passo.]
2. [Segundo passo.]
3. [Terceiro passo.]

**Resultado esperado:**  
[Comportamento observável que indicará que o teste passou.]

---

### CT02: [Título do caso]

**Integrante responsável:** [nome]  
**Funcionalidade:** [preencher]  
**Risco ou requisito relacionado:** [preencher]  
**Técnica utilizada:** [preencher]

**Pré-condição:**  
[preencher]

**Dados de entrada:**  
[preencher]

**Passos:**

1. [Primeiro passo.]
2. [Segundo passo.]
3. [Terceiro passo.]

**Resultado esperado:**  
[preencher]

---

> Copiem o modelo acima e continuem a numeração para criar os demais casos: CT03, CT04, CT05 etc.

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| [nome] | [funcionalidade] | [R01 ou requisito] | [técnica] | [CT01 e CT02] |
| [nome] | [funcionalidade] | [R02 ou requisito] | [técnica] | [CT03 e CT04] |

> Acrescentem as linhas necessárias. Verifiquem se todos os riscos selecionados possuem casos de teste relacionados.

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[Informar a ferramenta ou registrar “não utilizada”.]

**Como foi utilizada:**  
[Descrever brevemente.]

**Uma sugestão que precisou ser alterada ou rejeitada:**  
[Descrever brevemente. Caso nenhuma sugestão tenha sido rejeitada, expliquem como as sugestões foram analisadas criticamente.]

**Como as respostas foram verificadas:**  
[Descrever brevemente.]
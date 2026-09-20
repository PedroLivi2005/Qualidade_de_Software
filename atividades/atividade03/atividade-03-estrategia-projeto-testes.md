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
| [Busca] | [Limitação no número de integrantes do grupo e escolha pessoal.] |

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

| Estado | Evento |
|---|---|
| Criado | [Pedido submetido pelo cliente, aguardando resposta da cobrança.] |
| Confirmado | [Pagamento aprovado.] |
| Em preparação | [Restaurante aceitou e iniciou o preparo do pedido.] |
| Concluído | [Pedido entregue ao cliente.] |
| Cancelado | [Pedido abortado pelo cliente ou pelo estabelecimento.] |

**Casos derivados:** [CT01: Verificar transição válida de Criado para Confirmado após retorno positivo de pagamento e 
CT02: Verificar bloqueio de cancelamento com pedido quando está em preparação.]

#### Análise do integrante 2

**Integrante:** [nome]  
**Funcionalidade:** [Fazer pedido]  
**Risco relacionado:** [R02]  
**Técnica escolhida:** [Tabela de decisão]

**Por que a técnica foi escolhida:**  
[A técnica de Tabela de Decisão foi escolhida porque a finalização do pedido depende da combinação lógica de múltiplas condições de entrada.]

**Aplicação da técnica:**  
| Condições | |
|---|---|
| C1 | [O item principal está disponível/em estoque?] |
| C2 | [Os acompanhamentos/itens secundários selecionados estão disponíveis?] |
| C3 | [O restaurante está aberto para pedidos no momento?] |

| Ações | |
|---|---|
| A1 | [Permitir avançar para o pagamento.] |
| A2 | [Bloquear finalização e alertar que o item principal está esgotado.] |
| A3 | [Bloquear finalização e alertar sobre item adicional/secundário indisponível.] |
| A4 | [Bloquear finalização informando que o restaurante está fechado.] |

**Casos derivados:** [CT03: Finalizar pedido com todos os itens e adicionais disponíveis e restaurante aberto.
CT04: Tentar submeter pedido contendo produto marcado como indisponível/esgotado no carrinho, verificando se o sistema bloqueia o avanço e exibe alerta visual ao cliente.]

> Repitam ou removam a seção de análise conforme o número de integrantes.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

> No trabalho individual, elabore três casos. No trabalho em equipe, cada integrante deve elaborar pelo menos dois casos relacionados à própria funcionalidade.

### CT01: [Transição de Estado de Pedido]

**Integrante responsável:** [Pedro]  
**Funcionalidade:** [Fazer pedido]  
**Risco ou requisito relacionado:** [R01]  
**Técnica utilizada:** [Transição de estados]

**Pré-condição:**  
[O cliente precisa selecionar um item para efetuar o pagamento]

**Dados de entrada:**  
[Valores ou dados necessários: Forma de pagamento, dados do pagante e valor em dinheiro exigido.]

**Passos:**

1. [Cliente preenche os dados e executa o pagamento.]
2. [Confirmação do pagamento.]
3. [Confirmação de pedido.]

**Resultado esperado:**  
[Comportamento observável que indicará que o teste passou: Mensagem de confirmação: Pedido Realizado!]
[ver evidência](evidencias/confirmação_pedido.jpg)

---

### CT02: [Bloqueio de Cancelamento]

**Integrante responsável:** [Pedro]  
**Funcionalidade:** [Fazer pedido]  
**Risco ou requisito relacionado:** [R01]  
**Técnica utilizada:** [transição de estados]

**Pré-condição:**  
[Um pedido deve ter sido feito e chegado ao estado de "Em preparação".]

**Dados de entrada:**  
[Todas as informações do pedido escolhido, pagamento, local de entrega.]

**Passos:**

1. [Verificar status do pedido.]
2. [Pedido Em preparação.]
3. [Sistema bloqueia o cancelamento.]

**Resultado esperado:**  
[Sistema deve recusar o cancelamento e exibir mensagem de bloqueio.]

---

### CT03: [Finalização de Pedido]

**Integrante responsável:** [Pedro]  
**Funcionalidade:** [Fazer pedido]  
**Risco ou requisito relacionado:** [R02]  
**Técnica utilizada:** [Tabela de decisão]

**Pré-condição:**  
[Um pedido deve ter sido selecionado.]

**Dados de entrada:**  
[Pedido e suas informações, incluindo possíveis itens adicionais/secundários.]

**Passos:**

1. [Cliente seleciona um pedido e se deseja adicionais.]
2. [Verificação de estoque de item principal/secundário e horário de funcionamento do estabelecimento.]
3. [Finalizar pedido com todos os itens e adicionais disponíveis e restaurante aberto.]

**Resultado esperado:**  
[Caso as verificações estejam ok, o pedido será feito.]

---

> Copiem o modelo acima e continuem a numeração para criar os demais casos: CT03, CT04, CT05 etc.

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| [Pedro] | [Fazer pedido] | [R01 e R02] | [transição de estados e Tabela de decisão] | [CT01, CT02, CT03 e CT04] |

> Acrescentem as linhas necessárias. Verifiquem se todos os riscos selecionados possuem casos de teste relacionados.

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[Gemini AI.]

**Como foi utilizada:**  
[Dúvidas sobre arquivo .md no GitHub, ortografia, dúvidas sobre o conseito de Casos de Teste, Risco e Técnicas.]

**Uma sugestão que precisou ser alterada ou rejeitada:**  
[Rejeição de justificativa de técnica escolhida, pois acreditei que eu mesmo devo eleaborar a justificativa e escreve-la da forma que achar melhor.]

**Como as respostas foram verificadas:**  
[As respostas foram verificadas com base o conteúdo visto em aula, no material disponível no blackboard e pesquisas na web.]
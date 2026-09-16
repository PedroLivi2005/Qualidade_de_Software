# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** [Qualidade de Software 26/2 manhã]  
**Data:** [dd/mm/aaaa]

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| [Pedro Guterres Jaeger Livi] | [@PedroLivi2005] |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | [O usuário pode salvar restaurantes como favorito] | [Cliente] | [Falta de praticidade para fazer um novo pedido no mesmo restaurante] |
| Explícita | [Aviso confirmação após a aprovação da compra] | [Cliente/Empresa] | [O comprador fica em dúvida se o pedido foi processado e pode sobrecarregar o suporte com chamados] |
| Implícita | [O sistema exibir de forma legível e clara as informações do produto, de forma que fica fácil de distinguir cada tipo de informação (ex. Título, descrição, preço)] | [Cliente] | [Página confusa e de difícil leitura] |
| Implícita | [Não permitir que o usuário envie o formulário de pagamento duas vezes por cliques repetidos no botão] | [Cliente / Setor Financeiro] | [Cobrança duplicada no cartão do cliente, estornos e retrabalho para o financeiro] |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

[Sim, um sistema pode implementar todas as funcionalidades explícitas e ainda assim ser considerado de baixa qualidade. Pois fazer o que foi pedido é apenas uma das dimensões da qualidade de software. Se o sistema atende aos requisitos declarados no papel, mas falha em entregar estabilidade, usabilidade, segurança ou desempenho aceitável, ele não cumpre o objetivo fundamental da qualidade.]

---

## 3. Tarefa 2: Exploração da aplicação

> Cada integrante deve explorar uma funcionalidade, realizando uma utilização esperada e uma utilização alternativa, inválida ou incompleta. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| [Pedro] | [Meus Pedidos] | [Uso esperado: Ver quais os pedidos que eu fiz. Uso alternativo: tentar verificar quando foi feito o pedido] | [Foi observado que os pedididos realizados de fato aparecem, porém não é possível ver a data que foram feitos] | [ver evidência](evidencias/evidencia1.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

> Cada integrante deve formular um requisito de qualidade relacionado à mesma funcionalidade explorada na Tarefa 2. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| [Pedro] | [Mostrar a data e hora de quando o pedido foi feito] | [Funcionalidade / Completude funcional (ISO/IEC 25010)] | [O usuário precisa saber quando realizou a compra para acompanhar prazos de entrega, rastreio e conferência financeira.] | [exibição de data/hora no formato padrão (DD/MM/AAAA HH:mm)] |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[Gemini IA.]

**Como foi utilizada:**  
[Dúvidas sobre arquivo .md no GitHub, ortografia, dúvidas sobre o conseito de qualidade e requisitos.]

**Como as respostas foram verificadas:**  
[As respostas foram verificadas com base o conteúdo visto em aula e no material disponível no blackboard e pesquisas na web.]
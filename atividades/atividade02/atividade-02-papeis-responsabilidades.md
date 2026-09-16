# Atividade 2: Organização da Qualidade no LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** [Qualidade de Software 26/2 manhã]  
**Equipe:** [preencher, se aplicável]  
**Data:** [dd/mm/aaaa]

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| [Pedro Guterres Jaeger Livi] | [@PedroLivi2005] |


**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| [preencher] | [preencher] |
| [preencher] | [preencher] |
| [preencher] | [preencher] |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

[Não, qualidade do LocalEats deve ser uma responsabilidade compartilhada por toda a equipe. A qualidade nasce na clareza dos requisitos definidos, passa pela usabilidade projetada pelo Design e pela escrita de código com testes unitários pelos Desenvolvedores. O profissional de QA atua estrategicamente como facilitador, garantindo padrões de processo e testes integrados, e não como um filtro isolado ao final do fluxo. Centralizar essa obrigação em uma única pessoa gera gargalos nas entregas e compromete a confiabilidade do serviço.]


---

## 3. Tarefa 2: Papéis e competências

> Cada integrante deve ser responsável pela análise de pelo menos um papel. Acrescentem ou removam linhas conforme a composição da equipe e os papéis escolhidos.

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| [Pedro] | [Desenvolvedor Backend] | [Garantir regras de negócio sólidas, criar testes automatizados, prevenir vulnerabilidades de segurança e otimizar queries no banco de dados.] | [Modelagem de dados, arquitetura de APIs REST, frameworks backend, testes automatizados e controle de versão.] | [Atenção aos detalhes, raciocínio lógico, foco em prevenção de falhas e boa comunicação técnica.] |

---

## 4. Tarefa 3: Matriz de responsabilidades

> Substituam “Papel 1”, “Papel 2”, “Papel 3” e “Papel 4” pelos papéis definidos pela equipe. Acrescentem ou removam colunas conforme necessário.

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | Desenvolvedor Backend | Papel 2 | Papel 3 | Papel 4 |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | C |  |  |  |
| Revisar requisitos | R |  |  |  |
| Implementar a funcionalidade | R |  |  |  |
| Revisar o código | R/A |  |  |  |
| Criar testes unitários | R/A |  |  |  |
| Planejar e executar testes do sistema | C |  |  |  |
| Registrar e acompanhar defeitos | C |  |  |  |
| Priorizar a correção dos defeitos | C |  |  |  |
| Aprovar a disponibilização da versão | C |  |  |  |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
[Conflito: "Priorização da correção dos defeitos" e "Aprovação da disponibilização da versão".
A centralização da aprovação final exclusivamente no Product Owner cria um gargalo operacional e um conflito de interesses entre metas de negócio e confiabilidade técnica:
O PO tende a priorizar entregas visíveis em detrimento de débitos técnicos e bugs críticos mapeados pelo time de QA.
Caso o QA seja reduzido a um mero papel consultivo, permite a liberação de versões com riscos severos (segurança, concorrência ou picos de carga) para cumprir prazos.]

**Consequência:**  
[Expliquem o possível impacto para o produto ou para a equipe: A ausência de uma aprovação técnica obrigatória compromete a qualidade final do produto e expõe a operação a incidentes em produção. Nesse exemplo pode haver impactos diversos para o Produto]

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| [Pipeline de CI/CD com Quality Gates automatizados] | [Falta de padronização, regressões frequentes em produção e dependência de testes manuais lentos a cada nova versão.] | [Dev Backend, Dev Frontend e Analista de QA] |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[Gemini IA.]

**Como foi utilizada:**  
[Dúvidas sobre arquivo .md no GitHub, ortografia, dúvidas sobre o conseito de qualidade, requisitos e matriz de responsabilidade.]

**Como as respostas foram verificadas:**  
[As respostas foram verificadas com base o conteúdo visto em aula, no material disponível no blackboard e pesquisas na web.]
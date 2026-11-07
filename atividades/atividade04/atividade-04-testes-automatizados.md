# Atividade 4: Testes Automatizados do LocalEats

> **Orientação:** substitua os textos entre colchetes pelas informações da equipe. Remova as orientações que não fizerem parte da entrega final.

---

## 1. Identificação

- **Turma:** [Qualidade de Software 26/2 manhã]
- **Modalidade:** [individual]
- **Repositório:** [https://github.com/PedroLivi2005/Qualidade_de_Software/tree/main]
- **Diretório da atividade:** [https://github.com/PedroLivi2005/Qualidade_de_Software/blob/main/atividades/atividade04/atividade-04-testes-automatizados.md]
- **Data da última execução:** [06/11/2026]

### Integrantes

1. [Pedro Guterres Jaeger Livi]

---

## 2. Integrantes e responsabilidades

Preencha uma linha para cada teste. Os testes unitários devem usar identificadores `TU01`, `TU02` e seguintes. Os testes funcionais devem usar `TF01`, `TF02` e seguintes.

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Pedro Guterres | Unitário | Cálculo de desconto para pedido válido ($\ge$ 100) | `tests/test_regras_localeats.py::test_calcula_desconto_pedido_acima_de_cem` |
| TU02 | Pedro Guterres | Unitário | Validação de exceção para valor negativo de pedido | `tests/test_regras_localeats.py::test_rejeita_valor_negativo_para_desconto` |
| TF01 | Pedro Guterres | Funcional | Verificação da página inicial do LocalEats | `tests/test_localeats.py::test_verifica_pagina_inicial_local_eats` |

> Adicione as linhas necessárias conforme a quantidade de integrantes.

### Quantidades mínimas

- **Individual:** uma função, dois testes unitários e um teste funcional.
- **Dupla:** duas funções, quatro testes unitários e dois testes funcionais.
- **Trio:** três funções, seis testes unitários e três testes funcionais.
- **Equipe de quatro:** quatro funções, oito testes unitários e quatro testes funcionais.

Cada teste funcional deve possuir pelo menos duas assertions. Integrantes da mesma equipe devem escolher regras e fluxos diferentes.

---

## 3. Testes unitários

Cada integrante deve escolher uma regra diferente, implementar a função correspondente e criar pelo menos dois testes unitários.

### Regras disponíveis

#### Regra 1: valor mínimo do pedido

```python
pedido_atingiu_valor_minimo(valor_pedido)
```

- Retorna `True` para pedidos de R$ 30,00 ou mais.
- Retorna `False` para pedidos abaixo de R$ 30,00.
- Gera `ValueError` para valores negativos.

#### Regra 2: desconto do pedido

```python
calcular_desconto(valor_pedido)
```

- Retorna `0` para pedidos abaixo de R$ 100,00.
- Retorna 10% do valor para pedidos de R$ 100,00 ou mais.
- Retorna apenas o valor do desconto.
- Gera `ValueError` para valores negativos.

#### Regra 3: quantidade de itens

```python
quantidade_itens_valida(quantidade)
```

- Retorna `True` para quantidades entre 1 e 10.
- Retorna `False` para zero ou quantidades acima de 10.
- Gera `ValueError` para quantidades negativas.

#### Regra 4: avaliação do restaurante

```python
avaliacao_valida(nota)
```

- Retorna `True` para notas entre 1 e 5.
- Retorna `False` para notas abaixo de 1 ou acima de 5.

### Registro das regras implementadas

#### Regra de [Pedro Guterres Jaeger Livi]

- **Regra escolhida:** [Calcular o desconto do pedido (`calcular_desconto`)]
- **Função implementada:** `[calcular_desconto]`
- **Arquivo da implementação:** [`src/regras_localeats.py`]
- **Testes criados:** [`test_calcula_desconto_pedido_acima_de_cem;` `test_nao_oferece_desconto_pedido_abaixo_de_cem;` `test_rejeita_valor_negativo_para_desconto`]
- **Comportamentos verificados:** [Verificou-se se pedidos de R$ 100,00 ou mais recebem 10% de desconto, se pedidos abaixo de R$ 100,00 não recebem desconto, e se a inserção de um valor negativo gera corretamente uma exceção do tipo ValueError.]

> Repita esta subseção para cada integrante.

---

## 4. Aplicação do TDD

Cada integrante deve registrar de forma breve o desenvolvimento orientado a testes da própria regra.

### TDD de [Pedro Guterres Jaeger Livi]

- **Regra escolhida:** [Regra escolhida: Calcular o desconto do pedido (calcular_desconto)]
- **Primeiro teste escrito:** `[test_calcula_desconto_pedido_acima_de_cem]`
- **Por que o teste falhou inicialmente:** [O teste falhou porque o módulo src/regras_localeats.py e a função calcular_desconto ainda não haviam sido implementados no projeto (fase Red do TDD).]
- **Implementação mínima realizada:** [Foi criado o módulo de regras e a estrutura inicial da função calcular_desconto retornando o percentual de desconto para valores maiores ou iguais a R$ 100,00 e zero para valores inferiores (fase Green).]
- **Segundo teste escrito:** `[test_rejeita_valor_negativo_para_desconto]`
- **Melhoria ou refatoração realizada:** [Foi adicionada a validação de segurança para lançar uma exceção do tipo ValueError caso o valor do pedido seja menor que zero, garantindo maior robustez e conformidade com os requisitos da regra.]

> Repita esta subseção para cada integrante.

---

## 5. Testes funcionais com Playwright

Cada integrante deve automatizar um fluxo diferente pela interface do LocalEats.

**Sistema:** https://local-eats-unisenac.vercel.app/

### Fluxos possíveis

- verificar a apresentação da página inicial;
- pesquisar um restaurante;
- selecionar uma categoria;
- verificar restaurantes de uma categoria;
- verificar informações apresentadas em um restaurante;
- criar uma conta ou entrar no sistema, se o fluxo estiver disponível;
- favoritar ou desfavoritar um restaurante;
- consultar pedidos;
- automatizar outro comportamento estável identificado durante a exploração.

### Requisitos de cada teste funcional

- acessar o LocalEats;
- realizar pelo menos uma interação pela interface;
- utilizar locators do Playwright;
- possuir pelo menos duas assertions;
- verificar resultados observáveis;
- não utilizar `time.sleep`;
- executar com pytest;
- identificar o integrante responsável no código.

### Teste funcional de [nome do integrante]

- **ID:** `TF01`
- **Fluxo automatizado:** [Realizar o login na plataforma do LocalEats utilizando um e-mail e senha cadastrados.]
- **Interação realizada:** [Preenchimento do campo de e-mail, preenchimento do campo de senha e clique no botão de entrar (Entrar).]
- **Primeira assertion:** [Verificar se o URL da página mudou para a área logada/dashboard do sistema ou se a página inicial logada foi alcançada com sucesso.]
- **Segunda assertion:** [Verificar se algum elemento visível exclusivo da sessão autenticada (como o botão de sair ou o nome/perfil do usuário) é apresentado na interface.]
- **Arquivo e função:** `tests/test_localeats.py::test_entrar_no_sistema`
- **Resultado final:** [aprovado]

> Repita esta subseção para cada integrante.

---

## 6. Resultado da execução

Execute todos os testes no PowerShell:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

Depois, registre o resultado:

- **Quantidade total de testes:** [4]
- **Testes aprovados:** [test_entrar_no_sistema; test_calcula_desconto_pedido_acima_de_cem; test_nao_oferece_desconto_pedido_abaixo_de_cem; test_rejeita_valor_negativo_para_desconto]
- **Testes reprovados:** [0]
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** [Todos os testes foram aprovados]

---

## 7. Explicações individuais

Cada integrante deve escolher um teste de sua responsabilidade e demonstrar compreensão sobre o código entregue.

### Explicação do teste de [Pedro Guterres Jaeger Livi]

- **Teste escolhido:** `[test_rejeita_valor_negativo_para_desconto]`
- **Comportamento verificado:** [Valida se a função calcular_desconto é capaz de identificar e rejeitar valores de pedidos inválidos (negativos), garantindo a consistência das regras de negócio e a segurança contra entradas corrompidas.]
- **Dados ou estado inicial:** [O valor fornecido à função é um número decimal negativo (-10.0).]
- **Resultado esperado:** [A função deve lançar obrigatoriamente uma exceção do tipo ValueError, capturada de forma controlada pelo contexto do pytest.raises.]
- **O que faria o teste falhar:** [O teste falharia se a função permitisse o processamento de um valor negativo sem lançar a exceção esperada, ou se lançasse uma exceção de um tipo diferente (como TypeError ou KeyError).]

> Repita esta subseção para cada integrante.

---

## 8. Uso de inteligência artificial

O uso de inteligência artificial é permitido como apoio, mas todo o conteúdo e código devem ser revisados, executados e compreendidos pela equipe.

- **Ferramenta utilizada:** [informar ou escrever “Não utilizada”]
- **Como a ferramenta foi utilizada:** [Responder dúvidas sobre pytest (instalação/execução), .venv, comando relatorio.txt, arquivo .md, explicar erros de execução dos testes]
- **Uma sugestão que precisou ser alterada ou rejeitada:** [Erro no teste test_entrar_no_sistema]
- **Motivo da alteração ou rejeição:** [Playwright encontrou dois botões com o nome "Entrar" na página de login: um botão de alternância de aba (#showLoginBtn) e o botão de envio do formulário (type="submit")]
- **Como o código sugerido foi verificado:** [Execução local através do comando `python -m pytest -v` validando o sucesso de todos os testes unitários e funcionais.]

---

## 9. Diferenciais opcionais

Marque somente os diferenciais realmente implementados e inclua ao lado os respectivos links.

- [ ] Terceiro teste unitário para caso de borda.
- [ ] Uso de `pytest.raises` para verificar exceção.
- [ ] Parametrização com `pytest.mark.parametrize`.
- [ ] Cenário BDD em Gherkin.
- [ ] Automação com `pytest-bdd`.
- [ ] Organização com Page Object Model.
- [ ] Segundo teste funcional pelo mesmo integrante.
- [ ] Execução em mais de um navegador.
- [ ] Screenshot, vídeo ou trace do Playwright.
- [ ] Registro de uma falha encontrada e corrigida.

### Descrição dos diferenciais

[Descreva os diferenciais implementados e informe os arquivos correspondentes. Remova esta seção caso nenhum diferencial tenha sido desenvolvido.]

---

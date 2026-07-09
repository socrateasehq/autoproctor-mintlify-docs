---
title: "Bancos de Perguntas"
description: "Crie grandes conjuntos de perguntas e ofereça subconjuntos aleatórios aos candidatos usando os Bancos de Perguntas."
---

Os Bancos de Perguntas permitem que você crie grandes conjuntos de perguntas e ofereça um subconjunto aleatório para cada candidato. Cada candidato recebe uma combinação diferente de perguntas, reduzindo a chance de fraude enquanto mantém uma estrutura de avaliação consistente.

{% hint style="info" %}
Os Bancos de Perguntas são um recurso do plano **Elite**. Você precisa de uma assinatura Elite para criar e usar Bancos de Perguntas e Questionários de Bancos de Perguntas. Consulte [Recursos Elite](pricing-account/plans-credits/elite-features.md) para detalhes.
{% endhint %}

## O Que é um Banco de Perguntas?

Um Banco de Perguntas (BP) é uma coleção de perguntas organizadas por disciplina ou tema. Cada pergunta no banco pode ter um valor de pontos e um nível de dificuldade diferente. Quando os candidatos fazem um teste, eles recebem um subconjunto selecionado aleatoriamente do banco em vez do conjunto completo de perguntas.


![Visão geral do Banco de Perguntas mostrando uma lista de perguntas organizadas por tema e dificuldade](../../images/socratease/question-bank-overview.png)

### Exemplo: Testes de Física e Química

Imagine que você tem dois Bancos de Perguntas:
- **Banco de Perguntas de Física** — 100 perguntas em vários níveis de dificuldade
- **Banco de Perguntas de Química** — 100 perguntas em vários níveis de dificuldade

Você pode criar diferentes questionários que extraiam desses bancos com diferentes ponderações:

| Questionário | Perguntas de Física | Perguntas de Química | Total |
|---|---|---|---|
| Questionário de Física | 40 perguntas (2 pontos cada) | 10 perguntas (1 ponto cada) | 50 perguntas |
| Questionário de Química | 10 perguntas (1 ponto cada) | 40 perguntas (2 pontos cada) | 50 perguntas |

Cada candidato recebe um subconjunto aleatório diferente de perguntas dos respectivos bancos, mas a estrutura geral (número de perguntas, pontos, distribuição de dificuldade) permanece consistente entre todos os candidatos.

## Questionários de Bancos de Perguntas (QBP)

{% hint style="warning" %}
Os candidatos não podem realizar um Banco de Perguntas diretamente. Você deve criar um Questionário de Banco de Perguntas e adicioná-lo a um teste do AutoProctor para que os candidatos o realizem.
{% endhint %}

![Visão geral dos Questionários de Banco de Perguntas mostrando QBPs criados com contagem de respostas](../../images/socratease/question-bank-quiz-overview.png)
*Visão geral dos Questionários de Banco de Perguntas criados*

Um Questionário de Banco de Perguntas especifica:
- De quais Bancos de Perguntas extrair as perguntas
- Quantas perguntas incluir de cada banco
- Os níveis de dificuldade a incluir
- Os valores de pontos para cada nível de dificuldade

Você pode combinar múltiplos Bancos de Perguntas em um único QBP, ou usar um banco para fornecer perguntas em diferentes níveis de dificuldade.

## Como Criar um Questionário de Banco de Perguntas

{% embed url="../../videos/socratease/add-qbq.mp4" %}
Como criar um Questionário de Banco de Perguntas
{% endembed %}

{% stepper %}
{% step %}
### Crie um Banco de Perguntas
Navegue até a seção de Bancos de Perguntas no AutoProctor e crie um novo Banco de Perguntas. Adicione suas perguntas, atribuindo valores de pontos e níveis de dificuldade a cada uma.


{% endstep %}
{% step %}
### Crie um Questionário de Banco de Perguntas
Crie um novo Questionário de Banco de Perguntas (QBP). Selecione de quais Bancos de Perguntas extrair, quantas perguntas incluir e quais níveis de dificuldade usar.


{% endstep %}
{% step %}
### Adicione a um Teste do AutoProctor
Adicione o QBP a um teste do AutoProctor. Compartilhe o link do teste com seus candidatos.


{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [Importação em Massa a partir de Excel](socratease/create-questions/bulk-import-from-excel.md) — Importe perguntas em massa para popular seus Bancos de Perguntas
- [Tipos de Perguntas](socratease/create-questions/question-types.md) — Formatos de perguntas disponíveis para uso nos Bancos de Perguntas
- [Uso de Etiquetas](socratease/settings/using-tags.md) — Organize perguntas com etiquetas para filtragem e agrupamento
- [Configurações do Questionário](socratease/settings/quiz-settings.md) — Configure o comportamento do questionário
- [Recursos Elite](pricing-account/plans-credits/elite-features.md) — Conheça as capacidades do plano Elite

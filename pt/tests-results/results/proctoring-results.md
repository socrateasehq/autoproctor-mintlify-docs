---
title: "Onde Posso Ver os Resultados de Supervisão?"
description: "Acesse e revise os resultados de supervisão dos seus testes no AutoProctor, incluindo Trust Scores, detalhes de violações e relatórios por candidato."
---

Após os candidatos concluírem um teste supervisionado, o AutoProctor compila os dados de monitoramento em um relatório de supervisão. Este guia explica como acessar e interpretar esses resultados.

{% hint style="info" %}
Os resultados de supervisão só são gerados quando a supervisão está ativada nas [configurações do teste](tests-results/create/proctoring-settings.md). Se você configurou o teste apenas com temporizador, não há dados de supervisão disponíveis.
{% endhint %}

## Visualizando os Resultados de Supervisão

{% stepper %}
{% step %}
### Abra a página de resultados
Navegue até o seu [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/) e clique no botão **Results** do teste que deseja revisar.

![Botão de resultados destacado no painel do AutoProctor](../../images/results/results-button-dashboard.png)
*Botão de resultados no painel do AutoProctor*
{% endstep %}
{% step %}
### Revise a tabela de resultados
A página de resultados exibe uma tabela listando todas as submissões. Cada linha inclui:

- Nome e endereço de e-mail do candidato
- Hora de início e término do teste
- Trust Score (indicando a integridade da supervisão)
- Pontuação do questionário (apenas para Questionários Socratease)

![Tabela de resultados mostrando submissões dos candidatos com Trust Scores](../../images/results/results-table.png)
*Tabela de resultados*
{% endstep %}
{% step %}
### Veja o resumo de supervisão
Clique no **Trust Score** de um candidato para abrir o resumo detalhado de supervisão. Esta página lista todas as violações detectadas durante o teste, incluindo capturas de tela, timestamps e evidências.

![Página de resumo de supervisão mostrando violações detectadas e evidências](../../images/results/proctoring-summary.png)
*Página de resumo de supervisão*
{% endstep %}
{% endstepper %}

## O Que o Resumo de Supervisão Mostra

O resumo de supervisão de cada candidato inclui:

| Dado | Descrição |
|---|---|
| **Trust Score** | Classificação geral de integridade baseada nas violações detectadas |
| **Lista de violações** | Cada tipo de violação com timestamp e evidência |
| **Capturas de tela** | Fotos aleatórias capturadas durante a sessão do teste |
| **Gravações** | Gravações de tela e webcam (se ativadas na [supervisão avançada](tests-results/create/enhanced-proctoring.md)) |
| **Linha do tempo da sessão** | Quando o candidato iniciou, pausou ou enviou o teste |

## Recursos Relacionados

- [Onde Posso Ver os Resultados do Meu Teste?](tests-results/results/how-to-see-results.md) -- Visão geral dos resultados do teste vs. resultados de supervisão
- [Trust Score Explicado](understanding/how-proctoring-works/trust-score.md) -- Como os Trust Scores são calculados
- [O Que É Monitorado](understanding/how-proctoring-works/what-gets-tracked.md) -- O que o AutoProctor supervisiona durante um teste supervisionado
- [Exportar para Excel](tests-results/results/export-to-excel.md) -- Baixe os resultados de supervisão como planilha
- [Testes Não Enviados](tests-results/results/unsubmitted-tests.md) -- Veja detalhes de testes iniciados mas não enviados

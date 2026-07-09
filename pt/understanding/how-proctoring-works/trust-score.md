---
title: "Trust Score"
description: "Entenda como o Trust Score do AutoProctor funciona, como é calculado e o que constitui uma boa pontuação."
---

O AutoProctor atribui um Trust Score (0–100%) a cada relatório de supervisão. A pontuação fornece um resumo rápido da probabilidade de o candidato ter mantido a integridade durante o teste, para que você possa concentrar seu tempo de revisão nas tentativas que mais necessitam.

![Exibição do Trust Score mostrando uma porcentagem no topo de um relatório de supervisão do AutoProctor](images/getting-started/trustscore.png)

Quanto mais baixo o Trust Score, mais comportamento suspeito o AutoProctor detectou durante o teste.

{% hint style="warning" %}
Sempre revise as evidências de apoio antes de tirar conclusões. **Não** se baseie apenas no Trust Score — revise as fotos, capturas de tela e gravações de áudio das infrações para determinar se houve conduta indevida.
{% endhint %}

## Como o Trust Score é Calculado

O AutoProctor monitora os candidatos em tempo real por meio de múltiplos canais (dependendo das suas [configurações de supervisão](tests-results/create/proctoring-settings.md)):

- Câmera
- Microfone
- Atividade da tela

O algoritmo avalia as infrações com base em três fatores:

| Fator | Como Afeta a Pontuação |
|---|---|
| **Tipo de infração** | Diferentes infrações têm pesos diferentes. A troca de aba tem um impacto maior na pontuação do que a detecção de ruído. |
| **Frequência das infrações** | Mais incidentes resultam em uma pontuação mais baixa. |
| **Duração das infrações** | Infrações prolongadas reduzem a pontuação de forma mais significativa do que as breves. |


## O Que é um Bom Trust Score?

Como referência geral, revise as evidências de qualquer candidato com um Trust Score **inferior a 85%**. Esse limite é destinado à revisão, não como prova de conduta indevida.

{% hint style="info" %}
Fatores ambientais podem afetar significativamente a pontuação. Por exemplo, um candidato em um ambiente ruidoso perto do trânsito poderia receber um Trust Score de 0% mesmo quando nenhuma trapaça ocorreu. O microfone capta o ruído ambiente e o sistema nem sempre consegue distinguir entre fala humana e som de fundo. Sempre verifique as evidências antes de tomar uma decisão.
{% endhint %}

## Como Revisar um Trust Score

{% stepper %}
{% step %}
### Abra os resultados do teste
Acesse seu [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/), selecione um teste e clique em **Results**. Você verá uma lista de todos os candidatos com seus Trust Scores.
{% endstep %}
{% step %}
### Identifique os candidatos para revisão
Ordene por Trust Score e concentre-se nos candidatos com pontuação **inferior a 85%**. Essas tentativas são as mais propensas a conter infrações que merecem revisão.

{% embed url="videos/getting-started/trustscore-column.mp4" %}
Lista de resultados mostrando a coluna de Trust Score
{% endembed %}
{% endstep %}
{% step %}
### Revise as evidências de infrações
Clique em **Ver Relatório** na linha de um candidato para ver o detalhamento completo: fotos sinalizadas, capturas de tela, clipes de áudio e uma linha do tempo das infrações detectadas.


{% endstep %}
{% step %}
### Tome sua decisão
Use as evidências para decidir se as infrações indicam conduta indevida real ou são falsos positivos causados por fatores ambientais.
{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [O Que é Monitorado](understanding/how-proctoring-works/what-gets-tracked.md) — Todas as capacidades de monitoramento disponíveis
- [Resultados de Supervisão](tests-results/results/proctoring-results.md) — Como ver as evidências de infrações e os relatórios
- [Envios Individuais](tests-results/results/individual-submissions.md) — Revisando o relatório de um candidato em detalhes
- [Nenhum Rosto ou Múltiplos Rostos Detectados](tests-results/issues/no-face-or-multiple-faces.md) — Por que a detecção facial pode gerar falsos positivos
- [Infração Falsa de Troca de Aplicativo](tests-results/issues/false-app-switch.md) — Entendendo as sinalizações de infrações falsas
- [Boas Práticas para Criadores de Testes](understanding/getting-started/best-practices-for-teachers.md) — Dicas para aplicar testes supervisionados de forma eficaz

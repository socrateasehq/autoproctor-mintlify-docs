---
title: "Configurações de Supervisão"
description: "Configure detecção de troca de aba, monitoramento por câmera, gravação de microfone, modo de tela cheia obrigatório e outras opções de supervisão."
---

As Configurações de Supervisão controlam o que o AutoProctor monitora durante um teste — desde a troca de aba e detecção por câmera até o modo de tela cheia obrigatório e captura aleatória de fotos. Essas configurações determinam o quão rigorosamente os candidatos são supervisionados.


![Painel de configurações de supervisão](images/creating-tests/proctoring-settings.png)
*Painel de configurações de supervisão*

{% hint style="info" %}
Para ativar a supervisão, você deve marcar a caixa **Enable Proctor** na seção de Configurações Principais. Se a supervisão estiver desativada, nenhuma dessas configurações será aplicada.
{% endhint %}

## Opções Básicas de Supervisão

| Configuração | O Que Faz |
|---|---|
| **Tab Switching** | Detecta quando um candidato muda para uma aba ou aplicativo diferente no navegador. Captura uma captura de tela da aba para a qual ele mudou. |
| **Detect Multiple Monitors** | Detecta se um candidato conectou monitores externos ao computador. |
| **Camera** | Detecta se nenhum rosto é visível na câmera, ou se múltiplos rostos são visíveis. Captura fotos como evidência. |
| **Microphone** | Monitora o ambiente sonoro e grava áudio quando ruído é detectado. |
| **Photos at Random** | Captura algumas fotos aleatórias ao longo do teste em intervalos aleatórios. |
| **Enforce Full Screen** | Obriga os candidatos a realizar o teste em modo de tela cheia. Sair do modo tela cheia é registrado como uma infração. |
| **Enforce Desktop** | Exige que os candidatos usem um computador desktop ou laptop. O teste não será carregado em tablets ou dispositivos móveis. |
| **Photo Before Test Start** | Captura uma foto do candidato antes do início do teste. |
| **Customize Message** | Personalize a mensagem que os candidatos veem ao serem solicitados a tirar uma foto antes do teste. Use isso para pedir aos candidatos que mostrem seu documento de identidade. |

{% hint style="info" %}
A opção **Customize Message** é um recurso Premium.
{% endhint %}


## Supervisão Avançada

A supervisão avançada adiciona medidas anti-fraude avançadas. Cada recurso de supervisão avançada requer **4 créditos adicionais por tentativa**.

![Painel de supervisão avançada](images/creating-tests/enhanced-proctoring.png)
*Painel de supervisão avançada*

| Recurso | O Que Faz | Créditos |
|---|---|---|
| **ID Card Verification** | O candidato faz upload de um documento de identidade (carteira de candidato, passaporte, carteira de motorista, identidade governamental) com foto e nome visíveis. O AutoProctor verifica isso com a Foto Antes do Início do Teste e o nome inserido pelo candidato. | 4 por tentativa |
| **Impersonation Detection** | Detecta se alguém diferente do candidato original está realizando o teste. | 4 por tentativa |
| **Auxiliary Device (360°)** | O candidato emparelha seu celular com o laptop para supervisão em 360 graus. Também ajuda a detectar ferramentas de IA que exibem respostas como sobreposições na tela. | 4 por tentativa |
| **Session Recording** | Grava a tela e as ações do candidato, incluindo cliques do mouse e entrada do teclado. | 4 por tentativa |


## Configurações de Comunicação

Essas configurações controlam como as evidências de infrações são tratadas:

- **Me after the Test** — Armazena evidências (fotos, áudio, capturas de tela) para revisão posterior. Mantenha isso ativado, a menos que você tenha um motivo específico para desativar.
- **User during the Test** — Notifica o candidato durante o teste quando uma infração é detectada. Isso ajuda os candidatos a corrigir problemas inofensivos (como música de fundo acionando uma infração de ruído).

![Painel de configurações de comunicação](images/settings/communication-settings.png)
*Painel de configurações de comunicação*

{% hint style="info" %}
Recomendamos manter ambas as configurações de comunicação ativadas para a melhor experiência de supervisão.
{% endhint %}

## Recursos Relacionados

- [Configurações de Tempo](tests-results/create/timer-settings.md) — Configure a duração do teste e janelas de tempo
- [Supervisão Avançada](tests-results/create/enhanced-proctoring.md) — Guia detalhado sobre verificação de identidade, detecção de impostor e supervisão em 360°
- [Configurações do Questionário](socratease/settings/quiz-settings.md) — Para configurações específicas de questionários Socratease, consulte a página de Configurações do Questionário do Socratease
- [O Que é Monitorado](understanding/how-proctoring-works/what-gets-tracked.md) — Lista completa de tudo o que o AutoProctor monitora
- [Resultados de Supervisão](tests-results/results/proctoring-results.md) — Como revisar os dados de supervisão após um teste
- [Trust Score](understanding/how-proctoring-works/trust-score.md) — Como o Trust Score é calculado a partir dos dados de supervisão

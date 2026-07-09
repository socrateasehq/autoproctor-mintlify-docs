---
title: "Configurações de Questionários Socratease"
description: "Configure seu questionário Socratease com configurações de modo de exibição, visibilidade de resultados, aleatorização e mais."
---

O Socratease possui seu próprio conjunto de configurações, distintas das configurações gerais de Tempo e Supervisão do AutoProctor. Essas configurações controlam como o questionário se comporta para seus candidatos — desde como as perguntas aparecem até se os candidatos podem copiar e colar.


## Configurações Disponíveis

### 1. Modo de Exibição de Perguntas (Premium)

Controle como as perguntas aparecem para os candidatos: todas de uma vez (estilo Google Forms), uma por uma com navegação (estilo Typeform) ou uma por uma sem navegação. Essa configuração também afeta como os temporizadores funcionam.

Para mais detalhes, consulte [Modo de Exibição de Perguntas](socratease/settings/question-display-mode.md).

### 2. Visibilidade dos Resultados

Controle quando os candidatos veem suas pontuações e resultados:
- **Imediatamente** após o envio
- **Quando você libera pontuações individuais** (um candidato por vez)
- **Quando você libera todas as pontuações** (todos de uma vez)
- **Nunca** — os resultados são retidos por completo

Para mais detalhes, consulte [Mostrar Resultados aos Candidatos](socratease/settings/showing-results-to-candidates.md).

### 3. Aleatorização de Perguntas

Aleatorize a ordem das perguntas para cada candidato. O que o Candidato 1 vê como Pergunta 1 pode ser a Pergunta 10 para o Candidato 2. Isso reduz a oportunidade de os candidatos compartilharem respostas durante um teste.

{% hint style="info" %}
Esta opção está disponível apenas quando você usa o modo [Todas de uma vez (estilo Google Forms)](socratease/settings/question-display-mode.md).
{% endhint %}


### 4. Mistura de Opções

Para perguntas do tipo MCQ e MCA, você pode aleatorizar a ordem das opções de resposta entre os candidatos. Mesmo que dois candidatos vejam a mesma pergunta, as opções aparecem em uma ordem diferente.


### 5. Restrição de Copiar e Colar

Quando você ativa essa configuração, os candidatos não podem copiar o texto das perguntas do questionário nem colar texto de outra aba ou aplicativo no questionário. Isso reduz a dependência de ferramentas externas e assistentes de IA.


### 6. Envio Automático por Troca de Aba

Defina o número máximo de trocas de aba permitidas durante o teste. Se um candidato exceder esse limite, o teste é automaticamente enviado. Isso desencoraja os candidatos de mudar para outras abas para procurar respostas.

{% hint style="warning" %}
Quando um teste é enviado automaticamente devido ao limite de troca de aba, o candidato não pode retomar o teste. Certifique-se de comunicar a política de troca de aba aos seus candidatos antecipadamente.
{% endhint %}


### 7. Instruções Personalizadas

Adicione orientações gerais sobre o teste que são exibidas aos candidatos antes de iniciarem o questionário. Use isso para comunicar regras, instruções ou expectativas importantes.

{% hint style="info" %}
As instruções personalizadas estão disponíveis apenas quando você usa o modo de exibição de perguntas **todas de uma vez**.
{% endhint %}


### 8. Suporte de LaTeX

Se você deseja incluir equações matemáticas, escreva-as usando a sintaxe LaTeX e elas serão automaticamente renderizadas como equações formatadas. Ative essa configuração para habilitar a renderização de LaTeX no seu questionário.

Para mais detalhes, consulte [Uso de LaTeX para Equações Matemáticas](socratease/settings/latex-math-equations.md).

## Como Acessar as Configurações do Questionário

{% embed url="videos/socratease/soc-quiz-settings.mp4" %}
Como acessar e configurar as configurações do questionário Socratease
{% endembed %}

{% stepper %}
{% step %}
### Abra Seu Questionário
Abra o Questionário Socratease que deseja configurar a partir do seu [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/).
{% endstep %}
{% step %}
### Clique no Ícone de Configurações
Clique no ícone de **Settings** (engrenagem) na barra de ferramentas do editor de questionários.
{% endstep %}
{% step %}
### Ajuste Suas Configurações
Modifique qualquer uma das oito configurações listadas acima. As alterações são salvas automaticamente.
{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [Modo de Exibição de Perguntas](socratease/settings/question-display-mode.md) — Explicação detalhada das opções de exibição
- [Mostrar Resultados aos Candidatos](socratease/settings/showing-results-to-candidates.md) — Controle a visibilidade dos resultados
- [Uso de LaTeX para Equações Matemáticas](socratease/settings/latex-math-equations.md) — Adicione equações matemáticas aos seus questionários
- [Configurações de Tempo](tests-results/create/timer-settings.md) — Para configuração geral do temporizador e supervisão do teste (separada das configurações do questionário Socratease)
- [Criar um Questionário](socratease/create-questions/creating-a-quiz.md) — Guia passo a passo para criar um questionário

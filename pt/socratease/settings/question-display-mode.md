---
title: "Modo de Exibição de Perguntas"
description: "Controle como as perguntas são exibidas para os candidatos — todas de uma vez, uma por uma com navegação ou uma por uma sem navegação."
---

A configuração do Modo de Exibição de Perguntas controla como as perguntas aparecem para os participantes do teste. Você pode escolher entre três opções de exibição, cada uma com diferentes implicações para navegação, tempo e segurança do teste.

{% hint style="info" %}
O Modo de Exibição de Perguntas é um recurso **Premium**. Consulte [Pagamentos e Créditos](pricing-account/plans-credits/payments-and-credits.md) para os detalhes do plano.
{% endhint %}

## Modos de Exibição

![Painel de configurações do modo de exibição de perguntas mostrando as três opções disponíveis](../../images/socratease/question-display-mode.png)
*Configuração do modo de exibição de perguntas nas configurações do questionário*

### 1. Todas de Uma Vez (estilo Google Forms)

Os candidatos veem todas as perguntas ao mesmo tempo, uma abaixo da outra, como em um Google Form. O temporizador se aplica ao **teste inteiro**. Os candidatos podem rolar livremente entre as perguntas e respondê-las em qualquer ordem.

![Vista do candidato do modo todas de uma vez mostrando todas as perguntas em uma página](../../images/socratease/all-at-once.png)
*Modo todas de uma vez*

### 2. Uma por Uma com Navegação (estilo Typeform)

Os candidatos veem uma pergunta de cada vez e podem navegar para frente e para trás entre as perguntas. O temporizador se aplica ao **teste inteiro**, não às perguntas individuais. Os candidatos podem revisitar e alterar suas respostas a qualquer momento antes do envio.

![Vista do candidato do modo uma por uma com navegação mostrando uma pergunta com botões Próximo e Anterior](../../images/socratease/one-by-one-like-typeform.png)
*Uma por uma com navegação*

### 3. Uma por Uma sem Navegação

Os candidatos veem uma pergunta de cada vez. Depois de enviar uma pergunta (respondendo ou pulando), **não podem voltar a ela**. O temporizador é definido **por pergunta**, não para todo o teste.

![Vista do candidato do modo uma por uma sem navegação mostrando uma pergunta com botões Enviar e Pular](../../images/socratease/one-by-one.png)
*Uma por uma sem navegação*

## Diferenças Principais

| Característica | Todas de uma vez | Uma por uma com nav. | Uma por uma sem nav. |
|---|:---:|:---:|:---:|
| Escopo do temporizador | Teste inteiro | Teste inteiro | Por pergunta |
| Pode voltar a perguntas anteriores | Sim | Sim | Não |
| Instruções personalizadas | Sim | Não | Não |

## Quando Usar Uma por Uma sem Navegação

A opção sem navegação é especialmente útil para a segurança do teste. Os candidatos podem visualizar apenas uma pergunta de cada vez por uma duração limitada, o que reduz significativamente a oportunidade de fraude. Cada pergunta tem seu próprio temporizador, então os candidatos não podem gastar tempo extra em perguntas difíceis apressando-se nas mais fáceis.

## Como as Configurações de Tempo Mudam

{% hint style="warning" %}
Quando você usa **uma por uma sem navegação**, certas configurações de tempo no nível do teste ficam indisponíveis. O comportamento do temporizador muda para o nível da pergunta:

- **Duração**: Você define a duração por pergunta, não para o teste inteiro
- **Envio Automático**: Cada pergunta é enviada automaticamente quando seu temporizador individual expira
- **Must Submit By**: Essa configuração no nível do teste é substituída por **Cannot Start After** no nível do teste
{% endhint %}

Para mais informações sobre configuração de temporizadores, consulte [Configurações de Tempo](tests-results/create/timer-settings.md).

## Como Definir o Modo de Exibição

{% embed url="../../videos/socratease/question-display-mode.mp4" %}
Como definir o modo de exibição de perguntas
{% endembed %}

{% stepper %}
{% step %}
### Abra Seu Questionário
Abra o Questionário Socratease que deseja configurar a partir do seu [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/).
{% endstep %}
{% step %}
### Acesse as Configurações
Clique no ícone de **Settings** (engrenagem) na barra de ferramentas do editor de questionários.
{% endstep %}
{% step %}
### Selecione o Modo de Exibição
Escolha seu modo de exibição preferido no menu suspenso de **Question Display Mode**. O padrão é "Todas de uma vez".


{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [Configurações do Questionário](socratease/settings/quiz-settings.md) — Todas as opções de configuração de questionários Socratease
- [Configurações de Tempo](tests-results/create/timer-settings.md) — Configure temporizadores no nível do teste e da pergunta
- [Como Criar um Questionário Socratease](socratease/create-questions/creating-a-quiz.md) — Guia de criação passo a passo
- [Mostrar Resultados aos Candidatos](socratease/settings/showing-results-to-candidates.md) — Controle a visibilidade dos resultados

---
title: "Uso de LaTeX para Equações Matemáticas"
description: "Adicione equações matemáticas aos seus questionários Socratease usando a sintaxe LaTeX."
---

O Socratease suporta LaTeX, o padrão global para escrever equações matemáticas usado em publicações acadêmicas, livros didáticos e artigos de pesquisa em todo o mundo. Em vez de inserir imagens de equações ou usar notação de texto simplificada como `a^2` ou `3/4`, você pode escrever equações formatadas corretamente diretamente nas suas perguntas.

{% hint style="info" %}
O suporte a equações LaTeX é exclusivo dos **Socratease Quizzes** do AutoProctor. Não está disponível ao usar outros provedores de questionários.
{% endhint %}

## Como Escrever Equações LaTeX

Para incluir uma equação LaTeX no seu questionário, envolva a equação entre os delimitadores `\(` e `\)`.

**Exemplo:**

```
\(a^2 + b^2 = c^2\)
```

Isso é renderizado como o conhecido teorema de Pitágoras: a ao quadrado mais b ao quadrado é igual a c ao quadrado.


## O Que o LaTeX Suporta

O LaTeX pode renderizar qualquer notação matemática, incluindo:

| Notação | Sintaxe LaTeX | Descrição |
|---|---|---|
| Aritmética básica | `\(a + b = c\)` | Adição, subtração, multiplicação, divisão |
| Expoentes | `\(x^2\)` | Sobrescritos e potências |
| Índices | `\(a_n\)` | Notação de subscrito |
| Frações | `\(\frac{a}{b}\)` | Notação de fração |
| Raízes quadradas | `\(\sqrt{x}\)` | Raízes quadradas e enésimas |
| Integrais | `\(\int_0^1 x^2 dx\)` | Integrais definidas e indefinidas |
| Somatórios | `\(\sum_{i=1}^{n} i\)` | Notação de somatório |
| Letras gregas | `\(\alpha, \beta, \gamma\)` | Todos os símbolos de letras gregas |

Você também pode usar qualquer outra notação matemática padrão do LaTeX além dos exemplos listados acima.

## Ativando o LaTeX

{% embed url="videos/socratease/using-latex.mp4" %}
Como ativar e usar LaTeX no Socratease
{% endembed %}

{% stepper %}
{% step %}
### Abra Seu Questionário
Abra seu Questionário Socratease no AutoProctor.
{% endstep %}
{% step %}
### Acesse as Configurações
Clique no ícone de **Settings** (engrenagem) na barra de ferramentas do editor de questionários.
{% endstep %}
{% step %}
### Ative o Suporte de LaTeX
Ative a configuração **LaTeX Support**. Isso ativa a renderização de LaTeX para todas as perguntas do questionário.


{% endstep %}
{% step %}
### Escreva Suas Equações
Escreva suas equações no texto das perguntas usando os delimitadores `\(` e `\)`. As equações são renderizadas como fórmulas matemáticas formatadas quando os candidatos visualizam o questionário.


{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Certifique-se de ativar o botão de Suporte de LaTeX nas configurações do questionário **antes** de compartilhar o teste. Se o LaTeX não estiver ativado, os candidatos verão a sintaxe LaTeX bruta em vez das equações renderizadas.
{% endhint %}

## Experimente

Você pode ver um questionário de exemplo demonstrando a renderização de equações LaTeX em:
[autoproctor.co/tests/jVRBZGRMNU/load](https://www.autoproctor.co/tests/jVRBZGRMNU/load/)


## Recursos Relacionados

- [Configurações do Questionário](socratease/settings/quiz-settings.md) — Todas as opções de configuração de questionários Socratease
- [Tipos de Perguntas](socratease/create-questions/question-types.md) — Formatos de perguntas disponíveis
- [Como Criar um Questionário Socratease](socratease/create-questions/creating-a-quiz.md) — Guia de criação passo a passo
- [Por Que Socratease?](socratease/create-questions/why-socratease.md) — Benefícios de usar o Socratease em relação a outras plataformas

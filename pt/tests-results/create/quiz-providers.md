---
title: "Provedores de Questionários"
description: "Conheça as plataformas de questionários que você pode utilizar com o AutoProctor para testes online supervisionados."
---

O AutoProctor é uma plataforma de supervisão com inteligência artificial que monitora os candidatos durante as avaliações online. Você fornece o seu próprio questionário, e o AutoProctor cuida da supervisão.

Existem dois caminhos:

1. **Use a ferramenta de questionários própria do AutoProctor ([Socratease](socratease/create-questions/why-socratease.md))** — você cria e configura as perguntas, a pontuação e a correção diretamente dentro do AutoProctor.
2. **Use um provedor de questionários externo** (Google Forms, Microsoft Forms, TypeForm, etc.) — suas perguntas, pontuação e configurações permanecem nessa plataforma. O AutoProctor apenas adiciona a supervisão.

## Escolhendo um Provedor de Questionários

{% embed url="../../videos/creating-tests/all-test-types.mp4" %}
Como criar um teste com diferentes provedores de questionários no AutoProctor. Você só pode selecionar um provedor por teste
{% endembed %}

{% stepper %}
{% step %}
### Crie um Novo Teste
Acesse seu [**Dashboard**](https://www.autoproctor.co/test-admin/home/) e clique em **Create Test**.
{% endstep %}
{% step %}
### Selecione um Provedor de Questionários
Escolha um dos provedores disponíveis: **Socratease Quizzes**, **Google Forms**, **Microsoft Forms** ou **IFrame/Other**.
{% endstep %}
{% step %}
### Configure a Supervisão
Configure as definições de [tempo](tests-results/create/timer-settings.md) e [supervisão](tests-results/create/proctoring-settings.md). Se você escolheu o Socratease, também configura as perguntas e a correção dentro do AutoProctor. Para provedores externos, o conteúdo do questionário permanece nessa plataforma.
{% endstep %}
{% endstepper %}

## Provedores de Questionários Disponíveis

| Provedor | Melhor Para | Principal Vantagem |
|---|---|---|
| **Socratease Quizzes** | Avaliações com recursos completos | Integração nativa com proteção de envio automático |
| **Google Forms** | Usuários existentes de Google Forms | Complemento dedicado para criação automática de testes |
| **Microsoft Forms** | Organizações do ecossistema Microsoft | Integração perfeita para avaliações corporativas |
| **IFrame/Other** | TypeForm, ProProfs, ClassMarker, etc. | Adiciona supervisão a qualquer plataforma de questionários baseada na web |

### Questionários do Socratease

O Socratease é a ferramenta nativa de questionários do AutoProctor. Ele oferece a integração mais completa e a melhor experiência para o candidato:

- **Botão de envio único** evita a perda de respostas por sequenciamento incorreto
- **Proteção de envio automático** salva as respostas antes de o teste ser encerrado
- **Múltiplos tipos de perguntas** incluindo múltipla escolha, dissertações, respostas por voz, programação e mais
- **Importação em massa por Excel** e bancos de questões para montagem rápida de questionários

### Google Forms

O Google Forms é a plataforma de questionários mais utilizada. O AutoProctor oferece um [**complemento dedicado para Google Forms**](https://workspace.google.com/marketplace/app/timer_+_proctor_google_forms_autoproctor/691377974459) que cria um teste supervisionado diretamente de dentro do seu Google Form.

### Microsoft Forms

O Microsoft Forms é a segunda plataforma mais utilizada, especialmente dentro de organizações que dependem do ecossistema Microsoft para avaliações internas e processos de contratação.

### IFrame/Outros Provedores

Existem centenas de plataformas de questionários, incluindo TypeForm, ProProfs e ClassMarker. Embora essas plataformas não possuam supervisão remota integrada, você pode adicionar a supervisão do AutoProctor a qualquer uma delas selecionando a opção **IFrame/Other**. O AutoProctor incorpora seu questionário dentro de uma janela de navegador supervisionada.

{% hint style="info" %}
Ao usar provedores IFrame/Other, você pode personalizar a URL incorporada usando [argumentos de consulta](tests-results/create/iframe-query-arguments.md).
{% endhint %}

## Recursos Relacionados

- [Por Que Socratease?](socratease/create-questions/why-socratease.md) — Benefícios de usar a ferramenta nativa de questionários do AutoProctor
- [Como Criar um Questionário do Socratease](socratease/create-questions/creating-a-quiz.md) — Guia de criação passo a passo
- [Configurações de Tempo](tests-results/create/timer-settings.md) — Configure a duração do teste e janelas de tempo
- [Configurações de Supervisão](tests-results/create/proctoring-settings.md) — Opções de câmera, microfone e troca de aba
- [Argumentos de Consulta do IFrame](tests-results/create/iframe-query-arguments.md) — Personalize as URLs de questionários incorporados
- [Configurações Avançadas](tests-results/create/advanced-settings.md) — Provedores de login, colaboradores e mais

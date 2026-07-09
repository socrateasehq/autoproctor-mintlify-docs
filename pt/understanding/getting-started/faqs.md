---
title: "Perguntas Frequentes"
description: "Respostas para as perguntas mais comuns sobre a plataforma de supervisão, os preços e as capacidades do AutoProctor."
---

Encontre abaixo as respostas para as perguntas mais frequentes sobre o AutoProctor. Se sua pergunta não está coberta aqui, [entre em contato com nossa equipe de suporte](pricing-account/support/contact-us.md).

<AccordionGroup>
  <Accordion title="Como o AutoProctor garante a integridade dos testes on-line?">
    O AutoProctor utiliza monitoramento por IA no dispositivo que acessa câmeras, microfones e telas (com a permissão do candidato) para detectar comportamentos problemáticos. Isso inclui pessoas não autorizadas no enquadramento, ruído de fundo e tentativas de navegar para fora da tela do teste. Cada incidente gera um relatório detalhado de infração com evidências para sua revisão.

    Saiba mais sobre [o que é monitorado](understanding/how-proctoring-works/what-gets-tracked.md) durante a supervisão.
  </Accordion>

  <Accordion title="Como eu crio e administro testes no AutoProctor?">
    Você cria um teste supervisionado em cinco etapas:

{% stepper %}
{% step %}
### Crie um questionário
Elabore seu questionário usando Google Forms, Microsoft Forms ou [Socratease](socratease/create-questions/why-socratease.md).
{% endstep %}
{% step %}
### Registre o teste no AutoProctor
Faça login no AutoProctor e registre a URL do seu questionário, ou crie um questionário Socratease diretamente na plataforma.
{% endstep %}
{% step %}
### Configure as definições de supervisão
Configure o monitoramento por câmera, microfone, compartilhamento de tela e outras opções nas suas [configurações de supervisão](tests-results/create/proctoring-settings.md).
{% endstep %}
{% step %}
### Compartilhe o link do teste com os candidatos
Distribua o link exclusivo do teste AutoProctor para seus candidatos por e-mail, LMS ou qualquer ferramenta de mensagens.
{% endstep %}
{% step %}
### Revise os relatórios de infrações
Após o teste, revise os [resultados de supervisão](tests-results/results/proctoring-results.md) e os [Trust Scores](understanding/how-proctoring-works/trust-score.md) de cada candidato.
{% endstep %}
{% endstepper %}

    Para um guia completo, consulte o [Guia de Início Rápido](tests-results/create/your-first-proctored-test.md).
  </Accordion>

  <Accordion title="Quais são os planos de preços do AutoProctor?">
    O AutoProctor oferece três níveis de assinatura:

    | Plano | O Que Inclui |
    |---|---|
    | **Standard** | 150 créditos de supervisão por ciclo de faturamento, mais tentativas ilimitadas apenas com temporizador |
    | **Premium** | Recursos Standard mais capacidades de colaboração em equipe |
    | **Elite** | Recursos Premium mais tipos de perguntas avançados, bancos de questões e acesso à API/SDK |

    Todos os planos incluem um **teste gratuito de 10 créditos** sem necessidade de cartão de crédito. Você pode cancelar a qualquer momento.

    Visite a [página de preços](https://www.autoproctor.co/pricing/) para consultar as tarifas atuais, ou veja [Pagamentos e Créditos](pricing-account/plans-credits/payments-and-credits.md) para detalhes sobre como os créditos funcionam.
  </Accordion>

  <Accordion title="Quantos candidatos podem realizar um teste supervisionado simultaneamente?">
    O AutoProctor suporta até **5.000 candidatos simultâneos** em um único teste.

{% hint style="info" %}
Se você prevê mais de 5.000 candidatos realizando um teste ao mesmo tempo, [entre em contato conosco](pricing-account/support/contact-us.md) com pelo menos dois dias úteis de antecedência para que possamos preparar nossa infraestrutura.
{% endhint %}

    Saiba mais sobre os [limites de concorrência](tests-results/access-limits/concurrency.md).
  </Accordion>

  <Accordion title="Como o AutoProctor protege a privacidade e os dados dos usuários?">
    O AutoProctor coleta nomes, endereços de e-mail, imagens e gravações de áudio exclusivamente para fins de integridade dos testes. A empresa não vende informações pessoais nem as compartilha com terceiros além dos subprocessadores necessários.

    Fatos importantes sobre privacidade:
    - Todo o monitoramento por IA acontece **no dispositivo do candidato** — nenhuma gravação de vídeo completa é carregada nos servidores
    - Os dados são usados exclusivamente para gerar relatórios de supervisão
    - Candidatos menores de 18 anos necessitam do consentimento dos pais ou responsáveis

{% hint style="info" %}
O AutoProctor não grava vídeo completo. Consulte [O AutoProctor Grava Vídeo?](understanding/how-proctoring-works/video-recording.md) para detalhes sobre como a abordagem de monitoramento no dispositivo protege a privacidade do candidato.
{% endhint %}
  </Accordion>

  <Accordion title="Quais plataformas de questionários o AutoProctor suporta?">
    O AutoProctor funciona com as seguintes plataformas de questionários:

    - **Google Forms**
    - **Microsoft Forms**
    - **Socratease** (plataforma de questionários integrada do AutoProctor)
    - **Qualquer questionário baseado na web** via incorporação por iframe

    Consulte [Provedores de Questionários](tests-results/create/quiz-providers.md) para instruções de configuração de cada plataforma.
  </Accordion>

  <Accordion title="Posso restringir quem pode realizar meu teste?">
    Sim. O AutoProctor oferece várias opções de controle de acesso:

    - **[Restringir por domínio de e-mail](tests-results/access-limits/restricting-by-email.md)** — Permita apenas candidatos com domínios de e-mail específicos (por exemplo, @universidade.edu)
    - **[Restringir a usuários específicos](tests-results/access-limits/restricting-to-some-users.md)** — Permita apenas uma lista pré-aprovada de endereços de e-mail
    - **[Convidar candidatos por e-mail](tests-results/access-limits/inviting-candidates-via-email.md)** — Envie convites diretos para candidatos específicos

    Você configura essas opções nas suas [configurações avançadas](tests-results/create/advanced-settings.md).
  </Accordion>
</AccordionGroup>

## Recursos Relacionados

- [Início Rápido](tests-results/create/your-first-proctored-test.md) — Crie seu primeiro teste supervisionado em menos de 5 minutos
- [O Que é Monitorado](understanding/how-proctoring-works/what-gets-tracked.md) — Todas as capacidades de monitoramento disponíveis
- [Trust Score](understanding/how-proctoring-works/trust-score.md) — Como o AutoProctor classifica a integridade do candidato
- [Compatibilidade de Dispositivos](understanding/getting-started/device-compatibility.md) — Navegadores e dispositivos compatíveis
- [Fale Conosco](pricing-account/support/contact-us.md) — Obtenha ajuda da equipe de suporte do AutoProctor
- [Agendar uma Demonstração](pricing-account/support/booking-a-demo.md) — Agende uma apresentação ao vivo do AutoProctor

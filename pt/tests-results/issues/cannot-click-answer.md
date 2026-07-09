---
title: "Não Consigo Clicar nas Respostas do Formulário do Teste"
description: "Resolva o problema em que o formulário do teste carrega mas você não consegue clicar nas perguntas nem selecionar respostas. Geralmente causado por estar conectado com a conta Google incorreta."
---

Se você consegue ver o formulário do teste mas não consegue clicar nas perguntas nem selecionar respostas, o mais provável é que você esteja conectado com uma conta Google que não tem permissão para interagir com o formulário.

## Por Que Isso Acontece

Quando um Google Form é restrito a endereços de e-mail específicos, ele carrega em modo somente leitura para contas não autorizadas. Você pode ver as perguntas mas não pode interagir com elas. Como o AutoProctor incorpora o Google Form dentro de sua interface, essa restrição aparece dentro da janela de teste do AutoProctor.

![Google Form no AutoProctor que não pode ser clicado porque a conta Google incorreta está ativa](../../images/candidate-issues/cannot-click-form.png)
*Formulário do teste carregado em modo somente leitura devido à conta Google incorreta*

## Como Resolver

{% stepper %}
{% step %}
### Saia de todas as contas Google
Acesse [accounts.google.com/Logout](https://accounts.google.com/Logout) e saia de todas as suas contas.
{% endstep %}
{% step %}
### Faça login com a conta correta
Faça login novamente com a conta Google que tem acesso ao teste. Consulte seu administrador de testes se não tiver certeza de qual conta usar.
{% endstep %}
{% step %}
### Recarregue o teste
Volte ao link do teste e carregue-o novamente. Agora você deverá conseguir clicar nas perguntas e selecionar respostas.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Se você não tem certeza de qual conta Google tem acesso, entre em contato com seu administrador de testes. Ele pode confirmar o endereço de e-mail que recebeu permissão para realizar o teste.
{% endhint %}

## Recursos Relacionados

- [Página em Branco ou Tela Cinza](tests-results/issues/blank-page-grey-screen.md) -- Problema similar causado pela conta Google incorreta
- [Não Consigo Ver as Perguntas no Google Forms](tests-results/issues/google-forms-questions-not-visible.md) -- Restrições de acesso ao Google Forms
- [Como Fazer Logout](candidate-guide/attempting/how-to-logout.md) -- Passos para trocar de conta
- [Instruções para Testes Supervisionados](candidate-guide/attempting/proctored-test-instructions.md) -- Guia de configuração com seção de Conta Google
- [Compatibilidade de Dispositivos](understanding/getting-started/device-compatibility.md) -- Confira os navegadores e dispositivos compatíveis
- [Fale Conosco](pricing-account/support/contact-us.md) -- Entre em contato se precisar de ajuda adicional

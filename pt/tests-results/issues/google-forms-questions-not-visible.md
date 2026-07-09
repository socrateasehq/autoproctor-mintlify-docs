---
title: "Não Consigo Ver as Perguntas no Google Forms"
description: "Entenda por que as perguntas podem não estar visíveis em um Google Form carregado pelo AutoProctor e como resolver erros de restrição de acesso."
---

O AutoProctor carrega o seu Google Form dentro do seu próprio site para supervisão. Se o Google Form tem uma restrição de acesso ou outro erro, essa mesma mensagem de erro aparece dentro da interface do AutoProctor. O AutoProctor não pode controlar nem modificar nada dentro do Google Form devido a restrições de privacidade.

## Por Que as Perguntas Não Estão Visíveis

O Google Forms pode restringir o acesso com base na organização, no domínio de e-mail ou em contas específicas. Quando você está conectado com uma conta que não atende a essas restrições, o Google bloqueia o conteúdo do formulário e exibe uma mensagem de erro em seu lugar.


![Google Form exibindo erro de acesso restrito dentro da interface do AutoProctor](../../images/candidate-issues/google-forms-access-restricted.png)
*Google Form mostrando uma mensagem de restrição de acesso dentro do AutoProctor*

## Como Resolver

{% stepper %}
{% step %}
### Verifique a mensagem de erro
Leia a mensagem de erro exibida no formulário. Geralmente ela explica se o formulário está restrito a determinados usuários ou a uma organização.
{% endstep %}
{% step %}
### Faça login com a conta correta
Saia da sua conta Google atual em [accounts.google.com/Logout](https://accounts.google.com/Logout), depois faça login com a conta que tem acesso ao formulário.
{% endstep %}
{% step %}
### Entre em contato com o criador do formulário se necessário
Se você não tem certeza de qual conta usar ou acredita que deveria ter acesso, entre em contato com a pessoa que criou o teste. Ela pode precisar atualizar as configurações de compartilhamento do formulário.
{% endstep %}
{% endstepper %}

## Por Que o AutoProctor Não Pode Resolver Isso

Devido a restrições de privacidade, o Google não permite que o AutoProctor acesse ou modifique nada dentro de um Google Form. O AutoProctor apenas pode carregar o formulário -- não pode controlar o conteúdo, as configurações de acesso nem as mensagens de erro do formulário. Se você encontrar um problema de acesso ao formulário, somente o criador do formulário pode resolvê-lo.

{% hint style="info" %}
O AutoProctor incorpora Google Forms de forma semelhante a como os sites incorporam vídeos do YouTube. Se um vídeo do YouTube apresenta um erro em um site externo, o problema é do YouTube, não do site que o incorpora. O mesmo se aplica ao Google Forms no AutoProctor -- qualquer erro que você vê tem origem no Google, não no AutoProctor.
{% endhint %}

## Recursos Relacionados

- [Não Consigo Ver a Resposta no Google Forms](tests-results/issues/google-forms-response-not-visible.md) -- Respostas ausentes após o envio
- [Não Consigo Clicar na Resposta](tests-results/issues/cannot-click-answer.md) -- O formulário carrega mas não é interativo
- [Página em Branco ou Tela Cinza](tests-results/issues/blank-page-grey-screen.md) -- O formulário não carrega de forma alguma
- [Instruções para Testes Supervisionados](candidate-guide/attempting/proctored-test-instructions.md) -- Guia de configuração com seção de Conta Google
- [Como Fazer Logout](candidate-guide/attempting/how-to-logout.md) -- Passos para trocar de conta
- [Fale Conosco](pricing-account/support/contact-us.md) -- Entre em contato se precisar de ajuda adicional

---
title: "Não Consigo Ver a Resposta no Google Forms"
description: "Entenda por que as respostas podem aparecer no AutoProctor mas não no Google Forms, ou vice-versa. Geralmente causado por pular um dos dois botões de envio."
---

Se você consegue ver a resposta de um candidato no AutoProctor mas não no Google Forms (ou vice-versa), o mais provável é que o candidato tenha pulado um dos dois botões de envio necessários. Esta é a principal razão pela qual respostas desaparecem entre as duas plataformas.

## Entendendo os Dois Botões de Envio

Os candidatos devem clicar em **dois botões de envio separados** para completar um teste baseado em Google Forms no AutoProctor:

1. **Botão de envio roxo** (dentro do Google Form) -- envia as respostas para a seção de Respostas do Google Forms
2. **Botão de envio verde** (no topo da página) -- envia a sessão de supervisão ou cronometrada para o AutoProctor

![Botão de envio roxo do Google Forms e botão de envio verde do AutoProctor mostrados em um teste supervisionado](../../images/taking-tests/submit-buttons-proctored.png)
*Os dois botões de envio: roxo para o Google Forms, verde para o AutoProctor*

### Se o Candidato Pular o Botão de Envio Verde

Você verá as respostas do candidato na seção de **Respostas do Google Forms** mas não verá nenhum resultado no AutoProctor. A sessão de supervisão não foi finalizada.

### Se o Candidato Pular o Botão de Envio Roxo

Você verá o teste marcado como enviado no **AutoProctor**, mas as respostas do candidato não aparecerão nas Respostas do Google Forms. As respostas do formulário nunca foram enviadas ao Google.

{% hint style="warning" %}
Devido a restrições de privacidade, o Google não permite que o AutoProctor detecte se o botão de envio roxo foi clicado. Não há como o AutoProctor aplicar essa etapa automaticamente.
{% endhint %}

## Certifique-se de Compartilhar o Link do AutoProctor

Você deve enviar aos candidatos o **link do AutoProctor** (que contém `autoproctor.co` na URL). Se você enviar o link direto do Google Forms, os candidatos ignorarão o AutoProctor completamente e nenhum dado de supervisão será registrado.

## Por Que o AutoProctor Não Pode Resolver Isso

O AutoProctor incorpora Google Forms de forma semelhante a como os sites incorporam vídeos do YouTube. O Google não permite que o AutoProctor acesse ou controle nada do que acontece dentro do formulário. Se ocorrer um problema de envio dentro do Google Form, somente o Google controla esse comportamento.

{% hint style="info" %}
Para evitar a confusão com dois botões de envio, considere usar [questionários Socratease](socratease/create-questions/why-socratease.md) em vez do Google Forms. O Socratease tem um único botão de envio que gerencia tanto as respostas do questionário quanto a supervisão em uma única etapa.
{% endhint %}

## Recursos Relacionados

- [Diferenças do Botão de Envio](candidate-guide/attempting/submit-button.md) -- Comparação completa entre Socratease e outros tipos de questionários
- [Não Consigo Ver as Perguntas no Google Forms](tests-results/issues/google-forms-questions-not-visible.md) -- Problemas de acesso ao Google Forms
- [Resultados de Supervisão](tests-results/results/proctoring-results.md) -- Como revisar relatórios de supervisão
- [Por Que Socratease?](socratease/create-questions/why-socratease.md) -- Benefícios de usar o Socratease em vez do Google Forms
- [Fale Conosco](pricing-account/support/contact-us.md) -- Entre em contato se precisar de ajuda adicional

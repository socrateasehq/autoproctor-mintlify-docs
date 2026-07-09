---
title: "Restringir o Acesso ao Teste a Candidatos Específicos"
description: "Limite a participação no teste a candidatos específicos no AutoProctor usando distribuição de links, restrições de e-mail, links de convite únicos ou controles de acesso da plataforma."
---

Por padrão, qualquer pessoa com o link do seu teste pode realizá-lo. O AutoProctor oferece vários métodos para restringir o acesso para que apenas os candidatos que você escolher possam participar.

## Método 1: Distribuição Seletiva do Link

A abordagem mais simples é compartilhar o link do teste apenas com os candidatos que devem realizá-lo.

{% stepper %}
{% step %}
### Identifique os candidatos elegíveis
Determine quais candidatos devem ter acesso ao teste.
{% endstep %}
{% step %}
### Compartilhe o link de forma privada
Envie o link do teste apenas para esses candidatos por e-mail, pelo seu sistema de gestão de aprendizagem ou por outro canal privado. Evite publicar o link de forma pública.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Este método depende de os candidatos não compartilharem o link com outras pessoas. Se você precisa de um controle de acesso mais rigoroso, use um dos métodos abaixo.
{% endhint %}

## Método 2: Restrições Baseadas em E-mail

Use as **Restrições de Login** integradas do AutoProctor para permitir apenas domínios de e-mail ou endereços individuais específicos. Você configura isso na seção de Configurações Avançadas do seu teste.

{% stepper %}
{% step %}
### Abra as Configurações Avançadas
Navegue até as configurações do teste e role até a seção **Advanced Settings**.
{% endstep %}
{% step %}
### Insira as Restrições de Login
Adicione os domínios de e-mail (por exemplo, `@suaescola.edu`) ou endereços de e-mail específicos que deseja permitir.
{% endstep %}
{% step %}
### Salve o teste
Clique em **Create** ou **Update** para aplicar as restrições.
{% endstep %}
{% endstepper %}

![Campo de Restrições de Login com restrições de domínio e e-mail](../../images/settings/login-restrictions-email.png)
*Campo de Restrições de Login com restrições de domínio e e-mail*

Consulte [Restringir o Acesso ao Teste por Endereço de E-mail](tests-results/access-limits/restricting-by-email.md) para instruções completas de configuração e exemplos.

## Método 3: Links de Convite Únicos

Gere URLs únicos por candidato vinculados a endereços de e-mail específicos. Cada candidato recebe seu próprio link com verificação de e-mail, de modo que apenas o destinatário pretendido pode usá-lo.

{% embed url="../../videos/settings/unique-invitation-links.mp4" %}
Configuração de links de convite únicos
{% endembed %}

{% stepper %}
{% step %}
### Ative o URL Único
Abra as configurações do teste e ative a opção **Unique URL**.
{% endstep %}
{% step %}
### Faça upload dos endereços de e-mail
Faça upload dos endereços de e-mail dos candidatos por meio de um arquivo CSV (até 1.000 por vez).
{% endstep %}
{% step %}
### Gere os links únicos
O AutoProctor gera um link único para cada endereço de e-mail como pares separados por vírgulas.
{% endstep %}
{% step %}
### Formate os dados
Cole a saída em um aplicativo de planilha e divida pelo separador de vírgula para organizar os endereços de e-mail e os links em colunas separadas.
{% endstep %}
{% step %}
### Distribua os links únicos
Envie a cada candidato seu link único individualmente usando a planilha que você criou.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Os links de convite únicos estão disponíveis apenas no **Plano Elite** e funcionam com Socratease Quizzes e Testes IFrame. Consulte [Pagamentos e Créditos](pricing-account/plans-credits/payments-and-credits.md) para detalhes do plano.
{% endhint %}

Consulte [Convidar Candidatos por E-mail](tests-results/access-limits/inviting-candidates-via-email.md) para o processo completo de configuração.

## Método 4: Restrições de Acesso do Google Forms

Se você usa Google Forms, pode restringir o acesso no nível do Google Forms em vez de (ou além das) restrições do AutoProctor. Os candidatos ainda podem abrir o link do AutoProctor, mas não podem prosseguir se o Google Forms bloquear o acesso deles.

{% stepper %}
{% step %}
### Abra as configurações do seu Google Form
No Google Forms, clique no ícone de engrenagem de **Settings**.
{% endstep %}
{% step %}
### Restrinja à sua organização
Ative a opção para restringir as respostas aos usuários da sua organização. Isso limita o acesso a candidatos com endereços de e-mail sob o seu domínio de Google Workspace.

![Configurações de restrição de acesso do Google Forms](../../images/settings/google-form-restriction.png)
*Configurações de restrição de acesso do Google Forms*
{% endstep %}
{% endstepper %}

Para mais detalhes, consulte o [guia do Google sobre restrição de acesso a formulários](https://www.bettercloud.com/monitor/the-academy/restrict-access-to-google-forms/).

## Comparação dos Métodos de Controle de Acesso

| Método | Força | Funciona Com | Plano Necessário |
|---|---|---|---|
| Distribuição seletiva do link | Baixa — depende de confiança | Todos os tipos de teste | Qualquer |
| Restrições baseadas em e-mail | Média — bloqueia domínios incorretos | Todos os tipos de teste | Qualquer |
| Links de convite únicos | Alta — verificação por candidato | Socratease Quizzes, Testes IFrame | Elite |
| Restrições do Google Forms | Média — nível organizacional | Apenas Google Forms | Qualquer |

## Recursos Relacionados

- [Restringir o Acesso ao Teste por Endereço de E-mail](tests-results/access-limits/restricting-by-email.md) — Configure restrições baseadas em domínio e e-mail
- [Convidar Candidatos por E-mail](tests-results/access-limits/inviting-candidates-via-email.md) — Gere links de teste únicos por candidato
- [Métodos de Login do Candidato](candidate-guide/attempting/candidate-login-methods.md) — Conheça as opções de autenticação disponíveis
- [Configurações Avançadas](tests-results/create/advanced-settings.md) — Configure Restrições de Login e outras opções avançadas
- [Boas Práticas para Criadores de Testes](understanding/getting-started/best-practices-for-teachers.md) — Dicas para uma administração de testes tranquila

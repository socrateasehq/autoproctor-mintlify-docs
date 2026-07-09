---
title: "Restringir o Acesso ao Teste por Endereço de E-mail"
description: "Limite quem pode realizar o seu teste restringindo o acesso a domínios de e-mail específicos ou endereços individuais usando Restrições de Login."
---

As Restrições de Login permitem que você controle exatamente quem pode realizar seu teste, filtrando candidatos com base no endereço de e-mail. Isso impede o acesso não autorizado mesmo que alguém compartilhe ou descubra o link do seu teste.

## Como Configurar Restrições de E-mail

{% stepper %}
{% step %}
### Abra as configurações do teste
Navegue até o teste no seu [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/) e clique no botão **Settings**.


{% endstep %}
{% step %}
### Acesse as Configurações Avançadas
Role até a seção **Advanced Settings** e localize os campos de **Login Restrictions**.


{% endstep %}
{% step %}
### Adicione restrições de domínio ou e-mail
Insira os domínios de e-mail ou endereços de e-mail específicos que deseja permitir. Você pode combinar ambos os tipos de restrições em um único campo (veja os exemplos abaixo).
{% endstep %}
{% step %}
### Salve o teste
Clique em **Create** ou **Update** para aplicar as restrições.
{% endstep %}
{% endstepper %}

## Restrições Baseadas em Domínio

Você pode restringir o acesso a candidatos cujos endereços de e-mail terminam com domínios específicos. Por exemplo, ao inserir `@abc.com` e `@xyz.com`, apenas os candidatos com esses domínios de e-mail poderão realizar o teste.


![Campo de Restrições de Login mostrando restrições baseadas em domínio com @abc.com e @xyz.com inseridos](images/settings/login-restrictions-domain.png)

## Restrições por E-mail Específico

Você também pode permitir endereços de e-mail individuais juntamente com restrições de domínio. Isso é útil quando a maioria dos candidatos compartilha um domínio, mas alguns participantes externos precisam de acesso.

Por exemplo, você pode permitir todos os usuários cujo e-mail termina em `@abc.com` mais endereços de e-mail individuais específicos como `guest@gmail.com`.


![Campo de Restrições de Login mostrando uma combinação de restrições de domínio e e-mail individual](images/settings/login-restrictions-email.png)

{% hint style="info" %}
As restrições de e-mail funcionam em conjunto com o [método de login](candidate-guide/attempting/candidate-login-methods.md) do candidato. O candidato deve fazer login com um endereço de e-mail que corresponda a um dos domínios ou endereços permitidos que você especificou.
{% endhint %}

## Recursos Relacionados

- [Métodos de Login do Candidato](candidate-guide/attempting/candidate-login-methods.md) — Conheça as opções de autenticação disponíveis para candidatos
- [Restringir a Candidatos Específicos](tests-results/access-limits/restricting-to-some-users.md) — Outros métodos para limitar o acesso ao teste
- [Convidar Candidatos por E-mail](tests-results/access-limits/inviting-candidates-via-email.md) — Gere links de teste únicos por candidato
- [Configurações Avançadas](tests-results/create/advanced-settings.md) — Configure Restrições de Login e outras opções avançadas do teste
- [Boas Práticas para Criadores de Testes](understanding/getting-started/best-practices-for-teachers.md) — Dicas para uma administração de testes tranquila

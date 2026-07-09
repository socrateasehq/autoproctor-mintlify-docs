---
title: "Retomar Testes do Google Forms"
description: "Configure se os candidatos podem retomar testes do Google Forms após fechá-los no meio da tentativa, gerenciando as configurações de salvamento automático e retomada automática."
---

Os testes do Google Forms requerem que duas configurações estejam alinhadas para o comportamento correto de retomada: a configuração de **salvamento automático** no Google Forms e a configuração de **retomada automática** no AutoProctor. A incompatibilidade dessas configurações causa comportamento inesperado para os candidatos.

{% hint style="info" %}
Duas configurações controlam a retomada de testes do Google Forms:
1. **Disable Autosave** no Google Forms — Controla se os rascunhos de respostas são salvos enquanto o candidato preenche o formulário.
2. **Enable Auto-resume** no AutoProctor — Controla se o AutoProctor carrega a tentativa anterior quando o candidato retorna ao link do teste.

Você deve configurar ambas as configurações juntas para o comportamento pretendido.
{% endhint %}

## Para Permitir a Retomada do Teste

Se você quer que os candidatos continuem de onde pararam após fechar o teste:

{% stepper %}
{% step %}
### Mantenha o salvamento automático ativado no Google Forms
Certifique-se de que o recurso **Disable Autosave** está **DESLIGADO** nas configurações do teste do Google Forms. Essa é a configuração padrão, então você só precisa verificar se ela não foi alterada.



![Configurações do teste do Google Forms mostrando Disable Autosave desligado, mantendo o salvamento automático ativo](images/settings/gforms-autosave-enabled.png)
{% endstep %}
{% step %}
### Ative a retomada automática no AutoProctor
Ative a configuração **Enable Auto-resume** nas configurações do teste do AutoProctor.



![Configurações do teste do AutoProctor mostrando Enable Auto-resume ativado](images/settings/gforms-autoresume-enabled.png)
{% endstep %}
{% endstepper %}

## Para Impedir a Retomada do Teste

Se você quer que cada visita ao link do teste crie uma nova tentativa em branco:

{% stepper %}
{% step %}
### Desative o salvamento automático no Google Forms
Ative o recurso **Disable Autosave** nas configurações do teste do Google Forms. Isso impede que o Google Forms salve rascunhos de respostas.



![Configurações do teste do Google Forms mostrando Disable Autosave ligado, desativando o salvamento automático](images/settings/gforms-autosave-disabled.png)
{% endstep %}
{% step %}
### Desative a retomada automática no AutoProctor
Desative a opção **Enable Auto-resume** nas configurações do teste do AutoProctor.



![Configurações do teste do AutoProctor mostrando Enable Auto-resume desativado](images/settings/gforms-autoresume-disabled.png)
{% endstep %}
{% endstepper %}

## Referência de Combinação de Configurações

| Disable Autosave (Google Forms) | Enable Auto-resume (AutoProctor) | Resultado |
|---|---|---|
| OFF (padrão) | ON (padrão) | Os candidatos retomam de onde pararam |
| ON | OFF | Cada visita inicia uma tentativa nova e em branco |
| OFF | OFF | Nova tentativa é carregada, mas o Google Forms pode mostrar respostas previamente salvas — confuso para os candidatos |
| ON | ON | O AutoProctor tenta retomar, mas o Google Forms não tem rascunho salvo — o candidato vê um formulário em branco com tempo reduzido |

{% hint style="warning" %}
Se as duas configurações estiverem incompatíveis (por exemplo, salvamento automático está ativado mas retomada automática está desativada), os candidatos podem experimentar comportamento inesperado, como ver um formulário parcialmente preenchido em uma nova tentativa ou perder o progresso salvo. Sempre configure ambas as configurações de forma alinhada.
{% endhint %}

## Configurações Padrão

O Google Forms tem o salvamento automático ativado por padrão, e a configuração padrão correspondente do AutoProctor permite retomar tentativas de teste não enviadas. Isso significa que os testes são retomados por padrão, a menos que você altere explicitamente uma das configurações.

## Recursos Relacionados

- [Retomar Tentativas de Teste](tests-results/create/resuming-test-attempts.md) — Comportamento geral de retomada em todos os tipos de teste
- [Tentativas Máximas](tests-results/access-limits/maximum-attempts.md) — Configure quantas tentativas os candidatos podem realizar
- [Testes Não Enviados](tests-results/results/unsubmitted-tests.md) — Veja testes iniciados mas não enviados
- [Configurações de Tempo](tests-results/create/timer-settings.md) — Configure a duração do teste e janelas de tempo
- [Boas Práticas para Criadores de Testes](understanding/getting-started/best-practices-for-teachers.md) — Dicas para uma administração de testes tranquila

---
title: "Retomar Tentativas de Teste"
description: "Entenda como o AutoProctor gerencia a retomada de testes quando os candidatos se desconectam, fecham o navegador ou saem de um teste no meio da tentativa."
---

Quando um candidato sai de um teste no meio da tentativa — seja por uma falha do navegador, problema de rede ou fechamento acidental — o AutoProctor determina se deve retomar a tentativa anterior ou criar uma nova. O comportamento depende do tipo de teste e das suas configurações.

## Comportamento de Retomada por Tipo de Teste

| Tipo de Teste | Comportamento de Retomada | Detalhes |
|---|---|---|
| Socratease Quiz | Sempre retoma | Carrega as respostas anteriores automaticamente; os candidatos devem completar a tentativa existente antes de iniciar uma nova |
| Microsoft Forms | Nunca retoma | Cria uma nova tentativa a cada vez devido a limitações da plataforma |
| Google Forms | Configurável | Controlado pelo botão **Enable Auto Resume** e pela configuração de salvamento automático do Google Forms |
| Testes IFrame | Configurável | Controlado pelo botão **Enable Auto Resume** |

## Configurando o Recurso de Retomada

Para Google Forms e testes IFrame, você controla o comportamento de retomada pelo botão **Enable Auto Resume** nas configurações do teste.

{% stepper %}
{% step %}
### Abra as configurações do teste
Navegue até o teste no [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/) e clique no botão **Settings**.


{% endstep %}
{% step %}
### Ative o Enable Auto Resume
Encontre e ative ou desative a opção **Enable Auto Resume**.



![Botão Enable Auto Resume nas configurações de teste do AutoProctor](images/settings/enable-auto-resume.png)
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Para Google Forms, você também deve manter a configuração de **Save Draft** (salvamento automático) ativada no próprio Google Forms para que a retomada funcione corretamente. Consulte [Retomar Testes do Google Forms](tests-results/create/resuming-google-forms.md) para configuração detalhada.
{% endhint %}

## Como a Retomada Funciona

Quando um candidato retorna ao link do teste após se desconectar:

- **Se a retomada está ativada**: O AutoProctor carrega a tentativa anterior com todas as respostas anteriores intactas. O candidato continua de onde parou.
- **Se a retomada está desativada**: O AutoProctor cria uma nova tentativa em branco. Todas as respostas anteriores da tentativa interrompida são perdidas (embora a tentativa incompleta ainda apareça nos seus resultados).

## Como os Temporizadores Interagem com a Retomada

Se você tem [configurações de tempo](tests-results/create/timer-settings.md) definidas, elas afetam como a retomada funciona.

### Duração do Teste

O tempo restante da tentativa original é transferido. Por exemplo, se um candidato inicia um teste de 60 minutos às 10:00 e se desconecta às 10:30, retomar às 10:50 dá a ele apenas 10 minutos restantes. Quando a duração total expira (11:00), o teste não pode mais ser retomado.

### Cannot Start Before / Cannot Start After

Essas restrições se aplicam ao horário de início original, não ao horário de reconexão. Um candidato que iniciou antes do prazo pode retomar depois dele, desde que a duração do teste não tenha expirado.

### Must Submit By

Esse prazo é aplicado rigorosamente no momento da reconexão. Se o prazo de **Must Submit By** já passou antes de o candidato tentar retomar, o teste não é carregado — mesmo que o candidato tenha iniciado originalmente antes do prazo.

{% hint style="warning" %}
O prazo **Must Submit By** sobrepõe todas as outras configurações de tempo no momento da retomada. Se esse prazo já passou, o candidato não pode retomar independentemente do tempo restante de teste.
{% endhint %}

## Recursos Relacionados

- [Retomar Testes do Google Forms](tests-results/create/resuming-google-forms.md) — Configuração detalhada de retomada no Google Forms
- [Tentativas Máximas](tests-results/access-limits/maximum-attempts.md) — Como os limites de tentativas interagem com a retomada
- [Testes Não Enviados](tests-results/results/unsubmitted-tests.md) — Veja detalhes de testes iniciados mas não enviados
- [Configurações de Tempo](tests-results/create/timer-settings.md) — Configure a duração do teste, prazos e janelas de tempo
- [Boas Práticas para Criadores de Testes](understanding/getting-started/best-practices-for-teachers.md) — Dicas para uma administração de testes tranquila

---
title: "Supervisão Avançada"
description: "Configure verificação de identidade, detecção de impostor, supervisão em 360 graus e gravação de sessão para proteção avançada contra fraudes."
---

A Supervisão Avançada adiciona recursos avançados de verificação de identidade e monitoramento além da supervisão padrão. Esses recursos ajudam a prevenir a personificação, detectar ferramentas de IA e criar um registro completo de cada tentativa de teste.

![Painel de configurações de supervisão avançada](images/creating-tests/enhanced-proctoring.png)

{% hint style="info" %}
Cada recurso de supervisão avançada requer **4 créditos adicionais por tentativa**. Se você ativar múltiplos recursos avançados, o custo de créditos é cumulativo. Por exemplo, ativar a Verificação de Identidade e a Gravação de Sessão custa 8 créditos adicionais por tentativa de candidato.
{% endhint %}

## Recursos Disponíveis

### Verificação de Identidade

A Verificação de Identidade confirma a identidade do candidato comparando seu documento de identidade enviado com a foto do teste e o nome inserido.

{% stepper %}
{% step %}
### Ativar a Verificação de Identidade
Ative a opção **ID Card Verification** na seção de Supervisão Avançada das configurações do teste.
{% endstep %}
{% step %}
### O candidato faz upload do documento
Ao iniciar o teste, o candidato é solicitado a fazer upload de uma foto do seu documento de identidade. Documentos aceitos incluem carteiras de candidato, passaportes, carteiras de motorista e documentos emitidos pelo governo.
{% endstep %}
{% step %}
### O AutoProctor verifica a identidade
O sistema compara a foto e o nome no documento de identidade com a Foto Antes do Início do Teste e o nome que o candidato inseriu na plataforma.
{% endstep %}
{% endstepper %}

![Tela de verificação de identidade antes de iniciar o teste](images/taking-tests/id-verification.png)
*Tela de verificação de identidade antes de iniciar o teste*

{% hint style="info" %}
A **Foto Antes do Início do Teste** deve estar ativada nas configurações básicas de supervisão para que a Verificação de Identidade funcione efetivamente.
{% endhint %}

### Detecção de Impostor

A Detecção de Impostor monitora se alguém diferente do candidato original tenta ou continua o teste. O AutoProctor compara fotos periódicas tiradas durante o teste com a foto inicial para detectar mudanças de rosto.

![Evidência de impostor no relatório](images/taking-tests/impersonation-detected.png)
*Evidência de impostor no relatório*

### Dispositivo Auxiliar (Supervisão em 360°)

O recurso de Dispositivo Auxiliar permite a supervisão em 360 graus emparelhando o celular do candidato com o laptop. Isso fornece um ângulo de câmera secundário que captura o ambiente físico do candidato.

{% stepper %}
{% step %}
### Ativar o Dispositivo Auxiliar
Ative a opção **Auxiliary Device** nas configurações de Supervisão Avançada.
{% endstep %}
{% step %}
### O candidato emparelha o celular
Quando o teste começa, o candidato escaneia um código QR na tela do laptop usando a câmera do celular. Isso emparelha os dois dispositivos.

![Tela de emparelhamento do dispositivo auxiliar antes de iniciar o teste](images/taking-tests/aux-device.png)
*Tela de emparelhamento do dispositivo auxiliar antes de iniciar o teste*
{% endstep %}
{% step %}
### O celular fornece monitoramento secundário
A câmera do celular captura a mesa, o ambiente e a tela do candidato de um ângulo diferente. Isso também ajuda a detectar ferramentas de IA que exibem respostas como sobreposições na tela.
{% endstep %}
{% endstepper %}

![Capturas de evidência do dispositivo auxiliar](images/taking-tests/aux-device-evidence.png)
*Capturas de evidência do dispositivo auxiliar*

### Gravação de Sessão

A Gravação de Sessão captura um registro completo da atividade na tela do candidato durante todo o teste, incluindo cliques do mouse e entrada do teclado. Isso cria uma linha do tempo revisável de toda a tentativa de teste.


[Experimente a demonstração de supervisão avançada](https://www.autoproctor.co/tests/aux-demo/) para ver esses recursos em ação antes de ativá-los no seu teste.

## Resumo de Custos de Créditos

| Recurso | Créditos por Tentativa |
|---|---|
| Verificação de Identidade | 4 |
| Detecção de Impostor | 4 |
| Dispositivo Auxiliar (360°) | 4 |
| Gravação de Sessão | 4 |
| Todos os 4 recursos combinados | 12 (25% de desconto no pacote) |

## Recursos Relacionados

- [Configurações de Supervisão](tests-results/create/proctoring-settings.md) — Opções básicas de supervisão (câmera, microfone, troca de aba)
- [Trust Score](understanding/how-proctoring-works/trust-score.md) — Como os dados de supervisão avançada afetam o Trust Score
- [Resultados de Supervisão](tests-results/results/proctoring-results.md) — Revisando os resultados de supervisão avançada
- [Envios Individuais](tests-results/results/individual-submissions.md) — Visualizando dados detalhados de cada candidato
- [Pagamentos e Créditos](pricing-account/plans-credits/payments-and-credits.md) — Entendendo o uso e a compra de créditos
- [Recursos Elite](pricing-account/plans-credits/elite-features.md) — Visão geral dos recursos Premium e Elite

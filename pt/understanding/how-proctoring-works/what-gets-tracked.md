---
title: "O Que é Monitorado Durante a Supervisão"
description: "Conheça as fontes de dados, as capacidades de detecção e o registro de evidências disponíveis no sistema de supervisão do AutoProctor."
---

O AutoProctor monitora os candidatos em tempo real usando inteligência artificial no dispositivo e captura evidências apenas quando detecta uma infração. Isso significa que você revisa apenas os incidentes sinalizados, em vez de horas de gravação.

<Frame caption="Um relatório de supervisão de exemplo mostrando a Pontuação de Confiança, a contagem de infrações e os eventos sinalizados com evidências">
  ![Relatório de supervisão de exemplo](../../images/getting-started/sample-proctoring-report.png)
</Frame>

[Veja resultados de supervisão de exemplo](https://www.autoproctor.co/sample-dashboard/) para explorar um relatório real.

## Fontes de Dados

O AutoProctor pode acessar as seguintes fontes no dispositivo do candidato:

| Fonte | O Que Faz |
|---|---|
| **Câmera** | Monitora o rosto e o ambiente do candidato |
| **Microfone** | Detecta ruído de fundo e sinais de áudio |
| **Compartilhamento de tela** | Captura a atividade da tela durante o teste |
| **Câmera de dispositivo auxiliar** | Monitora por meio de um dispositivo secundário emparelhado (por exemplo, celular) |

{% hint style="info" %}
Quais fontes o AutoProctor acessa depende inteiramente de como você configura cada teste. Você ativa ou desativa cada fonte nas suas [configurações de supervisão](tests-results/create/proctoring-settings.md).
{% endhint %}

## O Que o AutoProctor Detecta e Registra

Ao contrário das plataformas de supervisão tradicionais que gravam sessões completas de vídeo e áudio, o AutoProctor detecta infrações e mostra a você evidências apenas dessas infrações — de modo que você não precise dedicar horas revisando a tentativa de cada candidato.

| Recurso de Detecção | O Que Faz |
|---|---|
| **Detecção de áudio de fundo** | Registra ruído e sinais de áudio do microfone |
| **Detecção facial** | Captura fotos quando nenhum rosto ou múltiplos rostos aparecem na câmera |
| **Troca de aba/aplicativo** | Captura capturas de tela quando os candidatos trocam de aba ou aplicativo |
| **Fotos aleatórias** | Tira fotos em intervalos aleatórios durante o exame |
| **Detecção de múltiplos monitores** | Identifica quando telas adicionais estão conectadas ao dispositivo |
| **Captura facial pré-teste** | Tira uma foto do rosto do candidato antes do início do teste |
| **Modo de tela cheia obrigatório** | Garante que o teste seja executado em modo de tela cheia e sinaliza saídas |
| **Registro de ações da sessão** | Registra cliques do mouse e atividade do teclado durante todo o teste |
| **Emparelhamento de dispositivo auxiliar** | Monitora por meio de um celular emparelhado para detectar o uso do teclado, garantindo que os candidatos não usem ChatGPT ou outras ferramentas para trapacear |

{% hint style="info" %}
Todas as funções de monitoramento são configuráveis por teste. Ative apenas o que você precisa nas suas [configurações de supervisão](tests-results/create/proctoring-settings.md).
{% endhint %}

## Como Configurar o Monitoramento

{% stepper %}
{% step %}
### Abra as configurações do teste
Acesse seu [painel do AutoProctor](https://www.autoproctor.co/test-admin/home/), selecione um teste e clique em **Settings**.


{% endstep %}
{% step %}
### Navegue até as Configurações de Supervisão
Clique na aba **Proctoring Settings** para ver todas as opções de monitoramento disponíveis.


{% endstep %}
{% step %}
### Ative os recursos necessários
Ative ou desative cada recurso de monitoramento de acordo com suas necessidades. Por exemplo, você pode ativar o monitoramento por câmera e a detecção de troca de aba, mas deixar o monitoramento por microfone desativado.


{% endstep %}
{% step %}
### Salve suas configurações
Clique em **Save** para aplicar suas alterações. Essas configurações entram em vigor imediatamente para todas as tentativas futuras de teste.
{% endstep %}
{% endstepper %}

{% embed url="../../videos/getting-started/configure-proctor-settings.mp4" %}
Como configurar as configurações de supervisão no AutoProctor
{% endembed %}

{% hint style="warning" %}
Ativar mais recursos de monitoramento aumenta a carga de processamento no dispositivo do candidato. Se seus candidatos usam hardware mais antigo, considere ativar apenas os recursos mais necessários. Consulte [Compatibilidade de Dispositivos](understanding/getting-started/device-compatibility.md) para os requisitos mínimos.
{% endhint %}

## Recursos Relacionados

- [Trust Score](understanding/how-proctoring-works/trust-score.md) — Como o AutoProctor classifica a integridade do candidato
- [Configurações de Supervisão](tests-results/create/proctoring-settings.md) — Configure quais recursos de supervisão ativar
- [Supervisão Avançada](tests-results/create/enhanced-proctoring.md) — Opções avançadas de monitoramento para maior segurança
- [Resultados de Supervisão](tests-results/results/proctoring-results.md) — Veja as evidências de infrações e os relatórios
- [Gravação de Vídeo](understanding/how-proctoring-works/video-recording.md) — Por que o AutoProctor não grava vídeo completo
- [Compatibilidade de Dispositivos](understanding/getting-started/device-compatibility.md) — Navegadores e dispositivos compatíveis

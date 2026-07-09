---
title: "Argumentos de Consulta do IFrame"
description: "Adicione parâmetros de consulta às URLs de iframe nas Configurações Avançadas do AutoProctor para personalizar o conteúdo incorporado."
---

Ao usar o provedor de questionários **IFrame/Other**, você pode adicionar parâmetros de consulta à URL do seu questionário incorporado através das **Configurações Avançadas** do AutoProctor. Isso permite personalizar como o conteúdo incorporado se comporta — por exemplo, forçando um idioma específico ou ativando o modo incorporado — sem modificar a URL original.

## Como Funciona

O AutoProctor constrói a URL final adicionando seus argumentos de consulta à URL original do questionário. Você fornece apenas os parâmetros; o AutoProctor adiciona o prefixo `?` automaticamente.

{% embed url="videos/settings/query-arguments.mp4" %}
Como usar argumentos de consulta nas Configurações Avançadas do AutoProctor
{% endembed %}

{% stepper %}
{% step %}
### Abra as Configurações Avançadas
Navegue até o seu teste e abra a seção **Advanced Settings**.
{% endstep %}
{% step %}
### Insira Seus Argumentos de Consulta
Digite seus parâmetros no campo **Query Arguments**. Use o formato `key1=val1&key2=val2`.
{% endstep %}
{% step %}
### Salve as Configurações
Salve as configurações do teste. O AutoProctor adicionará seus parâmetros à URL do questionário ao renderizar o iframe.
{% endstep %}
{% endstepper %}

### Exemplo

Se sua URL original é:

```
www.website.com
```

E você insere o seguinte no campo **Query Arguments**:

```
key1=val1&key2=val2
```

O AutoProctor renderiza o iframe como:

```
www.website.com?key1=val1&key2=val2
```

{% hint style="info" %}
Não inclua o prefixo `?` nos seus argumentos de consulta. O AutoProctor o adiciona automaticamente ao construir a URL.
{% endhint %}

## Parâmetros Comuns

| Parâmetro | Finalidade | Exemplo de Uso |
|---|---|---|
| `hl=en` | Definir o idioma para inglês | Renderizar um Google Form em inglês para candidatos internacionais |
| `hl=fr` | Definir o idioma para francês | Renderizar um Google Form em francês |
| `embedded=true` | Forçar o modo incorporado | Garantir que certas plataformas sejam exibidas corretamente dentro do iframe |

## Recursos Relacionados

- [Provedores de Questionários](tests-results/create/quiz-providers.md) — Todas as plataformas de questionários compatíveis
- [Configurações Avançadas](tests-results/create/advanced-settings.md) — Provedores de login, colaboradores e outras opções avançadas
- [Configurações de Tempo](tests-results/create/timer-settings.md) — Configure a duração do teste e janelas de tempo
- [Configurações de Supervisão](tests-results/create/proctoring-settings.md) — Opções de câmera, microfone e troca de aba

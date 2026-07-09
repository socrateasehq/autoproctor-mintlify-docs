---
title: "Modo de Visualización de Preguntas"
description: "Controle cómo se muestran las preguntas a los candidatos — todas a la vez, una por una con navegación o una por una sin navegación."
---

La configuración del Modo de Visualización de Preguntas controla cómo aparecen las preguntas para los participantes. Puede elegir entre tres opciones de visualización, cada una con diferentes implicaciones para la navegación, el tiempo y la seguridad del examen.

{% hint style="info" %}
Modo de Visualización de Preguntas es una función **Premium**. Consulte [Pagos y Créditos](pricing-account/plans-credits/payments-and-credits.md) para los detalles del plan.
{% endhint %}

## Modos de Visualización

![Panel de configuración del modo de visualización de preguntas mostrando las tres opciones disponibles](../../images/socratease/question-display-mode.png)
*Configuración del modo de visualización de preguntas en los ajustes del cuestionario*

### 1. Todas a la Vez (Estilo Google Forms)

Los candidatos ven todas las preguntas al mismo tiempo, una debajo de otra, como en un Google Form. El temporizador se aplica a la **prueba completa**. Los candidatos pueden desplazarse libremente entre las preguntas y responderlas en cualquier orden.

![Vista del candidato del modo todas a la vez mostrando todas las preguntas en una página](../../images/socratease/all-at-once.png)
*Modo todas a la vez*

### 2. Una por Una con Navegación (Estilo Typeform)

Los candidatos ven una pregunta a la vez y pueden navegar hacia adelante y hacia atrás entre las preguntas. El temporizador se aplica a la **prueba completa**, no a las preguntas individuales. Los candidatos pueden revisar y cambiar sus respuestas en cualquier momento antes de enviar.

![Vista del candidato del modo una por una con navegación mostrando una pregunta con botones Siguiente y Anterior](../../images/socratease/one-by-one-like-typeform.png)
*Una por una con navegación*

### 3. Una por Una sin Navegación

Los candidatos ven una pregunta a la vez. Una vez que envían una pregunta (al responderla u omitirla), **no pueden volver a ella**. El temporizador se establece **por pregunta**, no para toda la prueba.

![Vista del candidato del modo una por una sin navegación mostrando una pregunta con botones Enviar y Omitir](../../images/socratease/one-by-one.png)
*Una por una sin navegación*

## Diferencias Principales

| Característica | Todas a la Vez | Una por Una con Nav. | Una por Una sin Nav. |
|---|:---:|:---:|:---:|
| Alcance del temporizador | Prueba completa | Prueba completa | Por pregunta |
| Puede volver a preguntas anteriores | Sí | Sí | No |
| Instrucciones personalizadas | Sí | No | No |

## Cuándo Usar "Una por Una sin Navegación"

La opción sin navegación es especialmente útil para la seguridad del examen. Los candidatos solo pueden ver una pregunta a la vez por una duración limitada, lo que reduce significativamente la oportunidad de hacer trampa. Cada pregunta tiene su propio temporizador, por lo que los candidatos no pueden dedicar tiempo extra a preguntas difíciles apresurándose en las más fáciles.

## Cómo Cambia la Configuración del Temporizador

{% hint style="warning" %}
Cuando usa **una por una sin navegación**, ciertas configuraciones del temporizador a nivel de examen dejan de estar disponibles. El comportamiento del temporizador se traslada al nivel de la pregunta:

- **Duración**: Usted establece la duración por pregunta, no para todo el examen
- **Envío Automático**: Cada pregunta se envía automáticamente cuando su temporizador individual expira
- **Debe Enviar Antes**: Esta configuración a nivel de examen se reemplaza por **No Puede Iniciar Después** a nivel de examen
{% endhint %}

Para más información sobre la configuración del temporizador, consulte [Configuración del Temporizador](tests-results/create/timer-settings.md).

## Cómo Establecer el Modo de Visualización

{% embed url="../../videos/socratease/question-display-mode.mp4" %}
Cómo configurar el modo de visualización de preguntas
{% endembed %}

{% stepper %}
{% step %}
### Abra Su Cuestionario
Abra el Cuestionario Socratease que desea configurar desde su [panel de control de AutoProctor](https://www.autoproctor.co/test-admin/home/).
{% endstep %}
{% step %}
### Vaya a Configuración
Haga clic en el ícono de **Configuración** (engranaje) en la barra de herramientas del editor del cuestionario.
{% endstep %}
{% step %}
### Seleccione el Modo de Visualización
Elija su modo de visualización preferido en el menú desplegable de **Modo de Visualización de Preguntas**. El valor predeterminado es "Todas a la vez".


{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [Configuración del Cuestionario](socratease/settings/quiz-settings.md) — Todas las opciones de configuración de cuestionarios Socratease
- [Configuración del Temporizador](tests-results/create/timer-settings.md) — Configure temporizadores a nivel de examen y de pregunta
- [Cómo Crear un Cuestionario Socratease](socratease/create-questions/creating-a-quiz.md) — Guía de creación paso a paso
- [Mostrar Resultados a los Candidatos](socratease/settings/showing-results-to-candidates.md) — Controle la visibilidad de los resultados

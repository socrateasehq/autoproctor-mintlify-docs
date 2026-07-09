---
title: "Puntaje de Confianza"
description: "Comprenda cómo funciona el Puntaje de Confianza de AutoProctor, cómo se calcula y qué constituye un buen puntaje."
---

AutoProctor asigna un Puntaje de Confianza (0--100%) a cada informe de supervisión. El puntaje le brinda un resumen rápido de qué tan probable es que un candidato haya mantenido la integridad del examen, para que pueda enfocar su tiempo de revisión en los intentos que más lo necesitan.

![Visualización del Puntaje de Confianza mostrando un porcentaje en la parte superior de un informe de supervisión de AutoProctor](images/getting-started/trustscore.png)

Un Puntaje de Confianza más bajo significa que AutoProctor detectó más comportamiento sospechoso durante el examen.

{% hint style="warning" %}
Siempre revise la evidencia de respaldo antes de sacar conclusiones. **No** se base únicamente en el Puntaje de Confianza — revise las fotos de infracciones reales, las capturas de pantalla y las grabaciones de audio para determinar si ocurrió una conducta indebida.
{% endhint %}

## Cómo Se Calcula el Puntaje de Confianza

AutoProctor monitorea a los candidatos en tiempo real a través de múltiples canales (dependiendo de su [configuración de supervisión](tests-results/create/proctoring-settings.md)):

- Cámara
- Micrófono
- Actividad de pantalla

El algoritmo evalúa las infracciones basándose en tres factores:

| Factor | Cómo Afecta el Puntaje |
|---|---|
| **Tipo de infracción** | Diferentes infracciones tienen diferentes pesos. El cambio de pestaña impacta el puntaje más que la detección de ruido. |
| **Frecuencia de infracciones** | Más incidentes resultan en un puntaje más bajo. |
| **Duración de infracciones** | Infracciones prolongadas reducen el puntaje más significativamente que las breves. |


## ¿Qué Es un Buen Puntaje de Confianza?

Como pauta general, revise la evidencia de cualquier candidato con un Puntaje de Confianza **inferior al 85%**. Este umbral es para revisión, no como prueba de conducta indebida.

{% hint style="info" %}
Los factores ambientales pueden impactar significativamente la puntuación. Por ejemplo, un candidato en una habitación ruidosa cerca del tráfico podría recibir un Puntaje de Confianza del 0% incluso cuando no hubo trampa real. El micrófono capta el ruido ambiental y el sistema no siempre puede distinguir entre habla humana y sonido de fondo. Siempre verifique la evidencia antes de tomar una determinación.
{% endhint %}

## Cómo Revisar un Puntaje de Confianza

{% stepper %}
{% step %}
### Abra los resultados de su examen
Vaya a su [panel de control de AutoProctor](https://www.autoproctor.co/test-admin/home/), seleccione un examen y haga clic en **Resultados**. Verá una lista de todos los candidatos con sus Puntajes de Confianza.
{% endstep %}
{% step %}
### Identifique candidatos para revisión
Ordene por Puntaje de Confianza y concéntrese en los candidatos con puntuación **inferior al 85%**. Estos intentos son los más propensos a contener infracciones que vale la pena revisar.

{% embed url="videos/getting-started/trustscore-column.mp4" %}
Lista de resultados mostrando la columna de Puntaje de Confianza
{% endembed %}
{% endstep %}
{% step %}
### Revise la evidencia de infracciones
Haga clic en **Ver Informe** en la fila de un candidato para ver el desglose detallado: fotos señaladas, capturas de pantalla, clips de audio y una línea de tiempo de infracciones detectadas.


{% endstep %}
{% step %}
### Tome su determinación
Use la evidencia para decidir si las infracciones indican una conducta indebida real o son falsos positivos causados por factores ambientales.
{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [Qué Se Monitorea](understanding/how-proctoring-works/what-gets-tracked.md) — Todas las capacidades de monitoreo disponibles
- [Resultados de Supervisión](tests-results/results/proctoring-results.md) — Cómo ver la evidencia de infracciones y los informes
- [Acceder a Respuestas y Entregas del Candidato](tests-results/results/individual-submissions.md) — Revisión detallada del informe de un candidato individual
- [No Se Detecta Rostro o Se Detectan Múltiples Rostros](tests-results/issues/no-face-or-multiple-faces.md) — Por qué la detección facial puede generar falsos positivos
- [Infracción Falsa de Cambio de Aplicación](tests-results/issues/false-app-switch.md) — Comprenda las señalizaciones de infracciones falsas
- [Mejores Prácticas para Creadores de Exámenes](understanding/getting-started/best-practices-for-teachers.md) — Consejos para realizar exámenes supervisados eficaces

---
title: "Sin Rostro o Múltiples Rostros Detectados Incorrectamente"
description: "Comprenda por qué la IA de AutoProctor puede reportar incorrectamente infracciones de detección facial y cómo interpretar correctamente estos resultados en los informes de supervisión."
---

AutoProctor utiliza IA para la detección facial, y la IA no es 100% precisa. Es posible que vea infracciones de "Sin rostro detectado" o "Múltiples rostros detectados" en un informe incluso cuando la foto de evidencia muestra claramente un solo rostro.

## Por Qué Sucede Esto

Los modelos de IA de AutoProctor están entrenados con miles de rostros, pero pueden fallar en escenarios que difieren de sus datos de entrenamiento. Las tres causas más comunes de detección facial incorrecta son:

| Causa | Descripción |
|---|---|
| Fondos complejos | Los fondos recargados o coloridos pueden confundir a la IA, haciendo que detecte rostros adicionales o que no detecte el real |
| Posición de la cabeza | Los candidatos que miran hacia otro lado, miran hacia abajo o inclinan la cabeza pueden causar que la IA no detecte su rostro |
| Lentes con reflejos | Los lentes que reflejan la luz u oscurecen los ojos dificultan que el sistema de detección identifique un rostro |

## Cómo Interpretar Estas Infracciones

AutoProctor proporciona fotos de evidencia junto con cada infracción para que usted pueda verificar independientemente la determinación de la IA. Al revisar las infracciones de detección facial:

{% stepper %}
{% step %}
### Revise la foto de evidencia
Mire la foto asociada con la infracción. ¿Realmente muestra que no hay rostro, múltiples rostros, o la IA claramente se equivocó?
{% endstep %}
{% step %}
### Observe el patrón
Una sola detección incorrecta entre muchas correctas es probablemente un falso positivo. Múltiples detecciones consecutivas pueden justificar una revisión más detallada.
{% endstep %}
{% step %}
### Considere el contexto
La iluminación deficiente, los ángulos inusuales o los fondos recargados explican la mayoría de las detecciones falsas. Tenga en cuenta el entorno de realización del examen antes de sacar conclusiones.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Siempre revise el informe completo y la evidencia proporcionada antes de concluir si un candidato cometió fraude. No se base únicamente en los Trust Scores automatizados -- úselos como guía junto con la evidencia fotográfica.
{% endhint %}

## Recursos Relacionados

- [Comprensión del Trust Score](understanding/how-proctoring-works/trust-score.md) -- Cómo se calculan los Trust Scores
- [Qué Se Monitorea](understanding/how-proctoring-works/what-gets-tracked.md) -- Todos los eventos que AutoProctor supervisa
- [Resultados de Supervisión](tests-results/results/proctoring-results.md) -- Cómo revisar los informes de supervisión
- [Evidencia de Infracciones Faltante](tests-results/issues/missing-violation-evidence.md) -- Por qué algunas infracciones carecen de fotos de evidencia
- [Falso 'Cambió a Otra Aplicación'](tests-results/issues/false-app-switch.md) -- Otro escenario común de falso positivo
- [Contáctenos](pricing-account/support/contact-us.md) -- Comuníquese si necesita más ayuda

---
title: "Imágenes y Grabaciones Faltantes en el Informe"
description: "Comprenda por qué las imágenes o grabaciones de audio pueden no aparecer en el informe del examen de un candidato a pesar de que las infracciones están listadas, y cómo solucionarlo."
---

Si puede ver infracciones listadas en el informe del examen de un candidato pero no puede ver la evidencia de respaldo (imágenes o grabaciones de audio), existen dos escenarios posibles, cada uno con una causa y resolución diferente.

## Escenario 1: No Hay Imágenes ni Grabaciones en Absoluto

Si no aparecen imágenes ni grabaciones a pesar de que las infracciones están listadas, es probable que la función de grabación de evidencia haya sido desactivada en la configuración de su examen.

{% stepper %}
{% step %}
### Verifique la configuración de su examen
Navegue a la configuración de supervisión de su examen en el [panel de AutoProctor](https://www.autoproctor.co/test-admin/home/) y verifique que la grabación de evidencia esté activada. Consulte [Configuración de Supervisión](tests-results/create/proctoring-settings.md) para obtener detalles sobre cada opción.
{% endstep %}
{% step %}
### Active la grabación de evidencia para futuros exámenes
Si la grabación de evidencia estaba desactivada, actívela para futuros exámenes. Tenga en cuenta que este cambio no agregará retroactivamente evidencia a exámenes que ya se hayan realizado.
{% endstep %}
{% endstepper %}


## Escenario 2: Algunas Infracciones Tienen Evidencia, Otras No

Si algunas infracciones muestran archivos de evidencia mientras otras no, este es el comportamiento esperado. AutoProctor almacena un número fijo (aproximadamente 20) de imágenes y archivos de audio por intento de examen. Cuando las infracciones exceden este límite, no todas las infracciones tendrán un archivo de evidencia asociado.

| Lo Que Ve | Lo Que Significa |
|---|---|
| No hay archivos de evidencia en absoluto | Es probable que la grabación de evidencia esté desactivada en la configuración del examen |
| Algunas infracciones tienen archivos, otras no | Límite de almacenamiento alcanzado -- comportamiento normal |

{% hint style="warning" %}
**Todas las infracciones se registran y afectan el Trust Score**, incluso cuando los archivos de evidencia no se almacenan para su visualización. Los archivos de evidencia son un subconjunto -- existen para que usted pueda revisar lo que sucedió, pero el cálculo del Trust Score considera cada infracción detectada independientemente de si la evidencia fue almacenada.
{% endhint %}

## Recursos Relacionados

- [Configuración de Supervisión](tests-results/create/proctoring-settings.md) -- Configure el almacenamiento de evidencia y las opciones de supervisión
- [Evidencia de Infracciones Faltante](tests-results/issues/missing-violation-evidence.md) -- Explicación detallada de los límites de almacenamiento de evidencia
- [Fotos Aleatorias Faltantes](tests-results/issues/missing-random-photos.md) -- Por qué las fotos aleatorias pueden estar ausentes
- [Resultados de Supervisión](tests-results/results/proctoring-results.md) -- Cómo revisar los informes de supervisión
- [Comprensión del Trust Score](understanding/how-proctoring-works/trust-score.md) -- Cómo se calculan los Trust Scores
- [Contáctenos](pricing-account/support/contact-us.md) -- Comuníquese si necesita más ayuda

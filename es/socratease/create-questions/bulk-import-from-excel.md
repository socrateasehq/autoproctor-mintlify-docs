---
title: "Importación Masiva de Preguntas desde Excel"
description: "Importe preguntas de opción múltiple desde un archivo Excel a su cuestionario Socratease."
---

La función de Importación Masiva le permite importar preguntas de opción múltiple desde un archivo Excel a los Cuestionarios Socratease. Esto ahorra un tiempo significativo cuando tiene muchas preguntas en formato Excel o Word existente, o cuando varias personas colaboran en un gran conjunto de preguntas.

{% hint style="info" %}
La Importación Masiva está disponible únicamente para clientes del plan **Elite**. Consulte [Funciones Elite](pricing-account/plans-credits/elite-features.md) para más detalles.
{% endhint %}

## Cómo Importar Preguntas

{% embed url="videos/socratease/import-from-excel.mp4" %}
Cómo importar preguntas desde Excel a Socratease
{% endembed %}

{% stepper %}
{% step %}
### Descargue la Plantilla
Abra su cuestionario en el editor de Socratease y descargue la plantilla de Excel. Esta plantilla contiene los encabezados de columna y el formato requeridos.


{% endstep %}
{% step %}
### Agregue Preguntas al Archivo Excel
Complete la plantilla con sus preguntas, opciones de respuesta e indicadores de respuesta correcta. Consulte la referencia de columnas a continuación para detalles sobre cada campo.


{% endstep %}
{% step %}
### Cargue el Archivo Excel
Cargue el archivo Excel completado en su cuestionario. Las preguntas se importan automáticamente y aparecen en su editor de cuestionarios.


{% endstep %}
{% endstepper %}

## Referencia de Columnas de la Plantilla Excel

| Columna | Obligatoria | Descripción |
|---|:---:|---|
| **Question Type** | Sí | `MCQ` para una sola respuesta correcta, o `MCA` para múltiples respuestas correctas |
| **Question** | Sí | El texto de la pregunta |
| **Opt1 -- Opt5** | No | Opciones de respuesta. Use solo las necesarias (por ejemplo, si tiene 3 opciones, complete Opt1, Opt2, Opt3 y deje Opt4 y Opt5 en blanco) |
| **CorrectAnsInd** | Sí | Para MCQ: un solo número indicando la opción correcta (por ejemplo, `2` para Opt2). Para MCA: números separados por comas sin espacios (por ejemplo, `2,3` para Opt2 y Opt3) |
| **Markdown** | No | Ingrese `1` para formatear el texto de la pregunta como Markdown |
| **Points** | No | Valor en puntos por una respuesta correcta |
| **Time (seconds)** | No | Límite de tiempo por pregunta, en segundos |
| **Image** | No | Una URL directa a un archivo de imagen (.jpg, .png, etc.) para mostrar junto con la pregunta |

{% hint style="warning" %}
La columna **Image** requiere una URL directa al archivo de imagen. Los enlaces de uso compartido de Google Drive **no** son compatibles. Use un enlace directo que termine en una extensión de archivo como `.jpg` o `.png`.
{% endhint %}

## Consejos para una Importación Exitosa

- Los campos marcados con **Obligatoria: Sí** deben completarse para cada pregunta.
- Puede dejar las columnas opcionales en blanco si no son necesarias.
- Asegúrese de que los encabezados de columna coincidan exactamente con la plantilla — no renombre ni reordene las columnas.
- Para preguntas MCA, separe los números de respuesta correcta con una coma y **sin espacio** (por ejemplo, `2,3` no `2, 3`).
- Si importa una gran cantidad de preguntas, considere dividirlas en lotes más pequeños para facilitar la resolución de problemas.

{% hint style="info" %}
La Importación Masiva actualmente admite solo los tipos de preguntas **MCQ** y **MCA**. Para otros tipos de preguntas, agréguelas manualmente a través del editor del cuestionario. Consulte [Tipos de Preguntas](socratease/create-questions/question-types.md) para la lista completa de formatos disponibles.
{% endhint %}

## Recursos Relacionados

- [Tipos de Preguntas](socratease/create-questions/question-types.md) — Todos los formatos de preguntas disponibles
- [Bancos de Preguntas](socratease/create-questions/question-banks.md) — Cree conjuntos aleatorios de preguntas a partir de sus preguntas importadas
- [Configuración del Cuestionario](socratease/settings/quiz-settings.md) — Configure el comportamiento de su cuestionario
- [Modo de Visualización de Preguntas](socratease/settings/question-display-mode.md) — Controle cómo aparecen las preguntas para los candidatos
- [Funciones Elite](pricing-account/plans-credits/elite-features.md) — Conozca las capacidades del plan Elite

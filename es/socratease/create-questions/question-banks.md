---
title: "Bancos de Preguntas"
description: "Cree grandes conjuntos de preguntas y ofrezca subconjuntos aleatorios a los candidatos utilizando los Bancos de Preguntas."
---

Los Bancos de Preguntas le permiten crear grandes conjuntos de preguntas y ofrecer un subconjunto aleatorio a cada candidato. Cada candidato recibe una combinación diferente de preguntas, reduciendo la posibilidad de fraude mientras se mantiene una estructura de evaluación consistente.

{% hint style="info" %}
Los Bancos de Preguntas son una función del plan **Elite**. Necesita una suscripción Elite para crear y usar Bancos de Preguntas y Cuestionarios de Bancos de Preguntas. Consulte [Funciones Elite](pricing-account/plans-credits/elite-features.md) para más detalles.
{% endhint %}

## ¿Qué Es un Banco de Preguntas?

Un Banco de Preguntas (BP) es una colección de preguntas organizadas por materia o tema. Cada pregunta en el banco puede tener un valor de puntos y un nivel de dificultad diferente. Cuando los candidatos realizan un examen, reciben un subconjunto seleccionado aleatoriamente del banco en lugar del conjunto completo de preguntas.


![Vista general del Banco de Preguntas mostrando una lista de preguntas organizadas por tema y dificultad](../../images/socratease/question-bank-overview.png)

### Ejemplo: Exámenes de Física y Química

Imagine que tiene dos Bancos de Preguntas:
- **Banco de Preguntas de Física** — 100 preguntas de varios niveles de dificultad
- **Banco de Preguntas de Química** — 100 preguntas de varios niveles de dificultad

Puede crear diferentes cuestionarios que extraigan de estos bancos con diferentes ponderaciones:

| Cuestionario | Preguntas de Física | Preguntas de Química | Total |
|---|---|---|---|
| Cuestionario de Especialidad en Física | 40 preguntas (2 puntos cada una) | 10 preguntas (1 punto cada una) | 50 preguntas |
| Cuestionario de Especialidad en Química | 10 preguntas (1 punto cada una) | 40 preguntas (2 puntos cada una) | 50 preguntas |

Cada candidato recibe un subconjunto aleatorio diferente de preguntas de los respectivos bancos, pero la estructura general (número de preguntas, puntos, distribución de dificultad) se mantiene consistente entre todos los candidatos.

## Cuestionarios de Bancos de Preguntas (CBP)

{% hint style="warning" %}
Los candidatos no pueden realizar un Banco de Preguntas directamente. Debe crear un Cuestionario de Banco de Preguntas y agregarlo a un examen de AutoProctor para que los candidatos lo realicen.
{% endhint %}

![Vista general de los Cuestionarios de Banco de Preguntas mostrando CBPs creados con conteos de respuestas](../../images/socratease/question-bank-quiz-overview.png)
*Vista general de los Cuestionarios de Banco de Preguntas creados*

Un Cuestionario de Banco de Preguntas especifica:
- De qué Bancos de Preguntas se extraen las preguntas
- Cuántas preguntas incluir de cada banco
- Los niveles de dificultad a incluir
- Los valores de puntos para cada nivel de dificultad

Puede combinar múltiples Bancos de Preguntas en un solo CBP, o usar un banco para suministrar preguntas en varios niveles de dificultad.

## Cómo Crear un Cuestionario de Banco de Preguntas

{% embed url="../../videos/socratease/add-qbq.mp4" %}
Cómo crear un Cuestionario de Banco de Preguntas
{% endembed %}

{% stepper %}
{% step %}
### Cree un Banco de Preguntas
Navegue a la sección de Bancos de Preguntas en AutoProctor y cree un nuevo Banco de Preguntas. Agregue sus preguntas, asignando valores de puntos y niveles de dificultad a cada una.


{% endstep %}
{% step %}
### Cree un Cuestionario de Banco de Preguntas
Cree un nuevo Cuestionario de Banco de Preguntas (CBP). Seleccione de qué Bancos de Preguntas extraer, cuántas preguntas incluir y qué niveles de dificultad usar.


{% endstep %}
{% step %}
### Agréguelo a un Examen de AutoProctor
Agregue el CBP a un examen de AutoProctor. Comparta el enlace del examen con sus candidatos.


{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [Importación Masiva desde Excel](socratease/create-questions/bulk-import-from-excel.md) — Importe preguntas de forma masiva para llenar sus Bancos de Preguntas
- [Tipos de Preguntas](socratease/create-questions/question-types.md) — Formatos de preguntas disponibles para usar en los Bancos de Preguntas
- [Uso de Etiquetas](socratease/settings/using-tags.md) — Organice preguntas con etiquetas para filtrar y agrupar
- [Configuración del Cuestionario](socratease/settings/quiz-settings.md) — Configure el comportamiento de su cuestionario
- [Funciones Elite](pricing-account/plans-credits/elite-features.md) — Conozca las capacidades del plan Elite

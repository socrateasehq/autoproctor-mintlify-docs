---
title: "Funciones del Plan Elite"
description: "Explore las funciones exclusivas disponibles únicamente en el plan Elite de AutoProctor, incluyendo acceso a la API, bancos de preguntas y tipos de preguntas avanzados."
---

El plan Elite es el nivel con más funciones de AutoProctor. Incluye todo lo que ofrecen los planes Standard y Premium, además de varias capacidades exclusivas diseñadas para flujos de trabajo de evaluación avanzados.

{% hint style="warning" %}
Estas funciones están disponibles **únicamente** en el plan Elite. No tendrá acceso a ellas en la Prueba gratuita ni en los planes Standard o Premium.
{% endhint %}

## Funciones Exclusivas del Plan Elite

Como se muestra en la [Página de Precios](https://www.autoproctor.co/pricing/), AutoProctor ofrece tres niveles de suscripción: **Standard**, **Premium** y **Elite**. Las siguientes funciones son exclusivas del plan Elite.

### Acceso a API/SDK

Si ya tiene su propia plataforma de cuestionarios o evaluaciones y desea agregar supervisión, puede integrar AutoProctor utilizando el SDK de JavaScript. Esto le permite incorporar la supervisión directamente en su flujo de trabajo existente sin requerir que los candidatos utilicen una plataforma separada.


### Clonación de Cuestionarios

Puede **duplicar Cuestionarios de Socratease con un solo clic**. Esto es especialmente útil cuando necesita crear varios cuestionarios que comparten una estructura similar pero difieren en preguntas o configuraciones específicas.

<Frame caption="Cómo clonar un cuestionario">
  <iframe className="w-full rounded-xl" style={{aspectRatio: "16/9"}} src="https://www.youtube.com/embed/1gAEoe2Oy3E?rel=0" title="Cómo clonar un cuestionario" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>
</Frame>

### URL Única por Candidato

Genere un enlace de examen único para cada candidato, de modo que un solo enlace no pueda reenviarse a destinatarios no deseados. Consulte [URL Única por Candidato](tests-results/create/advanced-settings#unique-url-per-candidate-elite.md) para la configuración.

### Instrucciones Adicionales

Agregue instrucciones personalizadas a la página de instrucciones del candidato — útil para compartir reglas específicas, contexto o pautas antes de que comience el examen. Consulte [Instrucciones Adicionales](tests-results/create/advanced-settings#additional-instructions-elite.md) para más detalles.

{% hint style="info" %}
Las siguientes funciones (Bancos de Preguntas, Más Tipos de Preguntas e Importar desde Excel) se aplican específicamente a los Cuestionarios de Socratease.
{% endhint %}

### Bancos de Preguntas

Los Bancos de Preguntas le permiten crear grandes grupos de preguntas y seleccionar subconjuntos de forma dinámica para cada candidato. Esto admite dos casos de uso principales:

| Caso de Uso | Ejemplo |
|---|---|
| **Subconjunto aleatorio por dificultad** | Seleccione 5 preguntas fáciles y 2 difíciles de opción múltiple de un grupo de 100 preguntas |
| **Combinar múltiples grupos** | Extraiga 3 preguntas de Física y 2 de Química de dos grupos separados de 100 cada uno |

Para una guía detallada, consulte [Bancos de Preguntas](socratease/create-questions/question-banks.md).

### Más Tipos de Preguntas

Los Cuestionarios de Socratease admiten muchos formatos de preguntas. Los siguientes son exclusivos del plan Elite:

<CardGroup cols={3}>
  <Card title="Entrada de Voz">
    Los candidatos se graban hablando la respuesta. Útil para evaluaciones de idiomas, exámenes orales y preguntas de tipo presentación.
  </Card>
  <Card title="Texto con Calificación Automática">
    Usted especifica la respuesta correcta al crear la pregunta. Si la entrega del candidato coincide exactamente, recibe el puntaje completo. De lo contrario, recibe 0 puntos.
  </Card>
  <Card title="Responder Cualquiera">
    Presente múltiples preguntas (por ejemplo, 5) y permita a los candidatos responder un subconjunto (por ejemplo, 3). Las cantidades son totalmente configurables.
  </Card>
</CardGroup>

Para la lista completa de tipos de preguntas, consulte [Tipos de Preguntas de Socratease](socratease/create-questions/question-types.md).

### Importar desde Excel

Usando la plantilla de Excel de AutoProctor, puede **cargar preguntas en masa** a un Cuestionario de Socratease. Esto es ideal para migrar conjuntos de preguntas existentes o crear evaluaciones extensas rápidamente. Consulte [Importación Masiva desde Excel](socratease/create-questions/bulk-import-from-excel.md) para instrucciones paso a paso.

## Recursos Relacionados

- [Pagos y Créditos Explicados](pricing-account/plans-credits/payments-and-credits.md) -- Comprenda los niveles de suscripción y los precios
- [¿Qué Es un Equipo?](pricing-account/billing-teams/teams.md) -- Comparta la facturación y colabore con los miembros del equipo
- [Tipos de Preguntas](socratease/create-questions/question-types.md) -- Todos los formatos de preguntas de Socratease disponibles
- [Bancos de Preguntas](socratease/create-questions/question-banks.md) -- Guía detallada para usar bancos de preguntas
- [Importación Masiva desde Excel](socratease/create-questions/bulk-import-from-excel.md) -- Instrucciones paso a paso para la importación desde Excel
- [¿Por Qué Socratease?](socratease/create-questions/why-socratease.md) -- Beneficios de usar Socratease sobre otras plataformas

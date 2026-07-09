---
title: "Mejores Prácticas para Creadores de Exámenes"
description: "Siga estas mejores prácticas al administrar exámenes supervisados en AutoProctor para garantizar una experiencia fluida para usted y sus candidatos."
---


## Lista de Verificación Previa al Examen

{% stepper %}
{% step %}
### Haga que los candidatos completen un examen de demostración
Comparta el enlace del examen de demostración correspondiente a su tipo de examen con los candidatos al menos **24 horas** antes del examen real. La demostración ayuda a los candidatos a comprender la plataforma, otorgar los permisos del navegador requeridos y confirmar que su dispositivo cumple con los requisitos técnicos.

Enlaces de demostración para cada tipo de examen:

- [Examen de Socratease](https://www.autoproctor.co/tests/bj0yv14Ufu/load/)
- [Examen de Google Forms](https://www.autoproctor.co/tests/GFICZZZA/load/)
- [Examen de Microsoft Forms](https://www.autoproctor.co/tests/gToT6XfaO1/instructions/)
- [Examen de otras plataformas de cuestionarios](https://www.autoproctor.co/tests/UAIJ2bcQ1i/instructions/)

{% hint style="info" %}
El examen de demostración no consume créditos de examen de su cuenta. Los candidatos pueden realizarlo tantas veces como necesiten.
{% endhint %}


{% endstep %}
{% step %}
### Verifique que su cuenta tenga créditos suficientes
Asegúrese de que su cuenta tenga suficientes intentos de examen disponibles antes del examen. Si los candidatos intentan cargar un examen y su cuenta no tiene créditos, no podrán continuar.

Consulte [Pagos y Créditos](pricing-account/plans-credits/payments-and-credits.md) para verificar su saldo y comprar más si es necesario.

![Panel de AutoProctor mostrando la visualización de créditos y saldo de la cuenta](../../images/getting-started/display-credits.gif)
*Visualización de créditos de la cuenta en el panel de AutoProctor*
{% endstep %}
{% step %}
### Configure la programación del examen con margen adicional
Configure un Buffer Time para que los candidatos tengan un período de gracia después del límite "Can't Start After" para configurar su dispositivo.

Consulte [Configuración del Temporizador](tests-results/create/timer-settings.md) para detalles de configuración.
{% endstep %}
{% step %}
### Pruebe el enlace usted mismo
Antes de compartir el enlace del examen, haga clic en él usted mismo para verificar la experiencia del candidato. Confirme que la página de instrucciones, la verificación de cámara y la configuración de supervisión se carguen correctamente.
{% endstep %}
{% endstepper %}

## Distribución de los Enlaces del Examen

La forma en que comparte el enlace del examen es importante. Algunos métodos de distribución causan problemas de compatibilidad.

| Método | ¿Recomendado? | Notas |
|---|---|---|
| **Correo electrónico (Gmail, Outlook)** | Sí | Los enlaces se abren en el navegador predeterminado, lo cual funciona de manera confiable |
| **LMS (Moodle, Canvas, etc.)** | Sí | Los enlaces se abren en el navegador del sistema |
| **Telegram, Facebook, WhatsApp** | No | Los navegadores integrados de estas aplicaciones frecuentemente son incompatibles con la supervisión de AutoProctor |

{% hint style="warning" %}
Si los candidatos reciben enlaces del examen a través de aplicaciones de mensajería (como Telegram, WhatsApp o Facebook Messenger), aconséjeles que **copien el enlace** y lo abran directamente en **Chrome** o **Firefox**. Los navegadores integrados de estas aplicaciones carecen de las funciones que AutoProctor necesita para la supervisión.
{% endhint %}

{% hint style="info" %}
Envíe el enlace de demostración al menos 24 horas antes del examen real. Envíe el enlace del examen real más cerca de la hora programada para prevenir el acceso anticipado.
{% endhint %}

## Durante el Examen

- **Esté disponible** — Manténgase accesible a través de un canal de comunicación (como Google Meet, Zoom o WhatsApp) durante la ventana del examen para que los candidatos puedan contactarlo si encuentran problemas técnicos.

## Después del Examen

{% stepper %}
{% step %}
### Revise los resultados de supervisión
Consulte los [Puntajes de Confianza](understanding/how-proctoring-works/trust-score.md) y los informes de supervisión de cada candidato. Enfoque su revisión en los candidatos con puntuación inferior al 85%.


{% endstep %}
{% step %}
### Ayude a los candidatos con problemas técnicos
Si los candidatos enfrentan algún problema técnico durante el examen, pídales que sigan [este artículo](pricing-account/support/contact-us.md).
{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [Antes de Comenzar](understanding/getting-started/things-you-need-to-know.md) — Requisitos esenciales para usar AutoProctor
- [¿Dónde Puedo Ver los Resultados de Mi Examen?](tests-results/results/how-to-see-results.md) — Descripción general de resultados del examen vs. resultados de supervisión
- [Puntaje de Confianza](understanding/how-proctoring-works/trust-score.md) — Cómo se calculan los Puntajes de Confianza
- [Configuración de Supervisión](tests-results/create/proctoring-settings.md) — Configure qué se monitorea durante los exámenes
- [Concurrencia](tests-results/access-limits/concurrency.md) — Comprenda los límites de candidatos simultáneos
- [Compatibilidad de Dispositivos](understanding/getting-started/device-compatibility.md) — Navegadores y dispositivos compatibles

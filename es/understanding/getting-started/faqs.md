---
title: "Preguntas Frecuentes"
description: "Respuestas a las preguntas más comunes sobre la plataforma de supervisión, los precios y las capacidades de AutoProctor."
---

A continuación encontrará respuestas a las preguntas más frecuentes sobre AutoProctor. Si su pregunta no está cubierta aquí, [contacte a nuestro equipo de soporte](pricing-account/support/contact-us.md).

<AccordionGroup>
  <Accordion title="¿Cómo garantiza AutoProctor la integridad de las pruebas en línea?">
    AutoProctor utiliza monitoreo con inteligencia artificial en el dispositivo que accede a cámaras, micrófonos y pantallas (con el permiso del candidato) para detectar comportamientos problemáticos. Estos incluyen personas no autorizadas en el encuadre, ruido de fondo e intentos de navegar fuera de la pantalla del examen. Cada incidente genera un informe detallado de infracciones con evidencia para que usted lo revise.

    Obtenga más información sobre [qué se monitorea](understanding/how-proctoring-works/what-gets-tracked.md) durante la supervisión.
  </Accordion>

  <Accordion title="¿Cómo creo y administro exámenes en AutoProctor?">
    Usted crea un examen supervisado en cinco pasos:

{% stepper %}
{% step %}
### Cree un cuestionario
Elabore su cuestionario usando Google Forms, Microsoft Forms o [Socratease](socratease/create-questions/why-socratease.md).
{% endstep %}
{% step %}
### Registre el examen en AutoProctor
Inicie sesión en AutoProctor y registre la URL de su cuestionario, o cree un cuestionario de Socratease directamente en la plataforma.
{% endstep %}
{% step %}
### Configure sus ajustes de supervisión
Configure el seguimiento de cámara, el monitoreo de micrófono, la pantalla compartida y otras opciones en su [configuración de supervisión](tests-results/create/proctoring-settings.md).
{% endstep %}
{% step %}
### Comparta el enlace del examen con los candidatos
Distribuya el enlace único del examen de AutoProctor a sus candidatos por correo electrónico, LMS o cualquier herramienta de mensajería.
{% endstep %}
{% step %}
### Revise los informes de infracciones
Después del examen, revise los [resultados de supervisión](tests-results/results/proctoring-results.md) y los [Puntajes de Confianza](understanding/how-proctoring-works/trust-score.md) de cada candidato.
{% endstep %}
{% endstepper %}

    Para un recorrido completo, consulte la [guía de inicio rápido](tests-results/create/your-first-proctored-test.md).
  </Accordion>

  <Accordion title="¿Cuáles son los planes de precios de AutoProctor?">
    AutoProctor ofrece tres niveles de suscripción:

    | Plan | Qué Incluye |
    |---|---|
    | **Standard** | 150 créditos de supervisión por ciclo de facturación, más intentos ilimitados solo con temporizador |
    | **Premium** | Funciones Standard más capacidades de colaboración en equipo |
    | **Elite** | Funciones Premium más tipos de preguntas avanzados, bancos de preguntas y acceso a API/SDK |

    Todos los planes incluyen una **prueba gratuita de 10 créditos** sin necesidad de tarjeta de crédito. Puede cancelar en cualquier momento.

    Visite la [página de precios](https://www.autoproctor.co/pricing/) para consultar las tarifas actuales, o consulte [Pagos y Créditos](pricing-account/plans-credits/payments-and-credits.md) para detalles sobre cómo funcionan los créditos.
  </Accordion>

  <Accordion title="¿Cuántos candidatos pueden realizar un examen supervisado simultáneamente?">
    AutoProctor admite hasta **5,000 candidatos simultáneos** en un solo examen.

{% hint style="info" %}
Si anticipa más de 5,000 candidatos realizando un examen al mismo tiempo, [contáctenos](pricing-account/support/contact-us.md) con al menos dos días hábiles de anticipación para que podamos preparar nuestra infraestructura.
{% endhint %}

    Obtenga más información sobre los [límites de concurrencia](tests-results/access-limits/concurrency.md).
  </Accordion>

  <Accordion title="¿Cómo protege AutoProctor la privacidad y los datos de los usuarios?">
    AutoProctor recopila nombres, direcciones de correo electrónico, imágenes y grabaciones de audio exclusivamente con fines de integridad de los exámenes. La empresa no vende información personal ni la comparte con terceros más allá de los subprocesadores necesarios.

    Datos clave de privacidad:
    - Todo el monitoreo con IA ocurre **en el dispositivo del candidato** — no se cargan grabaciones de video completas a los servidores
    - Los datos se utilizan únicamente para generar informes de supervisión
    - Los candidatos menores de 18 años requieren el consentimiento de los padres o tutores

{% hint style="info" %}
AutoProctor no graba video completo. Consulte [¿AutoProctor Graba Video?](understanding/how-proctoring-works/video-recording.md) para detalles sobre cómo el enfoque de monitoreo en el dispositivo protege la privacidad del candidato.
{% endhint %}
  </Accordion>

  <Accordion title="¿Qué plataformas de cuestionarios admite AutoProctor?">
    AutoProctor funciona con las siguientes plataformas de cuestionarios:

    - **Google Forms**
    - **Microsoft Forms**
    - **Socratease** (la plataforma de cuestionarios integrada de AutoProctor)
    - **Cualquier cuestionario basado en la web** mediante inserción por iframe

    Consulte [Proveedores de Cuestionarios](tests-results/create/quiz-providers.md) para instrucciones de configuración de cada plataforma.
  </Accordion>

  <Accordion title="¿Puedo restringir quién puede realizar mi examen?">
    Sí. AutoProctor ofrece varias opciones de control de acceso:

    - **[Restringir por dominio de correo electrónico](tests-results/access-limits/restricting-by-email.md)** — Permita solo candidatos con dominios de correo electrónico específicos (por ejemplo, @universidad.edu)
    - **[Restringir a usuarios específicos](tests-results/access-limits/restricting-to-some-users.md)** — Permita solo una lista preaprobada de direcciones de correo electrónico
    - **[Invitar candidatos por correo electrónico](tests-results/access-limits/inviting-candidates-via-email.md)** — Envíe invitaciones directas a candidatos específicos

    Configure estas opciones en su [configuración avanzada](tests-results/create/advanced-settings.md).
  </Accordion>
</AccordionGroup>

## Recursos Relacionados

- [Inicio Rápido](tests-results/create/your-first-proctored-test.md) — Cree su primer examen supervisado en menos de 5 minutos
- [Qué Se Monitorea](understanding/how-proctoring-works/what-gets-tracked.md) — Todas las capacidades de monitoreo disponibles
- [Puntaje de Confianza](understanding/how-proctoring-works/trust-score.md) — Cómo AutoProctor califica la integridad del candidato
- [Compatibilidad de Dispositivos](understanding/getting-started/device-compatibility.md) — Navegadores y dispositivos compatibles
- [Contáctenos](pricing-account/support/contact-us.md) — Obtenga ayuda del equipo de soporte de AutoProctor
- [Solicitar una Demostración](pricing-account/support/booking-a-demo.md) — Programe un recorrido en vivo de AutoProctor

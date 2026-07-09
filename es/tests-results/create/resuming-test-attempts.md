---
title: "Reanudación de Intentos de Examen"
description: "Comprenda cómo AutoProctor gestiona la reanudación de exámenes cuando los candidatos se desconectan, cierran el navegador o abandonan un examen a mitad del intento."
---

Cuando un candidato abandona un examen a mitad del intento — ya sea por un fallo del navegador, un problema de red o un cierre accidental — AutoProctor determina si debe reanudar el intento anterior o crear uno nuevo. El comportamiento depende del tipo de examen y de su configuración.

## Comportamiento de Reanudación por Tipo de Examen

| Tipo de Examen | Comportamiento de Reanudación | Detalles |
|---|---|---|
| Cuestionario Socratease | Siempre reanuda | Carga las respuestas anteriores automáticamente; los candidatos deben completar el intento existente antes de iniciar uno nuevo |
| Microsoft Forms | Nunca reanuda | Crea un nuevo intento cada vez debido a limitaciones de la plataforma |
| Google Forms | Configurable | Controlado por la opción **Habilitar Reanudación Automática** y la configuración de autoguardado de Google Forms |
| Exámenes con IFrame | Configurable | Controlado por la opción **Habilitar Reanudación Automática** |

## Configurar la Función de Reanudación

Para Google Forms y Exámenes con IFrame, usted controla el comportamiento de reanudación mediante la opción **Habilitar Reanudación Automática** en la configuración de su examen.

{% stepper %}
{% step %}
### Abra la configuración del examen
Navegue a su examen en el [panel de control de AutoProctor](https://www.autoproctor.co/test-admin/home/) y haga clic en el botón **Configuración**.


{% endstep %}
{% step %}
### Active Habilitar Reanudación Automática
Busque y active o desactive la opción **Habilitar Reanudación Automática**.



![Opción de Habilitar Reanudación Automática en la configuración del examen de AutoProctor](images/settings/enable-auto-resume.png)
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Para Google Forms, también debe mantener habilitada la configuración de **Guardar Borrador** (autoguardado) en el propio Google Forms para que la reanudación funcione correctamente. Consulte [Reanudación de Exámenes de Google Forms](tests-results/create/resuming-google-forms.md) para una configuración detallada.
{% endhint %}

## Cómo Funciona la Reanudación

Cuando un candidato regresa al enlace del examen después de desconectarse:

- **Si la reanudación está habilitada**: AutoProctor carga el intento anterior con todas las respuestas previas intactas. El candidato continúa desde donde lo dejó.
- **Si la reanudación está deshabilitada**: AutoProctor crea un nuevo intento en blanco. Todas las respuestas anteriores del intento interrumpido se pierden (aunque el intento incompleto sigue apareciendo en sus resultados).

## Cómo Interactúan los Temporizadores con la Reanudación

Si tiene [configuración del temporizador](tests-results/create/timer-settings.md) configurada, esta afecta el funcionamiento de la reanudación.

### Duración del Examen

El tiempo restante del intento original se transfiere. Por ejemplo, si un candidato comienza un examen de 60 minutos a las 10:00 AM y se desconecta a las 10:30 AM, al reanudar a las 10:50 AM le quedarán solo 10 minutos. Una vez que la duración total expire (11:00 AM), el examen ya no puede reanudarse.

### No Puede Iniciar Antes / No Puede Iniciar Después

Estas restricciones se aplican a la hora de inicio original, no a la hora de reconexión. Un candidato que inició antes de la fecha límite puede reanudar después de esta, siempre que la duración del examen no haya expirado.

### Debe Enviar Antes

Esta fecha límite se aplica estrictamente en el momento de la reconexión. Si la fecha límite de **Debe Enviar Antes** ya pasó antes de que el candidato intente reanudar, el examen no se carga — incluso si el candidato inició originalmente antes de la fecha límite.

{% hint style="warning" %}
La fecha límite de **Debe Enviar Antes** anula todas las demás configuraciones del temporizador en el momento de la reanudación. Si esta fecha límite ha pasado, el candidato no puede reanudar independientemente del tiempo de examen restante.
{% endhint %}

## Recursos Relacionados

- [Reanudación de Exámenes de Google Forms](tests-results/create/resuming-google-forms.md) — Configuración detallada de la reanudación en Google Forms
- [Intentos Máximos](tests-results/access-limits/maximum-attempts.md) — Cómo los límites de intentos interactúan con la reanudación
- [Exámenes No Enviados](tests-results/results/unsubmitted-tests.md) — Ver detalles de exámenes iniciados pero no enviados
- [Configuración del Temporizador](tests-results/create/timer-settings.md) — Configure la duración del examen, fechas límite y ventanas de tiempo
- [Mejores Prácticas para Creadores de Exámenes](understanding/getting-started/best-practices-for-teachers.md) — Consejos para una administración de exámenes fluida

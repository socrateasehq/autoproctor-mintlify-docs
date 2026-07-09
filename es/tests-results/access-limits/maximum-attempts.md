---
title: "Intentos Máximos para un Examen"
description: "Configure cuántas veces los candidatos pueden intentar un examen en AutoProctor y comprenda cómo funciona el seguimiento de intentos en distintos métodos de inicio de sesión."
---

La configuración de **Intentos Máximos** le permite controlar cuántas veces cada candidato puede realizar un examen específico. Una vez que un candidato alcanza el límite, AutoProctor bloquea intentos adicionales y muestra una notificación.

## Cómo Configurar los Intentos Máximos

{% embed url="../../videos/settings/max-attempts-settings.mp4" %}
Cómo configurar los intentos máximos en AutoProctor
{% endembed %}

{% stepper %}
{% step %}
### Abra la configuración del examen
Navegue a su examen en el [panel de control de AutoProctor](https://www.autoproctor.co/test-admin/home/) y haga clic en el botón **Configuración**.
{% endstep %}
{% step %}
### Establezca el valor de Intentos Máximos
En la sección **Configuración Principal**, ubique el campo **Intentos Máximos** e ingrese el número de intentos permitidos.
{% endstep %}
{% step %}
### Guarde el examen
Haga clic en **Crear** o **Actualizar** para aplicar la configuración.
{% endstep %}
{% endstepper %}

Cuando un candidato excede el número de intentos permitidos, verá un mensaje de restricción y no podrá continuar.


![Restriction message shown to candidates](../../images/settings/max-attempts-blocked.png)
*Restriction message shown to candidates*

## Configuración Recomendada

| Tipo de Examen | Intentos Máximos Recomendados | Razón |
|---|---|---|
| Google Forms | 1 | AutoProctor [reanuda automáticamente](tests-results/create/resuming-test-attempts.md) estos exámenes si los candidatos recargan o revisitan el enlace |
| Cuestionario Socratease | 1 | AutoProctor [reanuda automáticamente](tests-results/create/resuming-test-attempts.md) estos exámenes si los candidatos recargan o revisitan el enlace |
| Microsoft Forms | Según sus necesidades | Cada visita crea un nuevo intento; la reanudación no es compatible |
| Exámenes con IFrame | Según sus necesidades | Comportamiento de reanudación configurable; ajuste los intentos en consecuencia |

{% hint style="info" %}
Para Google Forms y Cuestionarios Socratease, establezca **Intentos Máximos** en **1**. AutoProctor [reanuda automáticamente estos exámenes](tests-results/create/resuming-test-attempts.md) si los candidatos recargan la página o revisitan el enlace, por lo que no se necesitan múltiples intentos para la reanudación.
{% endhint %}

## Cómo Se Hace el Seguimiento de los Intentos

AutoProctor hace seguimiento de los intentos por la dirección de correo electrónico utilizada para iniciar sesión. Esto significa:

- Cada dirección de correo electrónico única cuenta como un candidato separado, independientemente de quién esté detrás.
- Si un candidato inicia sesión con diferentes direcciones de correo electrónico en distintos intentos (por ejemplo, usando **Iniciar sesión con Google** una vez e **Iniciar sesión con Correo Electrónico** otra vez con una dirección diferente), cada correo electrónico cuenta por separado, lo que efectivamente permite eludir el límite de intentos.

{% hint style="warning" %}
Si un candidato usa diferentes métodos de inicio de sesión que resuelven a diferentes direcciones de correo electrónico, cada una cuenta como un candidato separado. Esto puede permitirle eludir el límite de intentos máximos.
{% endhint %}

## Prevenir la Elusión del Límite de Intentos

Para evitar que los candidatos eludan la configuración de intentos máximos:

- **Restrinja los métodos de inicio de sesión** — Elija un tipo de examen que admita solo una opción de inicio de sesión. Google Forms restringe a los candidatos solo al inicio de sesión con Google, y Microsoft Forms restringe solo al inicio de sesión con Microsoft. Consulte [Métodos de Inicio de Sesión del Candidato](candidate-guide/attempting/candidate-login-methods.md).
- **Use restricciones por correo electrónico** — Limite el acceso a dominios o direcciones de correo electrónico específicos para que los candidatos no puedan usar cuentas alternativas. Consulte [Restringir el Acceso al Examen por Dirección de Correo Electrónico](tests-results/access-limits/restricting-by-email.md).
- **Use enlaces de invitación únicos** — Genere URLs por candidato que apliquen verificación de correo electrónico. Consulte [Invitar Candidatos por Correo Electrónico](tests-results/access-limits/inviting-candidates-via-email.md).

## Recursos Relacionados

- [Métodos de Inicio de Sesión del Candidato](candidate-guide/attempting/candidate-login-methods.md) — Cómo los métodos de inicio de sesión afectan al seguimiento de intentos
- [Reanudación de Intentos de Examen](tests-results/create/resuming-test-attempts.md) — Cómo funciona la reanudación de exámenes en los distintos tipos
- [Restringir el Acceso al Examen por Dirección de Correo Electrónico](tests-results/access-limits/restricting-by-email.md) — Limitar el acceso por dominio o dirección de correo electrónico
- [Configuración del Temporizador](tests-results/create/timer-settings.md) — Configure la duración del examen y las ventanas de tiempo
- [Invitar Candidatos por Correo Electrónico](tests-results/access-limits/inviting-candidates-via-email.md) — Envíe enlaces de examen únicos a los candidatos

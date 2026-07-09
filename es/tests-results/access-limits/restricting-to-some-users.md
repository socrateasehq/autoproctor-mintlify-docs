---
title: "Restringir el Acceso al Examen a Candidatos Específicos"
description: "Limite la participación en el examen a candidatos específicos en AutoProctor mediante la distribución de enlaces, restricciones por correo electrónico, enlaces de invitación únicos o controles de acceso de la plataforma."
---

De forma predeterminada, cualquier persona con su enlace de examen puede realizarlo. AutoProctor le ofrece varios métodos para restringir el acceso para que solo los candidatos que usted elija puedan participar.

## Método 1: Distribución Selectiva del Enlace

El enfoque más sencillo es compartir el enlace del examen solo con los candidatos que deben realizarlo.

{% stepper %}
{% step %}
### Identifique a los candidatos elegibles
Determine qué candidatos deben tener acceso al examen.
{% endstep %}
{% step %}
### Comparta el enlace de forma privada
Envíe el enlace del examen solo a esos candidatos por correo electrónico, su sistema de gestión de aprendizaje u otro canal privado. Evite publicar el enlace de forma pública.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Este método depende de que los candidatos no compartan el enlace con otras personas. Si necesita un control de acceso más estricto, utilice uno de los métodos siguientes.
{% endhint %}

## Método 2: Restricciones Basadas en Correo Electrónico

Utilice las **Restricciones de Inicio de Sesión** integradas en AutoProctor para permitir solo dominios de correo electrónico o direcciones individuales específicas. Esto se configura en la sección de Configuración Avanzada de su examen.

{% stepper %}
{% step %}
### Abra la Configuración Avanzada
Navegue a la configuración de su examen y desplácese hasta la sección de **Configuración Avanzada**.
{% endstep %}
{% step %}
### Ingrese las Restricciones de Inicio de Sesión
Agregue los dominios de correo electrónico (por ejemplo, `@suescuela.edu`) o las direcciones de correo electrónico específicas que desea permitir.
{% endstep %}
{% step %}
### Guarde el examen
Haga clic en **Crear** o **Actualizar** para aplicar las restricciones.
{% endstep %}
{% endstepper %}

![Campo de Restricciones de Inicio de Sesión con restricciones de dominio y correo electrónico](images/settings/login-restrictions-email.png)
*Campo de Restricciones de Inicio de Sesión con restricciones de dominio y correo electrónico*

Consulte [Restringir el Acceso al Examen por Dirección de Correo Electrónico](tests-results/access-limits/restricting-by-email.md) para instrucciones completas de configuración y ejemplos.

## Método 3: Enlaces de Invitación Únicos

Genere URLs únicas por candidato vinculadas a direcciones de correo electrónico específicas. Cada candidato recibe su propio enlace con verificación de correo electrónico, de modo que solo el destinatario previsto puede usarlo.

{% embed url="videos/settings/unique-invitation-links.mp4" %}
Configuración de enlaces de invitación únicos
{% endembed %}

{% stepper %}
{% step %}
### Active la URL Única
Abra la configuración de su examen y active la opción **URL Única**.
{% endstep %}
{% step %}
### Cargue las direcciones de correo electrónico
Cargue las direcciones de correo electrónico de los candidatos mediante un archivo CSV (hasta 1,000 a la vez).
{% endstep %}
{% step %}
### Genere los enlaces únicos
AutoProctor genera un enlace único para cada dirección de correo electrónico como pares separados por comas.
{% endstep %}
{% step %}
### Dé formato a los datos
Pegue el resultado en una aplicación de hoja de cálculo y divídalo por el separador de coma para organizar las direcciones de correo electrónico y los enlaces en columnas separadas.
{% endstep %}
{% step %}
### Distribuya los enlaces únicos
Envíe a cada candidato su enlace único de forma individual utilizando la hoja de cálculo que creó.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Los enlaces de invitación únicos solo están disponibles en el **Plan Elite** y funcionan con Cuestionarios Socratease y Exámenes con IFrame. Consulte [Pagos y Créditos](pricing-account/plans-credits/payments-and-credits.md) para detalles del plan.
{% endhint %}

Consulte [Invitar Candidatos por Correo Electrónico](tests-results/access-limits/inviting-candidates-via-email.md) para el proceso completo de configuración.

## Método 4: Restricciones de Acceso de Google Forms

Si usa Google Forms, puede restringir el acceso a nivel de Google Forms en lugar de (o además de) las restricciones de AutoProctor. Los candidatos pueden abrir el enlace de AutoProctor, pero no pueden continuar si Google Forms bloquea su acceso.

{% stepper %}
{% step %}
### Abra la configuración de su Google Form
En Google Forms, haga clic en el icono de engranaje de **Configuración**.
{% endstep %}
{% step %}
### Restrinja a su organización
Active la opción para restringir las respuestas a los usuarios de su organización. Esto limita el acceso a candidatos con direcciones de correo electrónico bajo su dominio de Google Workspace.

![Configuración de restricción de acceso de Google Forms](images/settings/google-form-restriction.png)
*Configuración de restricción de acceso de Google Forms*
{% endstep %}
{% endstepper %}

Para más detalles, consulte la [guía de Google sobre restricción de acceso a formularios](https://www.bettercloud.com/monitor/the-academy/restrict-access-to-google-forms/).

## Comparación de Métodos de Control de Acceso

| Método | Fortaleza | Funciona Con | Plan Requerido |
|---|---|---|---|
| Distribución selectiva del enlace | Baja — depende de la confianza | Todos los tipos de exámenes | Cualquiera |
| Restricciones basadas en correo electrónico | Media — bloquea dominios incorrectos | Todos los tipos de exámenes | Cualquiera |
| Enlaces de invitación únicos | Alta — verificación por candidato | Cuestionarios Socratease, Exámenes con IFrame | Elite |
| Restricciones de Google Forms | Media — nivel de organización | Solo Google Forms | Cualquiera |

## Recursos Relacionados

- [Restringir el Acceso al Examen por Dirección de Correo Electrónico](tests-results/access-limits/restricting-by-email.md) — Configure restricciones basadas en dominio y correo electrónico
- [Invitar Candidatos por Correo Electrónico](tests-results/access-limits/inviting-candidates-via-email.md) — Genere enlaces de examen únicos por candidato
- [Métodos de Inicio de Sesión del Candidato](candidate-guide/attempting/candidate-login-methods.md) — Conozca las opciones de autenticación disponibles
- [Configuración Avanzada](tests-results/create/advanced-settings.md) — Configure las Restricciones de Inicio de Sesión y otras opciones avanzadas
- [Mejores Prácticas para Creadores de Exámenes](understanding/getting-started/best-practices-for-teachers.md) — Consejos para una administración de exámenes fluida

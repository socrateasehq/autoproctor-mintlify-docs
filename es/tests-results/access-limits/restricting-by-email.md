---
title: "Restringir el Acceso al Examen por Dirección de Correo Electrónico"
description: "Limite quién puede realizar su examen restringiendo el acceso a dominios de correo electrónico específicos o direcciones individuales mediante Restricciones de Inicio de Sesión."
---

Las Restricciones de Inicio de Sesión le permiten controlar exactamente quién puede realizar su examen filtrando a los candidatos según su dirección de correo electrónico. Esto impide el acceso no autorizado incluso si alguien comparte o descubre el enlace de su examen.

## Cómo Configurar las Restricciones por Correo Electrónico

{% stepper %}
{% step %}
### Abra la configuración de su examen
Navegue al examen en su [panel de control de AutoProctor](https://www.autoproctor.co/test-admin/home/) y haga clic en el botón **Configuración**.


{% endstep %}
{% step %}
### Vaya a Configuración Avanzada
Desplácese hacia abajo hasta la sección de **Configuración Avanzada** y ubique los campos de **Restricciones de Inicio de Sesión**.


{% endstep %}
{% step %}
### Agregue restricciones de dominio o correo electrónico
Ingrese los dominios de correo electrónico o las direcciones de correo electrónico específicas que desea permitir. Puede combinar ambos tipos de restricciones en un solo campo (vea los ejemplos a continuación).
{% endstep %}
{% step %}
### Guarde el examen
Haga clic en **Crear** o **Actualizar** para aplicar las restricciones.
{% endstep %}
{% endstepper %}

## Restricciones Basadas en Dominio

Puede restringir el acceso a candidatos cuyas direcciones de correo electrónico terminen con dominios específicos. Por ejemplo, al ingresar `@abc.com` y `@xyz.com`, solo los candidatos con esos dominios de correo electrónico podrán realizar el examen.


![Campo de Restricciones de Inicio de Sesión mostrando restricciones basadas en dominio con @abc.com y @xyz.com ingresados](images/settings/login-restrictions-domain.png)

## Restricciones por Correo Electrónico Específico

También puede permitir direcciones de correo electrónico individuales junto con las restricciones de dominio. Esto es útil cuando la mayoría de los candidatos comparten un dominio pero algunos participantes externos necesitan acceso.

Por ejemplo, puede permitir a todos los usuarios cuyo correo electrónico termine en `@abc.com` más direcciones de correo electrónico individuales específicas como `guest@gmail.com`.


![Campo de Restricciones de Inicio de Sesión mostrando una combinación de restricciones de dominio y de correo electrónico individual](images/settings/login-restrictions-email.png)

{% hint style="info" %}
Las restricciones por correo electrónico funcionan en conjunto con el [método de inicio de sesión](candidate-guide/attempting/candidate-login-methods.md) del candidato. El candidato debe iniciar sesión con una dirección de correo electrónico que coincida con uno de los dominios o direcciones permitidos que usted especificó.
{% endhint %}

## Recursos Relacionados

- [Métodos de Inicio de Sesión del Candidato](candidate-guide/attempting/candidate-login-methods.md) — Conozca las opciones de autenticación disponibles para los candidatos
- [Restringir a Candidatos Específicos](tests-results/access-limits/restricting-to-some-users.md) — Otros métodos para limitar el acceso al examen
- [Invitar Candidatos por Correo Electrónico](tests-results/access-limits/inviting-candidates-via-email.md) — Genere enlaces de examen únicos por candidato
- [Configuración Avanzada](tests-results/create/advanced-settings.md) — Configure las Restricciones de Inicio de Sesión y otras opciones avanzadas del examen
- [Mejores Prácticas para Creadores de Exámenes](understanding/getting-started/best-practices-for-teachers.md) — Consejos para una administración de exámenes fluida

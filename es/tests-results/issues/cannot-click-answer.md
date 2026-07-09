---
title: "No Se Puede Hacer Clic en las Respuestas del Formulario del Examen"
description: "Solucione el problema en el que el formulario del examen carga pero no se puede hacer clic en las preguntas ni seleccionar respuestas. Generalmente es causado por haber iniciado sesión con la cuenta de Google incorrecta."
---

Si puede ver el formulario del examen pero no puede hacer clic en las preguntas ni seleccionar respuestas, lo más probable es que haya iniciado sesión con una cuenta de Google que no tiene permiso para interactuar con el formulario.

## Por Qué Sucede Esto

Cuando un formulario de Google Forms está restringido a direcciones de correo electrónico específicas, se carga en un modo de vista previa de solo lectura para las cuentas no autorizadas. Usted puede ver las preguntas pero no puede interactuar con ellas. Dado que AutoProctor incorpora el formulario de Google Forms dentro de su interfaz, esta restricción aparece dentro de la ventana del examen de AutoProctor.

![Formulario de Google Forms en AutoProctor en el que no se puede hacer clic porque la cuenta de Google incorrecta está activa](../../images/candidate-issues/cannot-click-form.png)
*Formulario del examen cargado en modo de solo lectura debido a una cuenta de Google incorrecta*

## Cómo Solucionarlo

{% stepper %}
{% step %}
### Cierre sesión en todas las cuentas de Google
Visite [accounts.google.com/Logout](https://accounts.google.com/Logout) y cierre sesión en todas sus cuentas.
{% endstep %}
{% step %}
### Inicie sesión con la cuenta correcta
Inicie sesión nuevamente con la cuenta de Google que tiene acceso al examen. Consulte con su administrador de exámenes si no está seguro de qué cuenta usar.
{% endstep %}
{% step %}
### Recargue el examen
Vuelva al enlace del examen y cárguelo de nuevo. Ahora debería poder hacer clic en las preguntas y seleccionar respuestas.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Si no está seguro de qué cuenta de Google tiene acceso, comuníquese con su administrador de exámenes. Ellos pueden confirmar la dirección de correo electrónico que recibió permiso para realizar el examen.
{% endhint %}

## Recursos Relacionados

- [Página en Blanco o Pantalla Gris](tests-results/issues/blank-page-grey-screen.md) -- Problema similar causado por la cuenta de Google incorrecta
- [No Se Pueden Ver las Preguntas en Google Forms](tests-results/issues/google-forms-questions-not-visible.md) -- Restricciones de acceso a Google Forms
- [Cómo Cerrar Sesión](candidate-guide/attempting/how-to-logout.md) -- Pasos para cambiar de cuenta
- [Instrucciones para Realizar un Examen Supervisado](candidate-guide/attempting/proctored-test-instructions.md) -- Guía de configuración con sección de Cuenta de Google
- [Compatibilidad de Dispositivos](understanding/getting-started/device-compatibility.md) -- Consulte los navegadores y dispositivos compatibles
- [Contáctenos](pricing-account/support/contact-us.md) -- Comuníquese si necesita más ayuda

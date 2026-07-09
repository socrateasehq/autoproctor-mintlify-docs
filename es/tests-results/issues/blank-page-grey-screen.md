---
title: "Página en Blanco o Pantalla Gris Durante el Examen"
description: "Resuelva problemas de página en blanco o pantalla gris al cargar un examen supervisado. Generalmente es causado por haber iniciado sesión con la cuenta de Google incorrecta."
---

Si su examen muestra una página en blanco o una pantalla gris en lugar de cargar las preguntas, la causa más común es que usted ha iniciado sesión con una cuenta de Google que no tiene acceso al formulario del examen.

## Por Qué Sucede Esto

Cuando un administrador de exámenes restringe el acceso a direcciones de correo electrónico específicas, Google Forms bloquea a cualquier persona que haya iniciado sesión con una cuenta diferente. AutoProctor carga el formulario de Google Forms dentro de su propia interfaz, por lo que usted ve una pantalla en blanco o gris en lugar del mensaje de error del propio formulario.


![Página en blanco mostrada cuando la cuenta de Google incorrecta está activa en AutoProctor](../../images/candidate-issues/blank-page-google-account.png)
*Página en blanco causada por haber iniciado sesión con la cuenta de Google incorrecta*

## Cómo Solucionarlo

{% stepper %}
{% step %}
### Cierre sesión en todas las cuentas de Google
Visite [accounts.google.com/Logout](https://accounts.google.com/Logout) para cerrar sesión en todas sus cuentas de Google.
{% endstep %}
{% step %}
### Inicie sesión con la cuenta correcta
Inicie sesión con la cuenta de Google que tiene acceso al examen. Generalmente es la dirección de correo electrónico para la cual su administrador de exámenes proporcionó instrucciones.
{% endstep %}
{% step %}
### Recargue el examen
Vuelva al enlace del examen y cárguelo de nuevo. El formulario debería mostrarse correctamente ahora.
{% endstep %}
{% step %}
### Pruebe usar el modo Incógnito
Si la página sigue en blanco, abra el enlace del examen en una **ventana de incógnito** (`Ctrl+Shift+N` en Windows o `Cmd+Shift+N` en Mac). El modo incógnito inicia una sesión nueva sin cuentas ni permisos en caché, lo que frecuentemente resuelve el problema.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Para instrucciones detalladas de configuración antes de realizar un examen, consulte:
- [Instrucciones para Realizar un Examen Supervisado](candidate-guide/attempting/proctored-test-instructions.md) -- Sección de Configuración de la Cuenta de Google
- [Instrucciones para Realizar un Examen Cronometrado](candidate-guide/attempting/timed-test-instructions.md) -- Sección de Configuración de la Cuenta de Google
{% endhint %}

## Recursos Relacionados

- [No Se Puede Hacer Clic en la Respuesta](tests-results/issues/cannot-click-answer.md) -- Problema similar causado por la cuenta de Google incorrecta
- [No Se Pueden Ver las Preguntas en Google Forms](tests-results/issues/google-forms-questions-not-visible.md) -- Problemas de acceso a Google Forms
- [El Examen Se Queda en la Pantalla de Carga](tests-results/issues/loading-screen.md) -- Otros problemas de carga
- [Cómo Cerrar Sesión](candidate-guide/attempting/how-to-logout.md) -- Pasos para cambiar de cuenta
- [Compatibilidad de Dispositivos](understanding/getting-started/device-compatibility.md) -- Consulte los navegadores y dispositivos compatibles
- [Contáctenos](pricing-account/support/contact-us.md) -- Comuníquese si necesita más ayuda

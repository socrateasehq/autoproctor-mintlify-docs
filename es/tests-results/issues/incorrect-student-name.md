---
title: "Nombre Incorrecto del Candidato en los Resultados"
description: "Corrija los nombres incorrectos de candidatos que aparecen en la página de resultados o en la exportación de Excel. Los nombres se obtienen del perfil de la cuenta de Google o Microsoft vinculada del candidato."
---

AutoProctor no pide a los candidatos que escriban su nombre directamente. En su lugar, obtiene el nombre de la cuenta utilizada para iniciar sesión. Si el nombre de un candidato aparece incorrectamente en los resultados, el problema se origina en el perfil de su cuenta -- no en AutoProctor.

## Por Qué Sucede Esto

AutoProctor obtiene los nombres de los candidatos del proveedor de autenticación que utilizaron para iniciar sesión:

| Método de Inicio de Sesión | Fuente del Nombre |
|---|---|
| Cuenta de Google | Nombre para mostrar configurado en la [configuración de la cuenta de Google](https://myaccount.google.com/personal-info) |
| Cuenta de Microsoft | Nombre para mostrar configurado en la [configuración de la cuenta de Microsoft](https://account.microsoft.com/profile) |

Si el nombre en su cuenta de Google o Microsoft es incorrecto, está mal escrito o usa un apodo, ese mismo nombre aparecerá en los resultados de AutoProctor.

{% hint style="info" %}
AutoProctor obtiene los nombres de los candidatos directamente del perfil de su cuenta. Si el nombre es incorrecto en los resultados, el candidato necesita actualizar su perfil en AutoProctor directamente.
{% endhint %}

![Nombre incorrecto del candidato mostrado en la página de resultados de AutoProctor](images/candidate-issues/incorrect-student-name.png)
*Ejemplo de un nombre incorrecto de candidato mostrado en los resultados de AutoProctor*

## Cómo Solucionarlo

{% stepper %}
{% step %}
### Identifique el correo electrónico del candidato
Encuentre la dirección de correo electrónico asociada con el intento de examen del candidato en la página de resultados.
{% endstep %}
{% step %}
### Indique al candidato que actualice su perfil
Pida al candidato que visite [autoproctor.co/account/edit-profile](https://www.autoproctor.co/account/edit-profile/) y actualice su nombre. Comparta este enlace con el candidato junto con una nota identificando qué dirección de correo electrónico necesita la corrección.
{% endstep %}
{% step %}
### Verifique el cambio
Una vez que el candidato actualice su nombre en su perfil de AutoProctor, el cambio se refleja automáticamente en todos los informes de exámenes existentes. No se requiere ninguna acción adicional por parte del administrador del examen.
{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [Resultados de Supervisión](tests-results/results/proctoring-results.md) -- Cómo revisar los informes de supervisión
- [Cómo Cerrar Sesión](candidate-guide/attempting/how-to-logout.md) -- Cambiar de cuenta si se usó la incorrecta
- [Métodos de Inicio de Sesión para Candidatos](candidate-guide/attempting/candidate-login-methods.md) -- Comprenda las opciones de inicio de sesión
- [Instrucciones para Realizar un Examen Supervisado](candidate-guide/attempting/proctored-test-instructions.md) -- Guía de configuración para candidatos
- [Contáctenos](pricing-account/support/contact-us.md) -- Comuníquese si necesita más ayuda

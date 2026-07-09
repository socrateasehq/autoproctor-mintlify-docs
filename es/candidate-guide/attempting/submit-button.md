---
title: "Botón de Envío: Socratease frente a Otros Cuestionarios"
description: "Comprenda las diferencias clave en el proceso de envío entre los cuestionarios de Socratease y otros tipos de cuestionarios en AutoProctor, y por qué Socratease elimina el riesgo de perder las respuestas."
---

El proceso de envío varía según el proveedor de cuestionarios que utilice. Los cuestionarios de Socratease utilizan un único botón de envío, lo que elimina el riesgo de perder las respuestas. Otros tipos de cuestionarios (Google Forms, Microsoft Forms, etc.) requieren dos botones de envío que deben presionarse en el orden correcto.

## Cuestionarios que No Son de Socratease (Google Forms, Microsoft Forms, etc.)

Cuando AutoProctor integra formularios externos, debe **enviar dos veces** porque las restricciones de privacidad impiden que las plataformas externas notifiquen a AutoProctor cuando se realiza un envío:

{% stepper %}
{% step %}
### Haga clic en el botón morado de envío primero
Haga clic en el **botón morado de envío** en la parte inferior del formulario para guardar sus respuestas del cuestionario en el proveedor de cuestionarios (Google Forms, Microsoft Forms, etc.).
{% endstep %}
{% step %}
### Haga clic en el botón verde de envío después
Haga clic en el **botón verde de envío** en la parte superior de la página para enviar la sesión supervisada o cronometrada a AutoProctor.
{% endstep %}
{% endstepper %}

![Examen supervisado que requiere que los candidatos hagan clic en dos botones de envío separados](../../images/taking-tests/submit-buttons-proctored.png)
*Otras plataformas: doble botón de envío*

{% hint style="warning" %}
Si no envía las respuestas del cuestionario **primero** (botón morado), todas sus respuestas se perderán. Esto no se puede recuperar. Debido a las restricciones de privacidad, Google y Microsoft no permiten que AutoProctor detecte si se hizo clic en el botón morado de envío, por lo que AutoProctor no puede aplicar este paso automáticamente.
{% endhint %}

## Cuestionarios de Socratease

Los cuestionarios de Socratease utilizan un **único botón de envío**. Un solo clic envía tanto sus respuestas como la sesión de supervisión -- sin confusiones ni riesgo de perder las respuestas.

![Cuestionario Socratease mostrando un único botón de Enviar en la parte inferior](../../images/taking-tests/soc-submit-button.png)
*Socratease: un solo botón de envío*

{% hint style="info" %}
Los Cuestionarios de Socratease están disponibles en **todos los planes**, incluyendo la prueba gratuita. Consulte [¿Por Qué Socratease?](socratease/create-questions/why-socratease.md) para conocer más beneficios.
{% endhint %}

## Comparación

| Característica | No Socratease (Google Forms, etc.) | Socratease |
|---|---|---|
| Número de botones de envío | 2 (morado y luego verde) | 1 |
| Riesgo de perder respuestas | Sí, si los botones se presionan en el orden incorrecto | Ninguno |
| ¿Por qué dos botones? | Las restricciones de privacidad impiden que las plataformas externas notifiquen a AutoProctor | No aplica -- Socratease está integrado en AutoProctor |

## Recursos Relacionados

- [Instrucciones para Exámenes Supervisados](candidate-guide/attempting/proctored-test-instructions.md) -- Guía completa para exámenes supervisados
- [Instrucciones para Exámenes Cronometrados](candidate-guide/attempting/timed-test-instructions.md) -- Guía completa para exámenes cronometrados
- [Instrucciones para Socratease Supervisado](candidate-guide/attempting/proctored-socratease-instructions.md) -- Guía más sencilla para Socratease
- [Respuesta de Google Forms No Visible](tests-results/issues/google-forms-response-not-visible.md) -- Solucionar problemas con envíos faltantes
- [¿Por Qué Socratease?](socratease/create-questions/why-socratease.md) -- Beneficios de usar Socratease sobre Google Forms

---
title: "Uso de LaTeX para Ecuaciones Matemáticas"
description: "Agregue ecuaciones matemáticas a sus cuestionarios Socratease utilizando la sintaxis LaTeX."
---

Socratease admite LaTeX, el estándar global para escribir ecuaciones matemáticas utilizado en publicaciones académicas, libros de texto y trabajos de investigación en todo el mundo. En lugar de insertar imágenes de ecuaciones o usar notación de texto simplificada como `a^2` o `3/4`, puede escribir ecuaciones correctamente formateadas directamente en las preguntas de su cuestionario.

{% hint style="info" %}
El soporte de ecuaciones LaTeX es exclusivo de los **Cuestionarios Socratease** de AutoProctor. No está disponible cuando se usan otros proveedores de cuestionarios.
{% endhint %}

## Cómo Escribir Ecuaciones LaTeX

Para incluir una ecuación LaTeX en su cuestionario, encierre la ecuación entre los delimitadores `\(` y `\)`.

**Ejemplo:**

```
\(a^2 + b^2 = c^2\)
```

Esto se renderiza como el conocido teorema de Pitágoras: a al cuadrado más b al cuadrado es igual a c al cuadrado.


## Qué Admite LaTeX

LaTeX puede renderizar cualquier notación matemática, incluyendo:

| Notación | Sintaxis LaTeX | Descripción |
|---|---|---|
| Aritmética básica | `\(a + b = c\)` | Suma, resta, multiplicación, división |
| Exponentes | `\(x^2\)` | Superíndices y potencias |
| Subíndices | `\(a_n\)` | Notación de subíndice |
| Fracciones | `\(\frac{a}{b}\)` | Notación de fracción |
| Raíces cuadradas | `\(\sqrt{x}\)` | Raíces cuadradas y enésimas |
| Integrales | `\(\int_0^1 x^2 dx\)` | Integrales definidas e indefinidas |
| Sumatorias | `\(\sum_{i=1}^{n} i\)` | Notación de sumatoria |
| Letras griegas | `\(\alpha, \beta, \gamma\)` | Todos los símbolos de letras griegas |

También puede usar cualquier otra notación matemática estándar de LaTeX más allá de los ejemplos listados anteriormente.

## Habilitar LaTeX

{% embed url="../../videos/socratease/using-latex.mp4" %}
Cómo habilitar y usar LaTeX en Socratease
{% endembed %}

{% stepper %}
{% step %}
### Abra Su Cuestionario
Abra su Cuestionario Socratease en AutoProctor.
{% endstep %}
{% step %}
### Vaya a Configuración
Haga clic en el ícono de **Configuración** (engranaje) en la barra de herramientas del editor del cuestionario.
{% endstep %}
{% step %}
### Active el Soporte de LaTeX
Active la configuración de **Soporte de LaTeX**. Esto activa la representación de LaTeX para todas las preguntas del cuestionario.


{% endstep %}
{% step %}
### Escriba Sus Ecuaciones
Escriba sus ecuaciones en el texto de las preguntas usando los delimitadores `\(` y `\)`. Las ecuaciones se renderizarán como matemáticas formateadas cuando los candidatos vean el cuestionario.


{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Asegúrese de activar la opción de Soporte de LaTeX en la configuración del cuestionario **antes** de compartir el examen. Si LaTeX no está habilitado, los candidatos verán la sintaxis LaTeX sin procesar en lugar de ecuaciones renderizadas.
{% endhint %}

## Pruébelo

Puede ver un cuestionario de ejemplo que demuestra la representación de ecuaciones LaTeX en:
[autoproctor.co/tests/jVRBZGRMNU/load](https://www.autoproctor.co/tests/jVRBZGRMNU/load/)


## Recursos Relacionados

- [Configuración del Cuestionario](socratease/settings/quiz-settings.md) — Todas las opciones de configuración de cuestionarios Socratease
- [Tipos de Preguntas](socratease/create-questions/question-types.md) — Formatos de preguntas disponibles
- [Cómo Crear un Cuestionario Socratease](socratease/create-questions/creating-a-quiz.md) — Guía de creación paso a paso
- [¿Por Qué Socratease?](socratease/create-questions/why-socratease.md) — Beneficios de usar Socratease sobre otras plataformas

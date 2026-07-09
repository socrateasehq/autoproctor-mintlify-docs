---
title: "Proveedores de Cuestionarios"
description: "Conozca las plataformas de cuestionarios que puede utilizar con AutoProctor para exámenes en línea supervisados."
---

AutoProctor es una plataforma de supervisión con inteligencia artificial que monitorea a los candidatos durante las evaluaciones en línea. Usted proporciona su propio cuestionario, y AutoProctor se encarga de la supervisión.

Hay dos opciones:

1. **Use la herramienta de cuestionarios propia de AutoProctor ([Socratease](socratease/create-questions/why-socratease.md))** — usted crea y configura las preguntas, los puntos y la calificación directamente dentro de AutoProctor.
2. **Use un proveedor de cuestionarios externo** (Google Forms, Microsoft Forms, TypeForm, etc.) — sus preguntas, puntos y configuraciones permanecen en esa plataforma. AutoProctor solo agrega la supervisión.

## Elegir un Proveedor de Cuestionarios

{% embed url="../../videos/creating-tests/all-test-types.mp4" %}
Cómo crear un examen con diferentes proveedores de cuestionarios en AutoProctor. Solo puede seleccionar un proveedor por examen
{% endembed %}

{% stepper %}
{% step %}
### Cree un Nuevo Examen
Vaya a su [**Panel de Control**](https://www.autoproctor.co/test-admin/home/) y haga clic en **Crear Examen**.
{% endstep %}
{% step %}
### Seleccione un Proveedor de Cuestionarios
Elija uno de los proveedores disponibles: **Cuestionarios Socratease**, **Google Forms**, **Microsoft Forms** o **IFrame/Otros**.
{% endstep %}
{% step %}
### Configure la Supervisión
Configure el [temporizador](tests-results/create/timer-settings.md) y las [opciones de supervisión](tests-results/create/proctoring-settings.md). Si eligió Socratease, también configura las preguntas y la calificación dentro de AutoProctor. Para proveedores externos, el contenido del cuestionario permanece en esa plataforma.
{% endstep %}
{% endstepper %}

## Proveedores de Cuestionarios Disponibles

| Proveedor | Ideal Para | Ventaja Principal |
|---|---|---|
| **Cuestionarios Socratease** | Evaluaciones con funciones completas | Integración nativa con protección de envío automático |
| **Google Forms** | Usuarios existentes de Google Forms | Complemento dedicado para creación automática de exámenes |
| **Microsoft Forms** | Organizaciones del ecosistema Microsoft | Integración fluida para evaluaciones empresariales |
| **IFrame/Otros** | TypeForm, ProProfs, ClassMarker, etc. | Agrega supervisión a cualquier plataforma de cuestionarios basada en la web |

### Cuestionarios Socratease

Socratease es la herramienta nativa de cuestionarios de AutoProctor. Proporciona la integración más estrecha y la mejor experiencia para el candidato:

- **Botón de envío único** que previene la pérdida de respuestas por secuenciación incorrecta
- **Protección de envío automático** que guarda las respuestas antes de que el examen se cierre
- **Múltiples tipos de preguntas** incluyendo opción múltiple, ensayos, respuestas de voz, programación y más
- **Importación masiva desde Excel** y bancos de preguntas para un ensamblaje rápido del cuestionario

### Google Forms

Google Forms es la plataforma de cuestionarios más utilizada. AutoProctor ofrece un [**complemento dedicado para Google Forms**](https://workspace.google.com/marketplace/app/timer_+_proctor_google_forms_autoproctor/691377974459) que crea un examen supervisado directamente desde su Google Form.

### Microsoft Forms

Microsoft Forms es la segunda plataforma más utilizada, especialmente dentro de organizaciones que dependen del ecosistema Microsoft para evaluaciones internas y procesos de contratación.

### IFrame/Otros Proveedores

Existen cientos de plataformas de cuestionarios, incluyendo TypeForm, ProProfs y ClassMarker. Aunque estas plataformas no tienen supervisión remota integrada, puede agregar la supervisión de AutoProctor a cualquiera de ellas seleccionando la opción **IFrame/Otros**. AutoProctor incorpora su cuestionario dentro de una ventana de navegador supervisada.

{% hint style="info" %}
Al usar proveedores IFrame/Otros, puede personalizar la URL incorporada usando [argumentos de consulta](tests-results/create/iframe-query-arguments.md).
{% endhint %}

## Recursos Relacionados

- [¿Por Qué Socratease?](socratease/create-questions/why-socratease.md) — Beneficios de usar la herramienta nativa de cuestionarios de AutoProctor
- [Cómo Crear un Cuestionario de Socratease](socratease/create-questions/creating-a-quiz.md) — Guía de creación paso a paso
- [Configuración del Temporizador](tests-results/create/timer-settings.md) — Configure la duración del examen y las ventanas de tiempo
- [Configuración de Supervisión](tests-results/create/proctoring-settings.md) — Opciones de cámara, micrófono y cambio de pestaña
- [Argumentos de Consulta del IFrame](tests-results/create/iframe-query-arguments.md) — Personalice las URL de cuestionarios incorporados
- [Configuración Avanzada](tests-results/create/advanced-settings.md) — Proveedores de inicio de sesión, colaboradores y más

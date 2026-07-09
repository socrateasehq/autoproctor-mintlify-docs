---
title: "Configuración de Supervisión"
description: "Configure la detección de cambio de pestaña, el monitoreo de cámara, la grabación de micrófono, el modo de pantalla completa obligatorio y otras opciones de supervisión."
---

La Configuración de Supervisión controla lo que AutoProctor monitorea durante un examen — desde el cambio de pestaña y la detección de cámara hasta el modo de pantalla completa obligatorio y la captura de fotos aleatorias. Estos ajustes determinan con qué nivel de rigor se supervisa a los candidatos.


![Panel de configuración de supervisión](../../images/creating-tests/proctoring-settings.png)
*Panel de configuración de supervisión*

{% hint style="info" %}
Para activar la supervisión, debe marcar la casilla **Activar Supervisión** en la sección de Configuración Principal. Si la supervisión está desactivada, ninguno de estos ajustes se aplica.
{% endhint %}

## Opciones Básicas de Supervisión

| Configuración | Qué Hace |
|---|---|
| **Cambio de Pestaña** | Detecta cuando un candidato cambia a una pestaña o aplicación diferente del navegador. Captura una captura de pantalla de la pestaña a la que cambió. |
| **Detectar Múltiples Monitores** | Detecta si un candidato ha conectado monitores externos a su computadora. |
| **Cámara** | Detecta si no hay ningún rostro visible en la cámara, o si hay múltiples rostros visibles. Captura fotos como evidencia. |
| **Micrófono** | Monitorea el entorno sonoro y graba audio cuando se detecta ruido. |
| **Fotos Aleatorias** | Captura algunas fotos aleatorias durante el examen a intervalos aleatorios. |
| **Pantalla Completa Obligatoria** | Obliga a los candidatos a realizar el examen en modo de pantalla completa. Salir del modo de pantalla completa se registra como una infracción. |
| **Exigir Escritorio** | Requiere que los candidatos usen una computadora de escritorio o portátil. El examen no se cargará en tabletas o dispositivos móviles. |
| **Foto Antes del Inicio del Examen** | Captura una foto del candidato antes de que comience el examen. |
| **Personalizar Mensaje** | Personalice el mensaje que ven los candidatos cuando se les pide tomar una foto antes del examen. Use esto para pedir a los candidatos que muestren su documento de identidad. |

{% hint style="info" %}
La opción **Personalizar Mensaje** es una función Premium.
{% endhint %}


## Supervisión Avanzada

La supervisión avanzada agrega medidas adicionales contra el fraude. Cada función avanzada requiere **4 créditos adicionales por intento**.

![Panel de supervisión avanzada](../../images/creating-tests/enhanced-proctoring.png)
*Panel de supervisión avanzada*

| Función | Qué Hace | Créditos |
|---|---|---|
| **Verificación de Documento de Identidad** | El candidato sube un documento de identidad (credencial estudiantil, pasaporte, licencia de conducir, identificación oficial) con su foto y nombre visibles. AutoProctor lo verifica contra la Foto Antes del Inicio del Examen y el nombre que ingresó. | 4 por intento |
| **Detección de Suplantación** | Detecta si alguien diferente al candidato original está realizando el examen. | 4 por intento |
| **Dispositivo Auxiliar (360°)** | El candidato empareja su teléfono con su computadora portátil para supervisión de 360 grados. También ayuda a detectar herramientas de IA que muestran respuestas como superposiciones en pantalla. | 4 por intento |
| **Grabación de Sesión** | Graba la pantalla y las acciones del candidato, incluyendo clics del ratón y entrada del teclado. | 4 por intento |


## Configuración de Comunicación

Estos ajustes controlan cómo se maneja la evidencia de infracciones:

- **Para mí después del Examen** — Almacena evidencia (fotos, audio, capturas de pantalla) para revisión posterior. Mantenga esto activado a menos que tenga una razón específica para desactivarlo.
- **Al usuario durante el Examen** — Notifica al candidato durante el examen cuando se detecta una infracción. Esto ayuda a los candidatos a corregir problemas inofensivos (como música de fondo que activa una infracción de ruido).

![Panel de configuración de comunicación](../../images/settings/communication-settings.png)
*Panel de configuración de comunicación*

{% hint style="info" %}
Recomendamos mantener ambas configuraciones de comunicación activadas para la mejor experiencia de supervisión.
{% endhint %}

## Recursos Relacionados

- [Configuración del Temporizador](tests-results/create/timer-settings.md) — Configure la duración del examen y las ventanas de tiempo
- [Supervisión Avanzada](tests-results/create/enhanced-proctoring.md) — Guía detallada sobre verificación de identidad, detección de suplantación y supervisión de 360°
- [Configuración del Cuestionario](socratease/settings/quiz-settings.md) — Para configuraciones específicas de cuestionarios Socratease, consulte la página de Configuración del Cuestionario de Socratease
- [Qué Se Monitorea](understanding/how-proctoring-works/what-gets-tracked.md) — Lista completa de todo lo que AutoProctor supervisa
- [Resultados de Supervisión](tests-results/results/proctoring-results.md) — Cómo revisar los datos de supervisión después de un examen
- [Puntaje de Confianza](understanding/how-proctoring-works/trust-score.md) — Cómo se calcula el puntaje de confianza a partir de los datos de supervisión

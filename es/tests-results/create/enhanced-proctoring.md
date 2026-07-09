---
title: "Supervisión Avanzada"
description: "Configure la verificación de documento de identidad, la detección de suplantación, la supervisión de 360 grados y la grabación de sesión para una protección avanzada contra el fraude."
---

La Supervisión Avanzada agrega funciones avanzadas de verificación de identidad y monitoreo más allá de la supervisión estándar. Estas funciones ayudan a prevenir la suplantación de identidad, detectar herramientas de IA y crear un registro completo de cada intento de examen.

![Panel de configuración de supervisión avanzada](images/creating-tests/enhanced-proctoring.png)

{% hint style="info" %}
Cada función de supervisión avanzada requiere **4 créditos adicionales por intento**. Si activa múltiples funciones avanzadas, el costo de créditos es acumulativo. Por ejemplo, activar Verificación de Documento de Identidad y Grabación de Sesión cuesta 8 créditos adicionales por intento de candidato.
{% endhint %}

## Funciones Disponibles

### Verificación de Documento de Identidad

La Verificación de Documento de Identidad confirma la identidad del candidato comparando su documento de identidad cargado con su foto del examen y el nombre ingresado.

{% stepper %}
{% step %}
### Active la Verificación de Documento de Identidad
Active la opción **Verificación de Documento de Identidad** en la sección de Supervisión Avanzada de la configuración de su examen.
{% endstep %}
{% step %}
### El candidato sube su documento de identidad
Al iniciar el examen, se le pide al candidato que suba una foto de su documento de identidad. Los documentos aceptados incluyen credenciales estudiantiles, pasaportes, licencias de conducir e identificaciones oficiales.
{% endstep %}
{% step %}
### AutoProctor verifica la identidad
El sistema compara la foto y el nombre en el documento de identidad con la Foto Antes del Inicio del Examen y el nombre que el candidato ingresó en la plataforma.
{% endstep %}
{% endstepper %}

![Pantalla de verificación de identidad antes de iniciar el examen](images/taking-tests/id-verification.png)
*Pantalla de verificación de identidad antes de iniciar el examen*

{% hint style="info" %}
La **Foto Antes del Inicio del Examen** debe estar activada en la configuración de supervisión básica para que la Verificación de Documento de Identidad funcione eficazmente.
{% endhint %}

### Detección de Suplantación

La Detección de Suplantación monitorea si alguien diferente al candidato original intenta o continúa el examen. AutoProctor compara las fotos periódicas tomadas durante el examen con la foto inicial para detectar cambios de rostro.

![Evidencia de suplantación en el informe](images/taking-tests/impersonation-detected.png)
*Evidencia de suplantación en el informe*

### Dispositivo Auxiliar (Supervisión de 360°)

La función de Dispositivo Auxiliar permite la supervisión de 360 grados al emparejar el teléfono del candidato con su computadora portátil. Esto proporciona un ángulo de cámara secundario que captura el entorno físico del candidato.

{% stepper %}
{% step %}
### Active el Dispositivo Auxiliar
Active la opción **Dispositivo Auxiliar** en la configuración de Supervisión Avanzada.
{% endstep %}
{% step %}
### El candidato empareja su teléfono
Cuando comienza el examen, el candidato escanea un código QR en la pantalla de su computadora portátil usando la cámara de su teléfono. Esto empareja los dos dispositivos.

![Pantalla de emparejamiento del dispositivo auxiliar antes de iniciar el examen](images/taking-tests/aux-device.png)
*Pantalla de emparejamiento del dispositivo auxiliar antes de iniciar el examen*
{% endstep %}
{% step %}
### El teléfono proporciona monitoreo secundario
La cámara del teléfono captura el escritorio, el entorno y la pantalla del candidato desde un ángulo diferente. Esto también ayuda a detectar herramientas de IA que muestran respuestas como superposiciones en la pantalla.
{% endstep %}
{% endstepper %}

![Capturas de evidencia del dispositivo auxiliar](images/taking-tests/aux-device-evidence.png)
*Capturas de evidencia del dispositivo auxiliar*

### Grabación de Sesión

La Grabación de Sesión captura un registro completo de la actividad de pantalla del candidato durante todo el examen, incluyendo clics del ratón y entrada del teclado. Esto crea una línea de tiempo revisable de todo el intento de examen.


[Pruebe la demostración de supervisión avanzada](https://www.autoproctor.co/tests/aux-demo/) para ver estas funciones en acción antes de activarlas en su examen.

## Resumen de Costos de Créditos

| Función | Créditos por Intento |
|---|---|
| Verificación de Documento de Identidad | 4 |
| Detección de Suplantación | 4 |
| Dispositivo Auxiliar (360°) | 4 |
| Grabación de Sesión | 4 |
| Las 4 funciones combinadas | 12 (25% de descuento por paquete) |

## Recursos Relacionados

- [Configuración de Supervisión](tests-results/create/proctoring-settings.md) — Opciones básicas de supervisión (cámara, micrófono, cambio de pestaña)
- [Puntaje de Confianza](understanding/how-proctoring-works/trust-score.md) — Cómo los datos de supervisión avanzada afectan el puntaje de confianza
- [Resultados de Supervisión](tests-results/results/proctoring-results.md) — Revisión de resultados de supervisión avanzada
- [Acceder a Respuestas y Entregas del Candidato](tests-results/results/individual-submissions.md) — Visualización de datos detallados para cada candidato
- [Pagos y Créditos](pricing-account/plans-credits/payments-and-credits.md) — Comprenda el uso de créditos y las compras
- [Funciones Elite](pricing-account/plans-credits/elite-features.md) — Descripción general de las funciones Premium y Elite

---
title: "Qué Se Monitorea Durante la Supervisión"
description: "Conozca las fuentes de datos, las capacidades de detección y el registro de evidencia disponibles en el sistema de supervisión de AutoProctor."
---

AutoProctor monitorea a los candidatos en tiempo real utilizando inteligencia artificial directamente en el dispositivo y captura evidencia solo cuando detecta una infracción. Esto significa que usted revisa incidentes señalados en lugar de horas de grabación.

<Frame caption="Un informe de supervisión de ejemplo que muestra el Puntaje de Confianza, el recuento de infracciones y los eventos señalados con evidencia">
  ![Informe de supervisión de ejemplo](images/getting-started/sample-proctoring-report.png)
</Frame>

[Vea resultados de supervisión de ejemplo](https://www.autoproctor.co/sample-dashboard/) para explorar un informe en vivo.

## Fuentes de Datos

AutoProctor puede acceder a las siguientes fuentes en el dispositivo del candidato:

| Fuente | Qué Hace |
|---|---|
| **Cámara** | Monitorea el rostro y el entorno del candidato |
| **Micrófono** | Detecta ruido de fondo y señales de audio |
| **Pantalla compartida** | Captura la actividad de la pantalla durante el examen |
| **Cámara de dispositivo auxiliar** | Monitorea a través de un dispositivo secundario emparejado (por ejemplo, un teléfono) |

{% hint style="info" %}
Las fuentes a las que AutoProctor accede dependen completamente de cómo configure cada examen. Usted activa o desactiva cada fuente en su [configuración de supervisión](tests-results/create/proctoring-settings.md).
{% endhint %}

## Qué Detecta y Registra AutoProctor

A diferencia de las plataformas de supervisión tradicionales que graban sesiones completas de video y audio, AutoProctor detecta infracciones y le muestra evidencia solo de esas infracciones — para que usted no dedique horas revisando el intento de cada candidato.

| Función de Detección | Qué Hace |
|---|---|
| **Detección de audio de fondo** | Registra ruido y señales de audio del micrófono |
| **Detección facial** | Captura fotos cuando no se detecta ningún rostro o se detectan múltiples rostros en la cámara |
| **Cambio de pestaña/aplicación** | Captura capturas de pantalla cuando los candidatos cambian de pestaña o aplicación |
| **Fotos aleatorias** | Toma fotos a intervalos aleatorios durante el examen |
| **Detección de múltiples monitores** | Identifica cuándo se conectan pantallas adicionales al dispositivo |
| **Captura facial previa al examen** | Toma una foto del rostro del candidato antes de que comience el examen |
| **Modo de pantalla completa obligatorio** | Asegura que el examen se ejecute en modo de pantalla completa y señala las salidas |
| **Registro de acciones de sesión** | Registra clics del ratón y actividad del teclado durante el examen |
| **Emparejamiento de dispositivo auxiliar** | Monitorea a través de un teléfono emparejado para detectar el uso del teclado, asegurando que los candidatos no estén usando ChatGPT u otras herramientas para hacer trampa |

{% hint style="info" %}
Todas las funciones de seguimiento son configurables por examen. Active solo lo que necesite en su [configuración de supervisión](tests-results/create/proctoring-settings.md).
{% endhint %}

## Cómo Configurar el Seguimiento

{% stepper %}
{% step %}
### Abra la configuración de su examen
Vaya a su [panel de control de AutoProctor](https://www.autoproctor.co/test-admin/home/), seleccione un examen y haga clic en **Configuración**.


{% endstep %}
{% step %}
### Navegue a Configuración de Supervisión
Haga clic en la pestaña **Configuración de Supervisión** para ver todas las opciones de seguimiento disponibles.


{% endstep %}
{% step %}
### Active las funciones que necesite
Active o desactive cada función de seguimiento según sus requisitos. Por ejemplo, puede activar el monitoreo de cámara y la detección de cambio de pestaña pero dejar desactivado el monitoreo de micrófono.


{% endstep %}
{% step %}
### Guarde su configuración
Haga clic en **Guardar** para aplicar sus cambios. Estos ajustes surten efecto inmediatamente para todos los intentos de examen futuros.
{% endstep %}
{% endstepper %}

{% embed url="videos/getting-started/configure-proctor-settings.mp4" %}
Cómo configurar los ajustes de supervisión en AutoProctor
{% endembed %}

{% hint style="warning" %}
Activar más funciones de seguimiento aumenta la carga de procesamiento en el dispositivo del candidato. Si sus candidatos usan hardware antiguo, considere activar solo las funciones que más necesite. Consulte [Compatibilidad de Dispositivos](understanding/getting-started/device-compatibility.md) para los requisitos mínimos.
{% endhint %}

## Recursos Relacionados

- [Puntaje de Confianza](understanding/how-proctoring-works/trust-score.md) — Cómo AutoProctor califica la integridad del candidato
- [Configuración de Supervisión](tests-results/create/proctoring-settings.md) — Configure qué funciones de supervisión activar
- [Supervisión Avanzada](tests-results/create/enhanced-proctoring.md) — Opciones de monitoreo avanzadas para mayor seguridad
- [Resultados de Supervisión](tests-results/results/proctoring-results.md) — Vea la evidencia de infracciones y los informes
- [Grabación de Video](understanding/how-proctoring-works/video-recording.md) — Por qué AutoProctor no graba video completo
- [Compatibilidad de Dispositivos](understanding/getting-started/device-compatibility.md) — Navegadores y dispositivos compatibles

---
title: "Compatibilidad de Dispositivos"
description: "Verifique qué navegadores, sistemas operativos y dispositivos son compatibles para realizar exámenes supervisados en AutoProctor."
---

AutoProctor ejecuta algoritmos de monitoreo con inteligencia artificial directamente en el dispositivo del candidato, lo cual requiere funciones específicas del navegador y capacidad de procesamiento adecuada. Antes de realizar un examen supervisado, los candidatos deben confirmar que su navegador y dispositivo cumplen con los requisitos mínimos indicados a continuación.

## Navegadores y Dispositivos Compatibles

| Sistema Operativo | Navegador | Versión Mínima |
|---|---|---|
| Windows | Chrome | 82 |
| Windows | Firefox | 78 |
| Windows | Edge | 88 |
| Linux | Chrome | 82 |
| macOS | Safari | 12 |
| macOS | Chrome | 82 |
| macOS | Firefox | 78 |
| Android | Chrome | 82 |
| iOS (iPad/iPhone) | Safari | 14.1 |
| iOS (iPad/iPhone) OS 16.1+ | Chrome | 82 |

{% hint style="warning" %}
Cualquier combinación de navegador y sistema operativo **no incluida** en la tabla anterior no es compatible. Los candidatos que utilicen configuraciones no compatibles (por ejemplo, Brave en Windows u Opera en Android) pueden experimentar fallos de carga o funcionalidades de supervisión defectuosas.
{% endhint %}

## Cómo Verificar Su Dispositivo

{% stepper %}
{% step %}
### Abra el enlace del examen de demostración
Visite el examen de demostración para confirmar que su dispositivo y navegador son compatibles:

[Realizar el Examen de Demostración](https://autoproctor.co/tests/bj0yv14Ufu/load/)


{% endstep %}
{% step %}
### Otorgue permisos de cámara, micrófono y pantalla compartida
Cuando se le solicite, permita que su navegador acceda a la cámara y al micrófono. También se le pedirá que comparta su pantalla — seleccione **Pantalla completa** y haga clic en **Compartir**. Si alguno de estos permisos falla, su navegador o dispositivo podría no ser compatible.

<div style={{display: "flex", flexDirection: "column", gap: "16px", alignItems: "center"}}>
  <div style={{display: "flex", gap: "16px", justifyContent: "center"}}>
    ![Solicitud de permiso del navegador para acceso al micrófono en autoproctor.co](../../images/getting-started/audio-permission.png)
*Solicitud de permiso para el micrófono*
    ![Solicitud de permiso del navegador para acceso a la cámara en autoproctor.co](../../images/getting-started/video-permission.png)
*Solicitud de permiso para la cámara*
  </div>
  ![Solicitud del navegador para compartir la pantalla completa con autoproctor.co](../../images/getting-started/screen-share-permission.png)
*Solicitud de permiso para compartir pantalla*
</div>
{% endstep %}
{% step %}
### Complete la demostración
Complete el examen de demostración para confirmar que todas las funciones de supervisión se cargan correctamente, incluyendo la vista previa de la cámara, el aviso de pantalla compartida y el modo de pantalla completa.


{% endstep %}
{% endstepper %}

{% hint style="info" %}
El examen de demostración no consume créditos de examen de ninguna cuenta. Los candidatos pueden realizarlo tantas veces como necesiten.
{% endhint %}

## Problemas Comunes de Compatibilidad

| Problema | Causa Probable | Solución |
|---|---|---|
| El examen se queda en la pantalla de carga | Navegador no compatible o versión desactualizada | Actualice el navegador o cambie a Chrome |
| Cámara no detectada | Permisos del navegador bloqueados | Permita el acceso a la cámara en la configuración del navegador |
| El examen funciona lentamente o con retrasos | Dispositivo demasiado antiguo o con pocos recursos | Cierre otras aplicaciones o use un dispositivo más nuevo |
| No aparece el aviso de pantalla compartida | El navegador no admite la API de captura de pantalla | Cambie a Chrome o Edge en escritorio |

## Recursos Relacionados

- [El Examen Se Queda en la Pantalla de Carga](tests-results/issues/loading-screen.md) — Solucione problemas de carga
- [Examen Lento o con Retrasos](tests-results/issues/slow-and-laggy.md) — Solucione problemas de rendimiento
- [Página en Blanco o Pantalla Gris](tests-results/issues/blank-page-grey-screen.md) — Resuelva problemas de visualización
- [Instrucciones para Exámenes Supervisados](candidate-guide/attempting/proctored-test-instructions.md) — Lo que los candidatos necesitan saber antes de comenzar
- [Mejores Prácticas para Creadores de Exámenes](understanding/getting-started/best-practices-for-teachers.md) — Consejos incluyendo compartir el examen de demostración con anticipación

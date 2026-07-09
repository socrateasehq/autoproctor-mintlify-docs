---
title: "Argumentos de Consulta del IFrame"
description: "Agregue parámetros de consulta a las URL de iframe en la Configuración Avanzada de AutoProctor para personalizar el contenido incorporado."
---

Al usar el proveedor de cuestionarios **IFrame/Otros**, puede agregar parámetros de consulta a la URL de su cuestionario incorporado a través de la **Configuración Avanzada** de AutoProctor. Esto le permite personalizar cómo se comporta el contenido incorporado — por ejemplo, forzar un idioma específico o habilitar el modo incorporado — sin modificar la URL original.

## Cómo Funciona

AutoProctor construye la URL final agregando sus argumentos de consulta a la URL original del cuestionario. Usted proporciona solo los parámetros; AutoProctor agrega el prefijo `?` automáticamente.

{% embed url="videos/settings/query-arguments.mp4" %}
Cómo usar argumentos de consulta en la Configuración Avanzada de AutoProctor
{% endembed %}

{% stepper %}
{% step %}
### Abra la Configuración Avanzada
Navegue a su examen y abra la sección de **Configuración Avanzada**.
{% endstep %}
{% step %}
### Ingrese Sus Argumentos de Consulta
Escriba sus parámetros en el campo **Argumentos de Consulta**. Use el formato `key1=val1&key2=val2`.
{% endstep %}
{% step %}
### Guarde la Configuración
Guarde la configuración de su examen. AutoProctor agrega sus parámetros a la URL del cuestionario al renderizar el iframe.
{% endstep %}
{% endstepper %}

### Ejemplo

Si su URL original es:

```
www.website.com
```

Y usted ingresa lo siguiente en el campo **Argumentos de Consulta**:

```
key1=val1&key2=val2
```

AutoProctor renderiza el iframe como:

```
www.website.com?key1=val1&key2=val2
```

{% hint style="info" %}
No incluya el prefijo `?` en sus argumentos de consulta. AutoProctor lo agrega automáticamente al construir la URL.
{% endhint %}

## Parámetros Comunes

| Parámetro | Propósito | Ejemplo de Uso |
|---|---|---|
| `hl=en` | Establecer el idioma a inglés | Renderizar un Google Form en inglés para candidatos internacionales |
| `hl=fr` | Establecer el idioma a francés | Renderizar un Google Form en francés |
| `embedded=true` | Forzar modo incorporado | Asegurar que ciertas plataformas se muestren correctamente dentro del iframe |

## Recursos Relacionados

- [Proveedores de Cuestionarios](tests-results/create/quiz-providers.md) — Todas las plataformas de cuestionarios compatibles
- [Configuración Avanzada](tests-results/create/advanced-settings.md) — Proveedores de inicio de sesión, colaboradores y otras opciones avanzadas
- [Configuración del Temporizador](tests-results/create/timer-settings.md) — Configure la duración del examen y las ventanas de tiempo
- [Configuración de Supervisión](tests-results/create/proctoring-settings.md) — Opciones de cámara, micrófono y cambio de pestaña

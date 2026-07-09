---
title: "Invitar Candidatos por Correo Electrónico"
description: "Genere enlaces de invitación únicos vinculados a direcciones de correo electrónico específicas para un acceso controlado al examen con verificación de correo electrónico en AutoProctor."
---

Los enlaces de invitación únicos le permiten generar una URL de examen distinta para cada candidato, vinculada a su dirección de correo electrónico. Cuando un candidato abre su enlace, AutoProctor envía un código de verificación de un solo uso para confirmar su identidad antes de conceder acceso al examen.

{% hint style="info" %}
Esta función solo está disponible en el **Plan Elite** y funciona exclusivamente con **Cuestionarios Socratease** y **Exámenes con IFrame**. No es compatible con Google Forms ni con Microsoft Forms, ya que estos requieren un inicio de sesión específico de la plataforma. Consulte [Pagos y Créditos](pricing-account/plans-credits/payments-and-credits.md) para detalles del plan.
{% endhint %}

## Cómo Configurar los Enlaces de Invitación Únicos

{% embed url="videos/settings/unique-invitation-links.mp4" %}
Cómo configurar los enlaces de invitación únicos en AutoProctor
{% endembed %}

{% stepper %}
{% step %}
### Active la URL Única
Abra la configuración de su examen y active la opción **URL Única**.


{% endstep %}
{% step %}
### Cargue las direcciones de correo electrónico
Cargue las direcciones de correo electrónico de los candidatos mediante un archivo CSV. Puede cargar un máximo de 1,000 direcciones de correo electrónico a la vez.


{% endstep %}
{% step %}
### Obtenga los enlaces generados
AutoProctor genera una salida de texto que contiene las direcciones de correo electrónico y sus correspondientes enlaces de examen únicos como columnas separadas por comas.


{% endstep %}
{% step %}
### Formatee los datos
Pegue la salida en una aplicación de hojas de cálculo y divida por el separador de comas para organizar las direcciones de correo electrónico y los enlaces en columnas separadas.
{% endstep %}
{% step %}
### Distribuya los enlaces
Envíe los enlaces únicos a sus candidatos por correo electrónico, su sistema de gestión de aprendizaje u otro método de distribución.
{% endstep %}
{% endstepper %}

## Cómo Funciona la Verificación

Cuando un candidato hace clic en su enlace único, AutoProctor envía un código de verificación de un solo uso a la dirección de correo electrónico asociada con ese enlace. El candidato debe ingresar este código para acceder al examen. Esto asegura que solo el destinatario previsto pueda usar cada enlace.


## Limitaciones Importantes

| Limitación | Detalles |
|---|---|
| URL estándar desactivada | Una vez que active esta función, la URL compartida estándar del examen deja de funcionar. Solo las URLs únicas por candidato otorgan acceso. |
| Sin revocación | No puede invalidar las invitaciones enviadas después de que se generen. |
| Sin prueba gratuita | Esta función no se puede probar antes de adquirir el Plan Elite. |
| Límite por lote | Puede cargar un máximo de 1,000 direcciones de correo electrónico a la vez. |

{% hint style="warning" %}
Después de activar las URLs únicas, el enlace común del examen deja de funcionar inmediatamente. Asegúrese de estar preparado para distribuir los enlaces individuales antes de activar esta función.
{% endhint %}

## Servicio de Envío Masivo de Correo Electrónico

Para campañas a gran escala que superen los 5,000 candidatos, AutoProctor ofrece un servicio de distribución de correo electrónico a $100 por cada 5,000 mensajes. Esto requiere saldo suficiente en la cuenta y el envío de su archivo CSV y el contenido del correo electrónico al equipo de AutoProctor. [Contáctenos](pricing-account/support/contact-us.md) para más detalles.

## Recursos Relacionados

- [Restringir el Acceso al Examen por Dirección de Correo Electrónico](tests-results/access-limits/restricting-by-email.md) — Método alternativo mediante restricciones de dominio de correo electrónico
- [Restringir a Candidatos Específicos](tests-results/access-limits/restricting-to-some-users.md) — Descripción general de todos los métodos de control de acceso
- [Métodos de Inicio de Sesión del Candidato](candidate-guide/attempting/candidate-login-methods.md) — Conozca las opciones de autenticación
- [Pagos y Créditos](pricing-account/plans-credits/payments-and-credits.md) — Detalles del plan y funciones del Plan Elite
- [Funciones Elite](pricing-account/plans-credits/elite-features.md) — Todas las funciones disponibles en el Plan Elite

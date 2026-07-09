---
title: "Métodos de Inicio de Sesión para Candidatos"
description: "Conozca las opciones de inicio de sesión disponibles para los candidatos que realizan exámenes en AutoProctor, incluyendo qué métodos de inicio de sesión funcionan con cada proveedor de cuestionarios."
---

Los candidatos deben iniciar sesión antes de intentar cualquier examen en AutoProctor. El inicio de sesión es necesario para que AutoProctor pueda diferenciar entre los envíos individuales cuando varios candidatos utilizan el mismo enlace de examen.

<iframe
  className="w-full aspect-video rounded-xl"
  src="https://www.youtube.com/embed/T9iZvk35sOc?si=ZKozRVlwbxXIiHqQ&rel=0"
  title="Tutorial de inicio de sesión del candidato en AutoProctor"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerPolicy="strict-origin-when-cross-origin"
  allowFullScreen
></iframe>

![Opciones de inicio de sesión de AutoProctor mostrando los botones de inicio de sesión con Google, Microsoft y correo electrónico](../../images/taking-tests/login-methods.png)
*Pantalla de inicio de sesión de AutoProctor*

## Métodos de Inicio de Sesión Disponibles

AutoProctor ofrece tres opciones de inicio de sesión para los candidatos:

- **Iniciar sesión con Google** -- utiliza la cuenta de Google del candidato
- **Iniciar sesión con Microsoft** -- utiliza la cuenta de Microsoft del candidato
- **Iniciar sesión con correo electrónico** -- el candidato introduce su dirección de correo electrónico directamente (no se requiere cuenta de terceros)

## Métodos de Inicio de Sesión por Proveedor de Cuestionarios

Los métodos de inicio de sesión disponibles dependen del proveedor de cuestionarios que utilice:

| Proveedor de Cuestionarios | Métodos de Inicio de Sesión Disponibles |
|---|---|
| Cuestionarios de Socratease | Google, Microsoft, correo electrónico |
| Google Forms | Solo Google |
| Microsoft Forms | Solo Microsoft |
| Exámenes IFrame | Google, Microsoft, correo electrónico |

{% hint style="info" %}
Los exámenes de Google Forms requieren inicio de sesión con Google porque AutoProctor necesita transmitir la identidad de Google del candidato al formulario. Lo mismo aplica para Microsoft Forms con el inicio de sesión de Microsoft. Los exámenes de Socratease e IFrame no tienen esta restricción, por lo que los tres métodos de inicio de sesión están disponibles.
{% endhint %}

{% hint style="info" %}
Para restringir qué candidatos pueden iniciar sesión en su examen, consulte [Restricción por Correo Electrónico](tests-results/access-limits/restricting-by-email.md). Puede limitar el acceso a direcciones de correo electrónico o dominios de correo electrónico específicos.
{% endhint %}

## Recursos Relacionados

- [Cómo Cerrar Sesión](candidate-guide/attempting/how-to-logout.md) -- Cambiar entre cuentas
- [Restricción por Correo Electrónico](tests-results/access-limits/restricting-by-email.md) -- Limitar quién puede acceder a su examen
- [Restricción a Algunos Usuarios](tests-results/access-limits/restricting-to-some-users.md) -- Controlar el acceso al examen para usuarios específicos
- [Invitar Candidatos por Correo Electrónico](tests-results/access-limits/inviting-candidates-via-email.md) -- Enviar invitaciones de examen directamente
- [Página de Instrucciones para Candidatos](tests-results/create/instructions-page-for-candidates.md) -- Lo que los candidatos ven antes de comenzar un examen
- [Contáctenos](pricing-account/support/contact-us.md) -- Comuníquese si necesita más ayuda

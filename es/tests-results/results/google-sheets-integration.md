---
title: "Escribir Resultados en Google Sheets"
description: "Configure la exportación automática de resultados de exámenes de AutoProctor a Google Sheets para que los datos fluyan en tiempo real sin descargas manuales."
---

En lugar de descargar archivos de Excel manualmente después de cada examen, puede configurar AutoProctor para que escriba automáticamente los resultados del examen en una hoja de Google Sheets. Los resultados aparecen en la hoja a medida que los candidatos completan sus exámenes, manteniendo sus datos actualizados sin esfuerzo adicional.

{% hint style="info" %}
Esta es una **Función Premium** y requiere una suscripción Premium o Elite. Consulte [Pagos y Créditos](pricing-account/plans-credits/payments-and-credits.md) para detalles del plan.
{% endhint %}

## Instrucciones de Configuración

![GIF mostrando cómo configurar la integración con Google Sheets en AutoProctor](images/settings/write-to-gsheet.gif)
*Configurando la integración con Google Sheets*

{% stepper %}
{% step %}
### Abra la configuración del examen
Visite la **Configuración del Examen** de un examen nuevo o existente en su [panel de AutoProctor](https://www.autoproctor.co/test-admin/home/).
{% endstep %}
{% step %}
### Ubique el campo ID de Google Sheets
Desplácese hacia abajo hasta la sección **Configuración Avanzada** y ubique el campo **Google Sheets ID**.
{% endstep %}
{% step %}
### Cree una hoja de Google Sheets en blanco
Cree una hoja de Google Sheets vacía en su Google Drive. Utilizará esta hoja para recibir los resultados de AutoProctor.
{% endstep %}
{% step %}
### Conceda acceso de escritura
Comparta la hoja de Google Sheets con `hello@autoproctor.co` y otorgue permisos de **Editor**. Esto permite que AutoProctor escriba datos en la hoja.

{% hint style="warning" %}
Si no comparte la hoja con `hello@autoproctor.co` como Editor, AutoProctor no podrá escribir resultados en ella. Asegúrese de otorgar acceso de Editor, no solo de Lector.
{% endhint %}
{% endstep %}
{% step %}
### Pegue la URL de la hoja de Google Sheets
Copie la URL de su hoja de Google Sheets y péguela en el campo **Google Sheets ID** en la configuración del examen de AutoProctor.
{% endstep %}
{% step %}
### Guarde el examen
Haga clic en **Crear** o **Actualizar** para guardar la configuración del examen.
{% endstep %}
{% step %}
### Verifique la integración
Complete un intento de examen. Aparecerá automáticamente una nueva pestaña denominada **AutoProctor** en su hoja de Google Sheets con los datos de resultados.
{% endstep %}
{% endstepper %}

Los intentos de examen posteriores llenan automáticamente la misma hoja de Google Sheets sin necesidad de configuración adicional.

## Integración con Socratease Quizzes

Para Socratease Quizzes, el sistema escribe tanto las puntuaciones de supervisión como las puntuaciones del cuestionario en la hoja. Sin embargo, las preguntas y respuestas individuales no se incluyen -- solo aparecen los datos de puntuación agregados.

{% hint style="info" %}
Si necesita datos detallados a nivel de pregunta para Socratease Quizzes, utilice la vista de [entregas individuales](tests-results/results/individual-submissions.md) en el [panel de AutoProctor](https://www.autoproctor.co/test-admin/home/).
{% endhint %}

## Recursos Relacionados

- [Exportar a Excel](tests-results/results/export-to-excel.md) -- Descargar resultados manualmente como hoja de cálculo
- [Acceder a Respuestas y Entregas del Candidato](tests-results/results/individual-submissions.md) -- Ver respuestas detalladas por candidato
- [¿Dónde Puedo Ver los Resultados de Mi Examen?](tests-results/results/how-to-see-results.md) -- Descripción general de los resultados del examen frente a los resultados de supervisión
- [Pagos y Créditos](pricing-account/plans-credits/payments-and-credits.md) -- Detalles del plan y disponibilidad de funciones
- [Compartir Resultados del Examen](tests-results/results/sharing-test-results.md) -- Conceder a otros usuarios acceso a los resultados del examen

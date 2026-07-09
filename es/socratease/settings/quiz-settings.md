---
title: "Configuración de Cuestionarios Socratease"
description: "Configure su cuestionario Socratease con opciones de modo de visualización, visibilidad de resultados, aleatorización y más."
---

Socratease tiene su propio conjunto de opciones configurables, distintas de la configuración general de Temporizador y Supervisión de AutoProctor. Estas opciones controlan cómo se comporta el cuestionario para sus candidatos — desde cómo aparecen las preguntas hasta si los candidatos pueden copiar y pegar.


## Opciones Disponibles

### 1. Modo de Visualización de Preguntas (Premium)

Controle cómo aparecen las preguntas para los candidatos: todas a la vez (estilo Google Forms), una por una con navegación (estilo Typeform), o una por una sin navegación. Esta configuración también afecta cómo funcionan los temporizadores.

Para más detalles, consulte [Modo de Visualización de Preguntas](socratease/settings/question-display-mode.md).

### 2. Visibilidad de Resultados

Controle cuándo los candidatos ven sus puntuaciones y resultados:
- **Inmediatamente** después del envío
- **Cuando usted publique las puntuaciones individuales** (un candidato a la vez)
- **Cuando usted publique todas las puntuaciones** (todos a la vez)
- **Nunca** — los resultados se retienen por completo

Para más detalles, consulte [Mostrar Resultados a los Candidatos](socratease/settings/showing-results-to-candidates.md).

### 3. Aleatorización de Preguntas

Aleatorice el orden de las preguntas para cada candidato. Lo que el Candidato 1 ve como Pregunta 1 puede ser la Pregunta 10 para el Candidato 2. Esto reduce la oportunidad de que los candidatos compartan respuestas durante un examen.

{% hint style="info" %}
Esta opción solo está disponible cuando usa el modo [Todas a la vez (estilo Google Forms)](socratease/settings/question-display-mode.md).
{% endhint %}


### 4. Mezcla de Opciones

Para las preguntas de tipo MCQ y MCA, puede aleatorizar el orden de las opciones de respuesta entre los candidatos. Incluso si dos candidatos ven la misma pregunta, las opciones aparecen en un orden diferente.


### 5. Restricción de Copiar y Pegar

Cuando activa esta configuración, los candidatos no pueden copiar el texto de las preguntas del cuestionario ni pegar texto desde otra pestaña o aplicación en el cuestionario. Esto reduce la dependencia de herramientas externas y asistentes de IA.


### 6. Envío Automático por Cambio de Pestaña

Establezca el número máximo de cambios de pestaña permitidos durante el examen. Si un candidato excede este límite, su examen se envía automáticamente. Esto disuade a los candidatos de cambiar a otras pestañas para buscar respuestas.

{% hint style="warning" %}
Cuando un examen se envía automáticamente debido a los límites de cambio de pestaña, el candidato no puede reanudar el examen. Asegúrese de comunicar la política de cambio de pestaña a sus candidatos de antemano.
{% endhint %}


### 7. Instrucciones Personalizadas

Agregue indicaciones generales sobre el examen que se muestran a los candidatos antes de comenzar el cuestionario. Úselas para comunicar reglas, instrucciones o expectativas importantes.

{% hint style="info" %}
Las instrucciones personalizadas solo están disponibles cuando usa el modo de visualización de preguntas **todas a la vez**.
{% endhint %}


### 8. Soporte de LaTeX

Si desea incluir ecuaciones matemáticas, escríbalas usando la sintaxis LaTeX y se renderizarán automáticamente como ecuaciones formateadas. Active esta configuración para habilitar la representación de LaTeX en su cuestionario.

Para más detalles, consulte [Uso de LaTeX para Ecuaciones Matemáticas](socratease/settings/latex-math-equations.md).

## Cómo Acceder a la Configuración del Cuestionario

{% embed url="../../videos/socratease/soc-quiz-settings.mp4" %}
Cómo acceder y configurar los ajustes del cuestionario Socratease
{% endembed %}

{% stepper %}
{% step %}
### Abra Su Cuestionario
Abra el Cuestionario Socratease que desea configurar desde su [panel de control de AutoProctor](https://www.autoproctor.co/test-admin/home/).
{% endstep %}
{% step %}
### Haga Clic en el Ícono de Configuración
Haga clic en el ícono de **Configuración** (engranaje) en la barra de herramientas del editor del cuestionario.
{% endstep %}
{% step %}
### Ajuste Sus Opciones
Modifique cualquiera de las ocho opciones listadas anteriormente. Los cambios se guardan automáticamente.
{% endstep %}
{% endstepper %}

## Recursos Relacionados

- [Modo de Visualización de Preguntas](socratease/settings/question-display-mode.md) — Explicación detallada de las opciones de visualización
- [Mostrar Resultados a los Candidatos](socratease/settings/showing-results-to-candidates.md) — Controle la visibilidad de los resultados
- [Uso de LaTeX para Ecuaciones Matemáticas](socratease/settings/latex-math-equations.md) — Agregue ecuaciones matemáticas a sus cuestionarios
- [Configuración del Temporizador](tests-results/create/timer-settings.md) — Para la configuración general de temporizador y supervisión del examen (separada de la configuración del cuestionario Socratease)
- [Crear un Cuestionario](socratease/create-questions/creating-a-quiz.md) — Guía paso a paso para crear un cuestionario

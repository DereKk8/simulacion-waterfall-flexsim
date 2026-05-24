# Proyecto #3: Aplicación de Simulación de Eventos Discretos al Desarrollo de Software mediante Metodologías Ágiles

## Contexto del Proyecto
Una empresa de desarrollo de software ha registrado durante un año completo (365 días) el comportamiento operativo de sus equipos de trabajo. La información recopilada incluye:
* Llegada de tareas.
* Tiempos de desarrollo.
* Eventos de calidad.
* Recursos disponibles.
* Productividad diaria.
* Métricas ágiles preliminares.

**Objetivo empresarial:** Evaluar el desempeño de diferentes metodologías ágiles y tradicionales para decidir cuál implementar en futuros proyectos.

---

## Base de Datos (BD) Entregada
Se proporciona un archivo Excel con datos históricos en bruto que contiene:
* **Eventos diarios:** Bugs, cambios de requisitos, hotfixes, etc.
* **Tareas nuevas por día.**
* **Tipo y complejidad** de las tareas.
* **Recursos disponibles:** Desarrolladores (Developers) y personal de control de calidad (QA).
* **Tiempos:** Registro de tiempos de desarrollo, QA y retrabajo.

---

## Asignación de Metodologías por Integrantes
Cada grupo deberá diseñar, modelar y simular el sistema bajo una metodología específica para analizar cómo cambia el desempeño de la organización:

* **Cascada (Waterfall)**

---

## Pasos para la Aplicación de la Simulación

### 1. Análisis de Datos y Entrada
A partir del dataset, el grupo debe:
* Calcular frecuencias de eventos.
* Estimar probabilidades de ocurrencia.
* Identificar patrones de comportamiento.
* Ajustar distribuciones de probabilidad para: tiempos de llegada, tiempos de desarrollo, tiempos de QA y retrabajo.

### 2. Modelado en FlexSim
Construir un modelo en FlexSim que represente fielmente la metodología seleccionada. Debe incluir de forma obligatoria:
* **Flujo del proceso** de desarrollo.
* **Entidades:** Tareas, bugs e historias de usuario.
* **Recursos:** Colas, bloqueos, desarrolladores y QA.
* **Reglas de prioridad:** Configuradas según la metodología elegida.
* **Dinámicas del entorno:** Llegada de nuevas tareas, aparición de bugs, cambios de requisitos y saturación de QA.

### 3. Definición de Escenarios
Cada grupo debe ejecutar y comparar un mínimo de **2 escenarios**:
* **Escenario A (Base):** Sistema operando de forma estándar según la metodología seleccionada, utilizando los parámetros calculados desde los datos históricos.
* **Escenario B (Mejora o Estrés):** Modificación de variables para optimización o prueba de resistencia (ej. aumento de tareas, reducción de QA, incremento de bugs, adición de desarrolladores, etc.).

---

## Entregables y Sustentación

### Estructura de la Presentación (Tipo Artículo Científico)
Los resultados se expondrán en una presentación ejecutiva que simule la estructura de un *paper* académico, utilizando herramientas de IA (como Elicit, Consensus, Research Rabbit o Scispace) para la revisión bibliográfica:
1. Resumen
2. Introducción
3. Revisión de literatura
4. Metodología
5. Resultados
6. Discusión
7. Conclusiones
8. Referencias (Mínimo 10 fuentes)

### Requisitos de la Sustentación
* **Duración:** 25 minutos de presentación + 10 minutos de preguntas.
* **Código de vestimenta:** Business casual.
* **Archivos a entregar:**
  * Archivos de análisis de datos (Excel o Python).
  * Archivo FlexSim del modelo base (Escenario A).
  * Archivo FlexSim de los escenarios modificados (Escenario B).
  * Presentación en PowerPoint con todo lo solicitado.

---

## Rúbrica de Evaluación

| Criterio | Excelente (5 pts) | Bueno (4 pts) | Aceptable (3 pts) | Insuficiente (1-2 pts) | Peso |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Análisis de datos y definición de parámetros** | Datos completos, precisos y bien organizados para ambas franjas horarias. Modelo adecuado, cálculos precisos y explicados claramente. Incluye tablas, gráficos/diagramas elaborados que apoyan el análisis. | Datos adecuados con mínimas omisiones o errores leves. Modelo adecuado con cálculos mayormente correctos. Tablas y gráficos claros, pero que son mejorables. | Datos básicos, con algunas inconsistencias o faltas menores. Modelo correcto con errores menores en cálculos, tablas y visualizaciones básicas, poco explicadas. | Datos incompletos, poco claros o incorrectos. Modelo inapropiado o con cálculos erróneos. Visualizaciones o visualizaciones insuficientes o ausentes. | **15%** |
| **Aplicación del modelo, cálculos, tablas y visualizaciones** | Modelado excelente en FlexSim. Flujos, lógicas de prioridad y recursos perfectamente alineados con la metodología elegida y los datos. | Modelado correcto en FlexSim. Representa bien la metodología con mínimos detalles lógicos por pulir. | Modelado básico. El flujo en FlexSim presenta bloqueos o inconsistencias con la metodología real. | Modelo de FlexSim incompleto, no corre, o no representa en absoluto la metodología asignada. | **40%** |
| **Análisis comparativo entre escenarios** | Análisis profundo y crítico, con interpretación clara y uso adecuado de datos visuales. | Análisis claro con interpretación razonable y algunos datos visuales. | Análisis superficial o incompleto con pocas visualizaciones o datos. | Análisis ausente, irrelevante o erróneo. | **15%** |
| **Propuesta de mejora** | Propuesta bien fundamentada, realista, basada en resultados y análisis previos. | Propuesta adecuada y justificada, con base en los datos obtenidos. | Propuesta básica, poco justificada o con conexión débil a los datos. | Propuesta no viable, poco clara o sin justificación. | **15%** |
| **Redacción y formato académico** | Artículo/Presentación estructurado, con buena redacción, referencias y uso correcto de herramientas. | Buen formato y redacción, con mínimas faltas y referencias correctas. | Artículo con errores de formato o redacción, referencias limitadas. | Artículo mal redactado, sin estructura ni referencias adecuadas. | **15%** |

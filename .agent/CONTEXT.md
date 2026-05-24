# CONTEXT — Proyecto #3: Simulación de Eventos Discretos (Waterfall)

## 1. Objetivo del Proyecto

Modelar y simular en **FlexSim** el proceso de desarrollo de software bajo la metodología **Cascada (Waterfall)**, usando datos históricos reales (365 días) de una empresa de desarrollo. Evaluar desempeño comparando **2 escenarios** (base vs. mejora/estrés) para decidir qué metodología conviene implementar.

## 2. Dataset

**Archivo:** `base_agile_sin_bloqueos.xlsx` (1 hoja: `Datos`, 365 filas + cabecera, 25 columnas)

| Columna | Descripción |
|---|---|
| Fecha | 2025-01-01 a 2025-12-31 |
| Tareas_Nuevas | Tareas que llegan por día (min=2, max=21, avg=11.57) |
| Tipo_Tarea | Feature (185), Bug (75), Refactor (66), Hotfix (39) |
| Prioridad | Media (165), Alta (91), Baja (71), Critica (38) |
| Proyecto | Web (98), Data (101), Backend (86), Mobile (80) |
| Complejidad | Escala 1–10 (avg=5.6) |
| Bugs_QA | Bugs detectados en QA por día (81 días con >0) |
| Cambio_Requisitos | Días con cambios de req (52 días) |
| Hotfix_Urgente | Hotfixes urgentes (27 días) |
| Saturacion_QA | Días con saturación de QA (66 días) |
| Ausencia_Recurso | Días con ausencias (38 días) |
| Repriorizacion_Backlog | Días con repriorización (65 días) |
| Retrabajo_Flag | Días con retrabajo (88 días) |
| Horas_Retrabajo | Horas de retrabajo |
| Developers_Disponibles | Rango 3–7, avg=5.1 |
| QA_Disponibles | Rango 1–3, avg=2.1 |
| Horas_Extra | Horas extra |
| Tiempo_Desarrollo_Horas | Rango 6.43–17.77, avg=11.19 |
| Tiempo_QA_Horas | Rango 2.02–5.99, avg=4.01 |
| Cantidad_Bugs | Bugs totales por día (rango 0–8, avg=2.89, total=1,055) |
| Tareas_Completadas | Rango 0–20, avg=8.69, total=3,173 |
| Sprint | 1–27 (sprints de ~13.5 días) |
| WIP | Rango 3–14, avg=8.7 |
| Lead_Time_Horas | Rango 8.85–24.70, avg=15.83 |
| Cycle_Time_Horas | Rango 8.85–22.56, avg=15.21 |

## 3. Metodología Asignada: Cascada (Waterfall)

El modelo debe representar el flujo secuencial clásico:

1. **Requisitos** → 2. **Diseño** → 3. **Implementación** → 4. **Verificación (QA)** → 5. **Mantenimiento**

Reglas clave del modelo:
- Cada fase debe completarse antes de pasar a la siguiente (sin solapamiento).
- Prioridad de tareas según metodología Waterfall (requisitos primero, luego diseño, etc.).
- Bugs y cambios de requisitos pueden generar retrabajo (regreso a fases anteriores).
- Hotfixes urgentes pueden interrumpir el flujo (prioridad máxima).
- Recursos: Developers y QA con capacidad limitada.
- Colas y bloqueos por saturación de QA.

## 4. Escenarios a Simular

### Escenario A (Base)
- Parámetros calculados directamente del dataset histórico.
- Distribuciones de probabilidad ajustadas a: tiempos de llegada, desarrollo, QA, retrabajo.
- Frecuencias de eventos según datos observados.

### Escenario B (Mejora o Estrés)
- Modificación de una o más variables. Opciones sugeridas:
  - Aumentar/disminuir desarrolladores o QA.
  - Incrementar tasa de llegada de tareas.
  - Reducir tiempos de desarrollo (mejora de productividad).
  - Aumentar tasa de bugs o cambios de requisitos.
  - Simular ausencia de recursos.

## 5. Entregables

| Archivo | Descripción |
|---|---|
| Analisis_Datos.xlsx / .py | Script/herramienta de análisis de datos y ajuste de distribuciones |
| Modelo_FlexSim_EscenarioA.fsm | Modelo base con parámetros históricos |
| Modelo_FlexSim_EscenarioB.fsm | Modelo modificado (estrés/mejora) |
| Presentacion.pptx | Presentación estilo paper científico (8 secciones, ≥10 referencias) |

## 6. Estructura de Presentación (Paper Científico)

1. Resumen
2. Introducción
3. Revisión de literatura (usar Elicit, Consensus, Research Rabbit o Scispace)
4. Metodología
5. Resultados (Escenario A vs B)
6. Discusión
7. Conclusiones
8. Referencias (≥10 fuentes)

## 7. Rúbrica de Evaluación (Pesos)

| Criterio | Peso |
|---|---|
| Análisis de datos y definición de parámetros | 15% |
| Aplicación del modelo FlexSim (flujos, prioridades, recursos) | 40% |
| Análisis comparativo entre escenarios | 15% |
| Propuesta de mejora | 15% |
| Redacción y formato académico | 15% |

## 8. Próximos Pasos

1. Análisis exploratorio del dataset (distribuciones, frecuencias, correlaciones).
2. Ajuste de distribuciones de probabilidad (llegadas, desarrollo, QA, retrabajo).
3. Construcción del modelo FlexSm — Escenario A.
4. Validación del modelo contra datos históricos.
5. Definición y construcción del Escenario B.
6. Ejecución de simulaciones y recolección de métricas (Lead Time, Cycle Time, Throughput, WIP, Utilización).
7. Análisis comparativo y propuesta de mejora.
8. Preparación de presentación y referencias bibliográficas.

# Simulación Waterfall FlexSim

Simulación de eventos discretos con FlexSim de un proceso de desarrollo software bajo metodología Cascada (Waterfall), usando datos históricos reales (365 días).

## Requisitos

- Python 3.8+
- Dependencias: `pip install pandas numpy scipy matplotlib`

## Ejecutar análisis de datos

```bash
python analisis_datos.py .agent/base_agile_sin_bloqueos.xlsx
```

Esto genera:

| Archivo | Descripción |
|---------|-------------|
| `resultados_analisis.txt` | Frecuencias, probabilidades, distribuciones ajustadas |
| `analisis_visualizacion.png` | 6 subplots: estacionalidad, tipos de tarea, histogramas, tendencia semanal, retrabajo |
| `distribuciones_ajustadas.png` | 4 histogramas con curvas de densidad ajustadas |

## Estructura del proyecto

```
.
├── analisis_datos.py          # Script de análisis estadístico
├── articulo-cientifico.tex    # Artículo LaTeX (Metodología + Resultados de Entrada)
├── resultados_analisis.txt    # Output: frecuencias y distribuciones
├── analisis_visualizacion.png # Output: visualización de patrones
├── distribuciones_ajustadas.png # Output: histogramas ajustados
├── .agent/
│   ├── CONTEXT.md             # Contexto del proyecto
│   ├── PROMPTS.md             # Prompts de trabajo
│   ├── Proyecto 3 2026-10.md  # Enunciado del proyecto
│   └── base_agile_sin_bloqueos.xlsx  # Datos históricos (365 días)
└── README.md
```

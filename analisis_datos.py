#!/usr/bin/env python3
"""
Script de análisis de datos para simulación de eventos discretos (Waterfall).
Calcula frecuencias, probabilidades, patrones y ajusta distribuciones de probabilidad.

Uso: python analisis_datos.py <ruta_al_archivo_csv>
"""

import sys
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


def cargar_datos(ruta_archivo):
    """Carga datos desde CSV o Excel."""
    if ruta_archivo.endswith('.csv'):
        df = pd.read_csv(ruta_archivo, parse_dates=['Fecha'])
    elif ruta_archivo.endswith('.xlsx'):
        df = pd.read_excel(ruta_archivo, parse_dates=['Fecha'])
    else:
        raise ValueError("Formato no soportado. Use CSV o XLSX.")
    
    print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")
    return df


def calcular_frecuencias_eventos(df):
    """
    Calcula frecuencias de eventos por día.
    
    Eventos analizados:
    - Tareas nuevas que llegan
    - Tareas completadas
    - Bugs detectados en QA
    - Días con retrabajo
    - Días con cambios de requisitos
    - Hotfixes urgentes
    """
    print("\n" + "="*60)
    print("FRECUENCIAS DE EVENTOS POR DÍA")
    print("="*60)
    
    frecuencias = {
        'Tareas_Nuevas': df['Tareas_Nuevas'].sum(),
        'Tareas_Completadas': df['Tareas_Completadas'].sum(),
        'Bugs_QA_Total': df['Bugs_QA'].sum(),
        'Dias_Con_Retrabajo': (df['Retrabajo_Flag'] > 0).sum(),
        'Dias_Con_Cambio_Requisitos': (df['Cambio_Requisitos'] > 0).sum(),
        'Dias_Con_Hotfix_Urgente': (df['Hotfix_Urgente'] > 0).sum(),
        'Dias_Con_Saturacion_QA': (df['Saturacion_QA'] > 0).sum(),
    }
    
    print("\nFrecuencia total de eventos en 365 días:")
    for evento, frecuencia in frecuencias.items():
        print(f"  {evento}: {frecuencia}")
    
    print("\nFrecuencia promedio por día:")
    total_dias = len(df)
    for evento, frecuencia in frecuencias.items():
        if evento.startswith('Dias_'):
            prob = frecuencia / total_dias
            print(f"  {evento}: {frecuencia} días ({prob:.2%})")
        else:
            promedio = frecuencia / total_dias
            print(f"  {evento}: {promedio:.2f} eventos/día")
    
    return frecuencias


def estimar_probabilidades(df):
    """
    Estima probabilidades de ocurrencia de eventos del sistema.
    """
    print("\n" + "="*60)
    print("PROBABILIDADES DE OCURRENCIA")
    print("="*60)
    
    total_dias = len(df)
    
    probabilidades = {
        'P(Retrabajo)': (df['Retrabajo_Flag'] > 0).sum() / total_dias,
        'P(Cambio_Requisitos)': (df['Cambio_Requisitos'] > 0).sum() / total_dias,
        'P(Hotfix_Urgente)': (df['Hotfix_Urgente'] > 0).sum() / total_dias,
        'P(Saturacion_QA)': (df['Saturacion_QA'] > 0).sum() / total_dias,
        'P(Ausencia_Recurso)': (df['Ausencia_Recurso'] > 0).sum() / total_dias,
        'P(Repriorizacion)': (df['Repriorizacion_Backlog'] > 0).sum() / total_dias,
    }
    
    print("\nProbabilidades diarias:")
    for evento, prob in probabilidades.items():
        print(f"  {evento}: {prob:.4f} ({prob:.2%})")
    
    print("\nProbabilidades por tipo de tarea:")
    tipos = df['Tipo_Tarea'].value_counts()
    for tipo, count in tipos.items():
        print(f"  P({tipo}): {count/total_dias:.4f} ({count/total_dias:.2%})")
    
    print("\nProbabilidades por prioridad:")
    prioridades = df['Prioridad'].value_counts()
    for prioridad, count in prioridades.items():
        print(f"  P({prioridad}): {count/total_dias:.4f} ({count/total_dias:.2%})")
    
    return probabilidades


def identificar_patrones(df):
    """
    Identifica patrones de comportamiento clave en los datos históricos.
    
    Patrones buscados:
    - Estacionalidad (variación por mes/semana)
    - Ráfagas (bursts de alta actividad)
    - Clústeres (agrupamiento de eventos)
    """
    print("\n" + "="*60)
    print("PATRONES DE COMPORTAMIENTO")
    print("="*60)
    
    df['Mes'] = df['Fecha'].dt.month
    df['Semana'] = df['Fecha'].dt.isocalendar().week
    df['Dia_Semana'] = df['Fecha'].dt.dayofweek
    
    print("\n1. ESTACIONALIDAD MENSUAL:")
    print("-" * 40)
    
    mensual = df.groupby('Mes').agg({
        'Tareas_Nuevas': 'mean',
        'Tareas_Completadas': 'mean',
        'Bugs_QA': 'mean',
        'Tiempo_Desarrollo_Horas': 'mean',
        'Tiempo_QA_Horas': 'mean'
    })
    
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
             'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    
    print("\nTareas nuevas promedio por mes:")
    for mes in mensual.index:
        nombre = meses[mes - 1] if mes <= 12 else f'Mes {mes}'
        print(f"  {nombre}: {mensual.loc[mes, 'Tareas_Nuevas']:.2f}")
    
    print("\n2. RÁFAGAS (BURSTS) DE ACTIVIDAD:")
    print("-" * 40)
    
    umbral_ráfaga = df['Tareas_Nuevas'].mean() + 2 * df['Tareas_Nuevas'].std()
    dias_ráfaga = df[df['Tareas_Nuevas'] > umbral_ráfaga]
    print(f"Umbral de ráfaga: >{umbral_ráfaga:.2f} tareas/día")
    print(f"Días con ráfagas: {len(dias_ráfaga)} ({len(dias_ráfaga)/len(df)*100:.1f}%)")
    
    if len(dias_ráfaga) > 0:
        print(f"  Máximo en ráfaga: {dias_ráfaga['Tareas_Nuevas'].max()} tareas")
        print(f"  Promedio en ráfaga: {dias_ráfaga['Tareas_Nuevas'].mean():.2f} tareas")
    
    umbral_bugs = df['Cantidad_Bugs'].mean() + 2 * df['Cantidad_Bugs'].std()
    dias_bugs = df[df['Cantidad_Bugs'] > umbral_bugs]
    print(f"\nUmbral de ráfaga de bugs: >{umbral_bugs:.2f} bugs/día")
    print(f"Días con ráfaga de bugs: {len(dias_bugs)} ({len(dias_bugs)/len(df)*100:.1f}%)")
    
    print("\n3. CLÚSTERES DE RETRABAJO:")
    print("-" * 40)
    
    df_ordenado = df.sort_values('Fecha').reset_index(drop=True)
    df_ordenado['Retrabajo_Seq'] = (df_ordenado['Retrabajo_Flag'] > 0).astype(int)
    
    clusters = []
    cluster_actual = 0
    en_cluster = False
    
    for i, row in df_ordenado.iterrows():
        if row['Retrabajo_Seq'] == 1:
            if not en_cluster:
                cluster_actual += 1
                en_cluster = True
            clusters.append(cluster_actual)
        else:
            en_cluster = False
            clusters.append(0)
    
    df_ordenado['Cluster_ID'] = clusters
    num_clusters = df_ordenado[df_ordenado['Cluster_ID'] > 0]['Cluster_ID'].nunique()
    
    print(f"Número de clústeres de retrabajo identificados: {num_clusters}")
    
    if num_clusters > 0:
        tamanos_cluster = df_ordenado[df_ordenado['Cluster_ID'] > 0].groupby('Cluster_ID').size()
        print(f"Tamaño promedio de clúster: {tamanos_cluster.mean():.2f} días")
        print(f"Tamaño máximo de clúster: {tamanos_cluster.max()} días consecutivos")
    
    print("\n4. CORRELACIONES IMPORTANTES:")
    print("-" * 40)
    
    correlaciones = df[['Tareas_Nuevas', 'Complejidad', 'Bugs_QA', 'Retrabajo_Flag',
                        'Tiempo_Desarrollo_Horas', 'Tiempo_QA_Horas', 
                        'Developers_Disponibles', 'QA_Disponibles']].corr()
    
    print("\nCorrelación entre Tareas_Nuevas y Tareas_Completadas:")
    corr = df['Tareas_Nuevas'].corr(df['Tareas_Completadas'])
    print(f"  r = {corr:.3f}")
    
    print("\nCorrelación entre Complejidad y Tiempo_Desarrollo_Horas:")
    corr = df['Complejidad'].corr(df['Tiempo_Desarrollo_Horas'])
    print(f"  r = {corr:.3f}")
    
    print("\nCorrelación entre Bugs_QA y Retrabajo_Flag:")
    corr = df['Bugs_QA'].corr(df['Retrabajo_Flag'])
    print(f"  r = {corr:.3f}")
    
    return df


def ajustar_distribuciones(df):
    """
    Ajusta distribuciones de probabilidad para:
    1. Tiempos de llegada de nuevas tareas
    2. Tiempos de desarrollo (horas)
    3. Tiempos de QA (horas)
    4. Tiempos y tasas de retrabajo
    """
    print("\n" + "="*60)
    print("AJUSTE DE DISTRIBUCIONES DE PROBABILIDAD")
    print("="*60)
    
    resultados = {}
    
    distribuciones_continuas = [
        stats.expon,
        stats.weibull_min,
        stats.lognorm,
        stats.gamma,
        stats.norm
    ]
    
    nombres_dist = ['Exponencial', 'Weibull', 'Lognormal', 'Gamma', 'Normal']
    
    def mejor_ajuste(datos, nombre_variable):
        """Encuentra la mejor distribución para un conjunto de datos."""
        datos = np.array(datos[datos > 0])
        
        if len(datos) < 10:
            return None, None, None
        
        resultados_ajuste = []
        
        for dist in distribuciones_continuas:
            try:
                params = dist.fit(datos)
                ks_stat, p_valor = stats.kstest(datos, dist.cdf, args=params)
                resultados_ajuste.append({
                    'dist': dist,
                    'params': params,
                    'ks': ks_stat,
                    'p': p_valor,
                    'aic': len(datos) * np.log(ks_stat) + 2 * len(params)
                })
            except:
                continue
        
        if not resultados_ajuste:
            return None, None, None
        
        mejor = min(resultados_ajuste, key=lambda x: x['ks'])
        idx = distribuciones_continuas.index(mejor['dist'])
        
        return nombres_dist[idx], mejor['params'], mejor['ks']
    
    print("\n1. TIEMPO ENTRE LLEGADAS DE TAREAS:")
    print("-" * 40)
    
    llegadas_diarias = df['Tareas_Nuevas'].values
    
    lambda_llegada = np.mean(llegadas_diarias)
    print(f"Promedio de tareas por día (λ): {lambda_llegada:.2f}")
    print(f"Desviación estándar: {np.std(llegadas_diarias):.2f}")
    
    dist_nombre, params, ks = mejor_ajuste(llegadas_diarias, "Tareas_Nuevas")
    if dist_nombre:
        print(f"Mejor distribución: {dist_nombre}")
        print(f"Parámetros: {params}")
        print(f"Estadístico KS: {ks:.4f}")
        resultados['llegadas'] = {'dist': dist_nombre, 'params': params, 'lambda': lambda_llegada}
    
    print("\n2. TIEMPO DE DESARROLLO (HORAS):")
    print("-" * 40)
    
    tiempo_desarrollo = df['Tiempo_Desarrollo_Horas'].values
    print(f"Media: {np.mean(tiempo_desarrollo):.2f} horas")
    print(f"Desviación estándar: {np.std(tiempo_desarrollo):.2f} horas")
    print(f"Mínimo: {np.min(tiempo_desarrollo):.2f} horas")
    print(f"Máximo: {np.max(tiempo_desarrollo):.2f} horas")
    
    dist_nombre, params, ks = mejor_ajuste(tiempo_desarrollo, "Tiempo_Desarrollo")
    if dist_nombre:
        print(f"Mejor distribución: {dist_nombre}")
        print(f"Parámetros: {params}")
        print(f"Estadístico KS: {ks:.4f}")
        resultados['desarrollo'] = {'dist': dist_nombre, 'params': params}
    
    print("\n3. TIEMPO DE QA (HORAS):")
    print("-" * 40)
    
    tiempo_qa = df['Tiempo_QA_Horas'].values
    print(f"Media: {np.mean(tiempo_qa):.2f} horas")
    print(f"Desviación estándar: {np.std(tiempo_qa):.2f} horas")
    print(f"Mínimo: {np.min(tiempo_qa):.2f} horas")
    print(f"Máximo: {np.max(tiempo_qa):.2f} horas")
    
    dist_nombre, params, ks = mejor_ajuste(tiempo_qa, "Tiempo_QA")
    if dist_nombre:
        print(f"Mejor distribución: {dist_nombre}")
        print(f"Parámetros: {params}")
        print(f"Estadístico KS: {ks:.4f}")
        resultados['qa'] = {'dist': dist_nombre, 'params': params}
    
    print("\n4. TIEMPO DE RETRABAJO (HORAS):")
    print("-" * 40)
    
    tiempo_retrabajo = df[df['Retrabajo_Flag'] > 0]['Horas_Retrabajo'].values
    print(f"Días con retrabajo: {len(tiempo_retrabajo)}")
    print(f"Media: {np.mean(tiempo_retrabajo):.2f} horas")
    print(f"Desviación estándar: {np.std(tiempo_retrabajo):.2f} horas")
    
    if len(tiempo_retrabajo) >= 10:
        dist_nombre, params, ks = mejor_ajuste(tiempo_retrabajo, "Horas_Retrabajo")
        if dist_nombre:
            print(f"Mejor distribución: {dist_nombre}")
            print(f"Parámetros: {params}")
            print(f"Estadístico KS: {ks:.4f}")
            resultados['retrabajo_tiempo'] = {'dist': dist_nombre, 'params': params}
    
    print("\n5. TASA DE RETRABAJO:")
    print("-" * 40)
    
    tasa_retrabajo = (df['Retrabajo_Flag'] > 0).sum() / len(df)
    print(f"Probabilidad de retrabajo: {tasa_retrabajo:.4f} ({tasa_retrabajo:.2%})")
    print(f"Distribución: Bernoulli(p={tasa_retrabajo:.4f})")
    resultados['retrabajo_tasa'] = {'dist': 'Bernoulli', 'p': tasa_retrabajo}
    
    print("\n6. CANTIDAD DE BUGS:")
    print("-" * 40)
    
    bugs = df['Cantidad_Bugs'].values
    print(f"Media: {np.mean(bugs):.2f} bugs/día")
    print(f"Varianza: {np.var(bugs):.2f}")
    print(f"Índice de dispersión (var/mean): {np.var(bugs)/np.mean(bugs):.2f}")
    
    lambda_bugs = np.mean(bugs)
    print(f"Distribución sugerida: Poisson(λ={lambda_bugs:.2f})")
    
    dist_nombre, params, ks = mejor_ajuste(bugs, "Cantidad_Bugs")
    if dist_nombre:
        print(f"Mejor distribución (continua): {dist_nombre}")
        print(f"Parámetros: {params}")
    resultados['bugs'] = {'dist': 'Poisson', 'lambda': lambda_bugs}
    
    return resultados


def crear_visualizaciones(df, resultados):
    """
    Crea visualizaciones básicas de los análisis.
    """
    print("\n" + "="*60)
    print("GENERANDO VISUALIZACIONES")
    print("="*60)
    
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    fig.suptitle('Análisis de Datos - Simulación Waterfall', fontsize=16, fontweight='bold')
    
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, 10))
    
    ax1 = axes[0, 0]
    df['Mes'] = df['Fecha'].dt.month
    mensual = df.groupby('Mes')['Tareas_Nuevas'].mean()
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
             'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    ax1.bar(mensual.index, mensual.values, color=colors[0])
    ax1.set_xlabel('Mes')
    ax1.set_ylabel('Tareas Nuevas (promedio)')
    ax1.set_title('Estacionalidad: Tareas Nuevas por Mes')
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(meses, rotation=45)
    ax1.grid(axis='y', alpha=0.3)
    
    ax2 = axes[0, 1]
    tipos = df['Tipo_Tarea'].value_counts()
    ax2.bar(tipos.index, tipos.values, color=colors[1:5])
    ax2.set_xlabel('Tipo de Tarea')
    ax2.set_ylabel('Frecuencia')
    ax2.set_title('Distribución por Tipo de Tarea')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(axis='y', alpha=0.3)
    
    ax3 = axes[1, 0]
    ax3.hist(df['Tiempo_Desarrollo_Horas'], bins=20, color=colors[5], edgecolor='black', alpha=0.7)
    ax3.axvline(df['Tiempo_Desarrollo_Horas'].mean(), color='red', linestyle='--', 
                label=f'Media: {df["Tiempo_Desarrollo_Horas"].mean():.2f}h')
    ax3.set_xlabel('Tiempo de Desarrollo (horas)')
    ax3.set_ylabel('Frecuencia')
    ax3.set_title('Distribución: Tiempo de Desarrollo')
    ax3.legend()
    ax3.grid(axis='y', alpha=0.3)
    
    ax4 = axes[1, 1]
    ax4.hist(df['Tiempo_QA_Horas'], bins=20, color=colors[6], edgecolor='black', alpha=0.7)
    ax4.axvline(df['Tiempo_QA_Horas'].mean(), color='red', linestyle='--',
                label=f'Media: {df["Tiempo_QA_Horas"].mean():.2f}h')
    ax4.set_xlabel('Tiempo de QA (horas)')
    ax4.set_ylabel('Frecuencia')
    ax4.set_title('Distribución: Tiempo de QA')
    ax4.legend()
    ax4.grid(axis='y', alpha=0.3)
    
    ax5 = axes[2, 0]
    df['Semana'] = df['Fecha'].dt.isocalendar().week
    semanal = df.groupby('Semana')['Tareas_Nuevas'].sum()
    ax5.plot(semanal.index, semanal.values, marker='o', linewidth=2, markersize=4, color=colors[7])
    ax5.axhline(df['Tareas_Nuevas'].mean() * 7, color='red', linestyle='--', 
                label=f'Promedio semanal: {df["Tareas_Nuevas"].mean()*7:.1f}')
    ax5.set_xlabel('Semana del Año')
    ax5.set_ylabel('Tareas Nuevas')
    ax5.set_title('Tendencia Semanal: Tareas Nuevas')
    ax5.legend()
    ax5.grid(alpha=0.3)
    
    ax6 = axes[2, 1]
    retrabajo_por_tipo = df.groupby('Tipo_Tarea')['Retrabajo_Flag'].mean() * 100
    ax6.bar(retrabajo_por_tipo.index, retrabajo_por_tipo.values, color=colors[8])
    ax6.set_xlabel('Tipo de Tarea')
    ax6.set_ylabel('Porcentaje de Retrabajo (%)')
    ax6.set_title('Tasa de Retrabajo por Tipo de Tarea')
    ax6.tick_params(axis='x', rotation=45)
    ax6.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('analisis_visualizacion.png', dpi=150, bbox_inches='tight')
    print("Visualización guardada: analisis_visualizacion.png")
    
    fig2, axes2 = plt.subplots(2, 2, figsize=(12, 10))
    fig2.suptitle('Distribuciones de Probabilidad Ajustadas', fontsize=14, fontweight='bold')
    
    datos_y_titulos = [
        (df['Tareas_Nuevas'].values, 'Tareas Nuevas por Día', axes2[0, 0]),
        (df['Tiempo_Desarrollo_Horas'].values, 'Tiempo de Desarrollo (horas)', axes2[0, 1]),
        (df['Tiempo_QA_Horas'].values, 'Tiempo de QA (horas)', axes2[1, 0]),
        (df[df['Retrabajo_Flag'] > 0]['Horas_Retrabajo'].values, 'Horas de Retrabajo', axes2[1, 1])
    ]
    
    for datos, titulo, ax in datos_y_titulos:
        datos = datos[datos > 0]
        ax.hist(datos, bins=15, density=True, alpha=0.6, color='lightblue', edgecolor='black')
        
        x = np.linspace(datos.min(), datos.max(), 100)
        
        if 'Tiempo' in titulo or 'Horas' in titulo:
            for dist_func, nombre in [(stats.expon, 'Exponencial'), 
                                       (stats.weibull_min, 'Weibull'),
                                       (stats.lognorm, 'Lognormal')]:
                try:
                    params = dist_func.fit(datos)
                    ax.plot(x, dist_func.pdf(x, *params), label=nombre, linewidth=2)
                except:
                    pass
        
        ax.set_xlabel('Valor')
        ax.set_ylabel('Densidad de Probabilidad')
        ax.set_title(titulo)
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('distribuciones_ajustadas.png', dpi=150, bbox_inches='tight')
    print("Visualización guardada: distribuciones_ajustadas.png")
    
    plt.close('all')


def guardar_resultados(resultados, frecuencias, probabilidades):
    """Guarda resultados en un archivo de texto."""
    with open('resultados_analisis.txt', 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write("RESULTADOS DEL ANÁLISIS DE DATOS\n")
        f.write("="*60 + "\n\n")
        
        f.write("FRECUENCIAS DE EVENTOS:\n")
        f.write("-"*40 + "\n")
        for evento, freq in frecuencias.items():
            f.write(f"  {evento}: {freq}\n")
        
        f.write("\n\nPROBABILIDADES:\n")
        f.write("-"*40 + "\n")
        for evento, prob in probabilidades.items():
            f.write(f"  {evento}: {prob:.4f}\n")
        
        f.write("\n\nDISTRIBUCIONES AJUSTADAS:\n")
        f.write("-"*40 + "\n")
        for variable, info in resultados.items():
            f.write(f"\n{variable.upper()}:\n")
            f.write(f"  Distribución: {info['dist']}\n")
            if 'params' in info:
                f.write(f"  Parámetros: {info['params']}\n")
            if 'lambda' in info:
                f.write(f"  Lambda (λ): {info['lambda']:.4f}\n")
            if 'p' in info:
                f.write(f"  Probabilidad (p): {info['p']:.4f}\n")
    
    print("\nResultados guardados: resultados_analisis.txt")


def main():
    if len(sys.argv) < 2:
        print("Uso: python analisis_datos.py <ruta_al_archivo_csv>")
        print("Ejemplo: python analisis_datos.py datos_eventos.csv")
        sys.exit(1)
    
    ruta_archivo = sys.argv[1]
    
    print("="*60)
    print("ANÁLISIS DE DATOS PARA SIMULACIÓN WATERFALL")
    print("="*60)
    print(f"\nArchivo: {ruta_archivo}")
    
    try:
        df = cargar_datos(ruta_archivo)
        frecuencias = calcular_frecuencias_eventos(df)
        probabilidades = estimar_probabilidades(df)
        df = identificar_patrones(df)
        resultados = ajustar_distribuciones(df)
        crear_visualizaciones(df, resultados)
        guardar_resultados(resultados, frecuencias, probabilidades)
        
        print("\n" + "="*60)
        print("ANÁLISIS COMPLETADO EXITOSAMENTE")
        print("="*60)
        print("\nArchivos generados:")
        print("  - analisis_visualizacion.png")
        print("  - distribuciones_ajustadas.png")
        print("  - resultados_analisis.txt")
        
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{ruta_archivo}'")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

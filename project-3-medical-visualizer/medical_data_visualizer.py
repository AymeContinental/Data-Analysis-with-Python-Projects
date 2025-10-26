import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

script_dir = os.path.dirname(__file__) # Directorio del script
file_path = os.path.join(script_dir, 'medical_examination.csv') # Ruta completa al CSV

df = pd.read_csv(file_path)

# Añadir columna 'overweight'
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# Normalizar datos (0 bueno, 1 malo)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Dibujar Gráfico Categórico
def draw_cat_plot():
    # Crear DataFrame para cat plot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Agrupar y reformatear
    # No es necesario agrupar manualmente si usamos kind='count' en catplot

    # Dibujar el catplot
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        hue='value',
        col='cardio',
        kind='count',
        height=4,
        aspect=1
    ).set_axis_labels('variable', 'total')

    # Obtener la figura
    fig = fig.fig

    # No modificar las siguientes dos líneas
    fig.savefig('catplot.png')
    return fig

# Dibujar Heat Map
def draw_heat_map():
    # Limpiar los datos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calcular la matriz de correlación
    corr = df_heat.corr()

    # Generar una máscara para el triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configurar la figura de matplotlib
    fig, ax = plt.subplots(figsize=(11, 9))

    # Dibujar el heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        linewidths=.5,
        square=True,
        center=0,
        cbar_kws={'shrink': .5},
        ax=ax
    )

    # No modificar las siguientes dos líneas
    fig.savefig('heatmap.png')
    return fig
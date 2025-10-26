import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress

def draw_plot():
    script_dir = os.path.dirname(__file__) # Directorio del script
    file_path = os.path.join(script_dir, 'epa-sea-level.csv') # Ruta completa al CSV

    df = pd.read_csv(file_path)

    # Crear gráfico de dispersión
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Crear primera línea de mejor ajuste (datos desde 1880)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Crear años para la predicción hasta 2050
    x_pred1 = pd.Series([i for i in range(1880, 2051)])
    y_pred1 = res1.intercept + res1.slope * x_pred1
    ax.plot(x_pred1, y_pred1, 'r', label='Best Fit Line (1880-2050)')

    # Crear segunda línea de mejor ajuste (datos desde 2000)
    df_2000 = df[df['Year'] >= 2000]
    res2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    # Crear años para la predicción (2000-2050)
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res2.intercept + res2.slope * x_pred2
    ax.plot(x_pred2, y_pred2, 'green', label='Best Fit Line (2000-2050)')

    # Añadir etiquetas y título
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()
    
    # Guardar y devolver la imagen
    plt.savefig('sea_level_plot.png')
    return plt.gca()
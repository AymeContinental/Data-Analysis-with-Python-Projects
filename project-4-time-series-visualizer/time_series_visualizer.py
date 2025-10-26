import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

script_dir = os.path.dirname(__file__) # Directorio del script
file_path = os.path.join(script_dir, 'fcc-forum-pageviews.csv') # Ruta completa al CSV

# Importar datos (parsear fechas y establecer 'date' como índice)
df = pd.read_csv(
    file_path,  # <-- Usas la variable file_path
    parse_dates=['date'], 
    index_col='date'
)

# Limpiar datos
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Dibujar gráfico de línea
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Guardar imagen y devolver fig
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copiar y preparar datos para el gráfico de barras mensual
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')
    
    # Agrupar por año y mes, calculando la media
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Ordenar los meses
    months_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_bar = df_bar[months_order]

    # Dibujar el gráfico de barras
    fig = df_bar.plot(kind='bar', figsize=(10, 6)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', loc='upper left')
    plt.tight_layout()

    # Guardar imagen y devolver fig
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Preparar datos para box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Orden de los meses
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Dibujar box plots (Year-wise y Month-wise)
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    
    # Gráfico 1: Year-wise
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Gráfico 2: Month-wise
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Guardar imagen y devolver fig
    fig.savefig('box_plot.png')
    return fig
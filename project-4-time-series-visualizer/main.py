import time_series_visualizer

# Llama a tus funciones para generar los gráficos
# (Asegúrate de que 'fcc-forum-pageviews.csv' esté en esta misma carpeta)
# Esto guardará los 3 gráficos .png en la carpeta
print("Generando gráfico de línea (line_plot.png)...")
time_series_visualizer.draw_line_plot()

print("Generando gráfico de barras (bar_plot.png)...")
time_series_visualizer.draw_bar_plot()

print("Generando diagramas de caja (box_plot.png)...")
time_series_visualizer.draw_box_plot()

# NOTA: Los tests oficiales se importarían de 'test_module.py'
# from unittest import main
# main(module='test_module', exit=False)
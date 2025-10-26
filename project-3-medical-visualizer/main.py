import medical_data_visualizer

# Llama a tus funciones para generar los gráficos
# (Asegúrate de que 'medical_examination.csv' esté en esta misma carpeta)
# Esto guardará 'catplot.png' y 'heatmap.png' en la carpeta
print("Generando gráfico categórico (catplot.png)...")
medical_data_visualizer.draw_cat_plot()

print("Generando mapa de calor (heatmap.png)...")
medical_data_visualizer.draw_heat_map()

# NOTA: Los tests oficiales se importarían de 'test_module.py'
# from unittest import main
# main(module='test_module', exit=False)
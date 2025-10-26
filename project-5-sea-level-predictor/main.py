import sea_level_predictor
import matplotlib.pyplot as plt

# Llama a tu función para generar el gráfico
# (Asegúrate de que 'epa-sea-level.csv' esté en esta misma carpeta)
# Esto guardará 'sea_level_plot.png'
print("Generando predictor de nivel del mar (sea_level_plot.png)...")
sea_level_predictor.draw_plot()

# Muestra el gráfico (opcional, para tu desarrollo)
# plt.show() 

# NOTA: Los tests oficiales se importarían de 'test_module.py'
# from unittest import main
# main(module='test_module', exit=False)
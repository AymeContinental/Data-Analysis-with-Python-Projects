import demographic_data_analyzer

# Llama a tu función. La función misma imprimirá los resultados.
# (Asegúrate de que 'adult.data.csv' esté en esta misma carpeta)
print("Ejecutando el Analizador de Datos Demográficos:")
results = demographic_data_analyzer.calculate_demographic_data(print_data=True)

# NOTA: Los tests oficiales se importarían de 'test_module.py'
# from unittest import main
# main(module='test_module', exit=False)
import mean_var_std

# Llama a tu función con un ejemplo
# Esto imprimirá el diccionario de cálculos
try:
    print(mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
except ValueError as e:
    print(e)

# Ejemplo de error
try:
    print(mean_var_std.calculate([1, 2, 3]))
except ValueError as e:
    print(f"\nError capturado (esto es esperado): {e}")

# NOTA: Los tests oficiales se importarían de 'test_module.py'
# from unittest import main
# main(module='test_module', exit=False)
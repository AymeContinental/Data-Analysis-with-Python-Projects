import numpy as np

def calculate(list_of_nums):
    if len(list_of_nums) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convertir la lista a una matriz 3x3 de Numpy
    matrix = np.array(list_of_nums).reshape(3, 3)

    # Calcular las estadísticas
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # axis 1 (columnas)
            matrix.mean(axis=1).tolist(),  # axis 2 (filas)
            matrix.mean()                # aplanado
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum()
        ]
    }

    return calculations
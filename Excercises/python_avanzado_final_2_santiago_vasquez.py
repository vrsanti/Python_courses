# Universidad San Carlos de Guatemala
# Facultad de Ingeniería
# Escuela de Ciencias y Sistemas
# Python Avanzado
# Final 2

# Santiago Vásquez Ramírez

# Ejercicio de Matrices en Python:
# • Crea una función llamada crear_matriz que acepte dos parámetros: filas y columnas. Esta función debe crear una matriz de tamaño filas x columnas e inicializarla con valores enteros aleatorios entre 1 y 100.
# • Crea una función llamada imprimir_matriz que acepte una matriz como argumento e imprima sus elementos en formato de matriz, es decir, una fila por línea (como lo hicimos en clase).
# • Crea una función llamada sumar_matrices que tome dos matrices como argumentos y devuelva una nueva matriz que sea la suma de las dos matrices. Asegúrate de que las matrices tengan las mismas dimensiones para que la suma sea válida.
# • [OPCIONAL] Crea una función llamada multiplicar_matrices que tome dos matrices como argumentos y devuelva una nueva matriz que sea el producto de las dos matrices. Asegúrate de que las dimensiones de las matrices sean adecuadas para la multiplicación (el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz).
# PASOS
# • Llama a la función crear_matriz para crear dos matrices diferentes.
# • Imprime ambas matrices utilizando la función imprimir_matriz.
# • Suma las dos matrices utilizando la función sumar_matrices y muestra el resultado.
# • [OPCIONAL] Multiplica las dos matrices utilizando la función multiplicar_matrices y muestra el resultado.

# Matrices => Una lista de listas

import numpy as np

'''
    Las filas son interpretadas como las listas interiores
    Las columnas son interpretadas como los elementos de cada una de las listas
    Nomenclatura para definir la dimension es: (Filas)x(Columnas)
'''
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]  # => Filas: 3 - Columnas: 3 -> Matriz: 3x3


# Proceso de dibujo de una matriz

def dibujar_matriz(matriz):
    dibujo = ''
    _fila = 0

    for fila in matriz:
        dibujo += '['
        for columna in fila:
            dibujo += f'{str(columna)},'
        dibujo = dibujo[:len(dibujo) - 1]
        dibujo += f'] => {_fila}\n'
        _fila += 1

    return dibujo


# print(dibujar_matriz(matriz))


# Acceder a los datos de una matriz
indice_fila = 2
indice_columna = 0
valor_encontrado = matriz[indice_fila][indice_columna]
# print(valor_encontrado)

# Modificar a los datos de una matriz
indice_fila = 2
indice_columna = 0
matriz[indice_fila][indice_columna] = 100
# print(dibujar_matriz(matriz))


# Numpy -> Matrices
matriz = [[1, 2, 3, 'a'],
          [4, 5, 6, 'b'],
          [7, 8, 9, 'c']]  # => Filas: 3 - Columnas: 4 -> Matriz: 3x4

np_matriz = np.array(matriz)
# print(np_matriz)

np_eye = np.eye(5, 5, dtype=int)
# print(np_eye)

np_identity = np.identity(10)
# print(np_identity)

np_ones = np.ones((10, 10))
# print(np_ones)

np_zeros = np.zeros((10, 10))
# print(np_zeros)

# Acceder a elementos
print(np_matriz[1][3])

# Modificar a elementos
np_matriz[1][3] = 'z'
# print(np_matriz)


# Suma de matrices
matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]  # => Filas: 3 - Columnas: 3 -> Matriz: 3x3
matriz2 = [[10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]]  # => Filas: 3 - Columnas: 3 -> Matriz: 3x32

np_matriz1 = np.array(matriz1)
np_matriz2 = np.array(matriz2)

np_result = np_matriz1 + np_matriz2
print(np_result)
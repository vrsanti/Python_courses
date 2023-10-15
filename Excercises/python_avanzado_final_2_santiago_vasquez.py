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

from random import randint

def crear_matriz(n, m) -> int:
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(randint(1,100))
        matriz.append(fila) 
    return matriz

def dibujar_matriz(matriz) -> None:
    dibujo = ''
    _fila = 0

    for fila in matriz:
        dibujo += '['
        for columna in fila:
            dibujo += f'{str(columna)},'
        dibujo = dibujo[:len(dibujo) - 1]
        dibujo += f']\n'
        _fila += 1
    return dibujo

def sumar_matriz(a, b) -> None: 
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        c = crear_matriz(len(a), len(a[0])) 
        for i in range(len(a)):
            for j in range(len(a[0])): c[i][j] = a[i][j] + b[i][j]
    return c

def multiplica_matriz(a, b):
    if len(a[0]) == len(b):
        c = crear_matriz(len(a), len(b[0])) 
        for i in range(len(c)):
            for j in range(len(c[0])):
                for k in range(len(a[0])):
                    c[i][j] += a[i][k] * b[k][j]
        return c

matriz_1 = crear_matriz(4, 4)
print("Matriz (formato lineal): ", matriz_1)
matriz_2 = crear_matriz(4, 4)
print("Matriz (formato lineal): ", matriz_2)

print(" ")
print("Matriz 1:\n", dibujar_matriz(matriz_1))
print("Matriz 2:\n", dibujar_matriz(matriz_2))

print(" ")
print("Suma matriz 1 y matriz 2:\n", dibujar_matriz(sumar_matriz(matriz_1, matriz_2)))

print(" ")
print("Multiplicación matriz 1 y matriz 2:\n", dibujar_matriz(multiplica_matriz(matriz_1, matriz_2)))
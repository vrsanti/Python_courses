
# filas x columnas

matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

def dibujar_matriz(matriz):
    dibujo = ''
    for fila in matriz:
        dibujo += '['
        for columna in fila:
            dibujo += f'{str(columna)},'
        dibujo
        dibujo += ']/n'
    return dibujo

print(dibujar_matriz)
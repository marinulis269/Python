#EJERCICIO 15
def suma(matriz1,matriz2):
    """ matriz MxM, matriz MxM -> matriz MxM
        OBJ: suma 2 matrices
        PRE: Las matrices son cuadradas y de las mismas dimensiones
    """
    suma = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        suma.append(fila)
    return suma

a = [ [1, 2, 3], [1, 2, 3] ]
b = [ [4, 5, 6], [4, 5, 6], [4, 5, 6] ]
print(suma(a, b))
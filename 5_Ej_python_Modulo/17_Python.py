#EJERCICIO 17
def en_orden_ascendente(lista):
    ordenado = True
    i = 1
    ant = lista[0]
    while i < len(lista) and ordenado:
        if lista[i] < ant:
            ordenado = False
        else:
            ant = lista[i]
            i += 1
    return ordenado

a = [1, 3, 5, 10]
b = [3, 5, 1, 10]
print('a: ', en_orden_ascendente(a))
print('b: ', en_orden_ascendente(b))
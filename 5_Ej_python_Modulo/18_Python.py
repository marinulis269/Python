#EJERCICIO 18

def limpiar_diccionario(diccionario, lista):
    nuevo_diccionario = {}
    for clave in diccionario.keys():
        if clave in lista:
            nuevo_diccionario[clave] = diccionario[clave]
    return nuevo_diccionario

dic = {'clave 1': 'valor 1', 'clave 2': 'valor 2', 'clave 3': 'valor 3'}
lis = ['clave 1', 'clave 3']
print(limpiar_diccionario(dic, lis))
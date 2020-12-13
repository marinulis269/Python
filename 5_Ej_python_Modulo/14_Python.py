#EJERCICIO 14

def count_comunes(lista1, lista2):
    comunes = []
    for i in lista1:
        if (i in lista2 and i not in comunes):
            comunes.append(i)
    return len(comunes)


a = [1,4,3,2,6]
b = [6,1,4,7]
print(count_comunes(a,b))
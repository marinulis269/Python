#EJERCICIO 13

def comunes(lista1, lista2):
    comunes = []
    for i in lista1:
        if (i in lista2 and i not in comunes):
            comunes.append(i)
    return comunes


a = [1,4,3,2,6]
b = [6,1,4,7]
print(comunes(a,b))
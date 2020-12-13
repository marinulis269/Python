#EJERCICIO 5
def suma_multiplos(lista_3_5):
    return sum(lista_3_5)

def sublista_rangos(rango):
    for i in rango:
        if (i%3 == 0 or i%5 == 0):
            lista_3_5.append(i)

rango = range(1,201)
lista_3_5=[]
sublista_rangos(rango)
print(suma_multiplos(lista_3_5))
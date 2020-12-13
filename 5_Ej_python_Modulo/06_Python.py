#EJERCICIO 6
def suma_primeros_multiplos():
    acum = 0
    i=1
    suma = 0
    while acum < 50:
        if (i%3 == 0 or i%5 == 0):
            acum +=1
            suma += i
        i +=1
    return suma


print(suma_primeros_multiplos())


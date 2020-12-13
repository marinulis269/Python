#EJERCICIO PROPUESTO 11
#Un año es bisiesto si es divisible por 400 o si lo es por 4 pero no por 100. 
# Programa una función que reciba un año y decida si es o no bisiesto. 

## ---- Modulos o subprogramas
def es_bisiesto(año):
    return(año%400 == 0 or año%4 == 0 and año%100 != 0)

## ---- Programa ppal
año = int(input("Escribe un año "))
print("¿Es bisiento? ", es_bisiesto(año))


#EJERCICIO PROPUESTO 6
#Escribe un programa que lea una longitud en kilómetros 
# y muestre su equivalencia en Hm, Dm y m 
# utilizando una función para cada cálculo.

## ---- Modulos o subprogramas
def converssion_hm (km):
    return round(km / 10, 2)

def converssion_dm (km):
    return round(km / 100, 2)

def converssion_m (km):
    return round(km / 1000, 2)

## ---- Programa ppal
kilometros = float(input("Escrime km: "))
print("La conversion a hm es: ", converssion_hm(kilometros))
print("La conversion a dm es: ", converssion_dm(kilometros))
print("La conversion a m es: ", converssion_m(kilometros))




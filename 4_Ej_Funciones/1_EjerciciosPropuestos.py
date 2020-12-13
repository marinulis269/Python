# Ejercicio propuesto 1
# Implementa una función “fuerza” que retorne el valor de la fuerza 
# en función de los valores de masa y aceleración recibidos como parámetros. 
# Implementa, posteriormente, un programa probador que, 
# leyendo de teclado los valores necesarios,
#  invoque a la función “fuerza” y muestre por pantalla el valor 
# de la fuerza a partir de una masa y aceleración dadas.

## ---- Modulos o subprogramas
def fuerza (masa, aceleracion):

    return masa * aceleracion

## ---- Programa ppal
masa = float(input("Masa: "))
aceleracion = float(input("Aceleracion: "))
print("La fuerza es", fuerza(masa, aceleracion))








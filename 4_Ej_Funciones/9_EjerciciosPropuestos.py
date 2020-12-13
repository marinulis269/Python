#EJERCICIO PROPUESTO 9
# Escribe un programa que muestre por pantalla la tabla de multiplicar 
# de un  número dado invocando para ello una función a la que le pasará 
# dicho número. 

## ---- Modulos o subprogramas
def tabla_multiplicar(numero):
    for x in range(0,11):
        print(str(numero)+ "x"+ str(x) + "=" + str(numero * x))

## ---- Programa ppal
num = int (input("Escribe un número: "))
tabla_multiplicar(num)
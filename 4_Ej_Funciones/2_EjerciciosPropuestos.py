# Ejercicio propuesto 2
# Implementa un programa modularizado que, leyendo de teclado los valores necesarios, 
# muestre en pantalla el área de un círculo, un cuadrado y un triángulo. 
# Utiliza el valor 3.1416 como aproximación de ¬ П (pi) 
# o importa el valor del módulo “math”.

# area_circulo = 2 * PI * radio
# area_cuadrado = lado ^2
# area_triangulo = (base * altura) / 2


## ---- Modulos o subprogramas
import math
def area_circulo(radio):
    return round(math.pi * radio *2, 2)

def area_cuadrado(lado):
    return round(lado**2)

def area_triangulo(base, altura):
    return round(base*altura/2)

## ---- Programa ppal
figuras = ("1.circulo", "2.cuadrado", "3.triangulo")
print("Elige una de estas 3 figuras: ", figuras)
selecion_figuras = int(input("Escribe 1 / 2 / 3 "))
if (selecion_figuras == 1):
    r = float(input("Escribe el radio del circulo "))
    print("El area del circulo es ", area_circulo(r))
elif (selecion_figuras == 2):
    l = float(input("Escribe la longitud de un lado del cuadrado "))
    print("El area del cuadrado es ", area_cuadrado(l))
elif (selecion_figuras == 3):
    b = float(input("Escribe la base del tringulo "))
    h = float(input("Escribe la altura del tringulo "))
    print("El area del triangulo es ", area_triangulo(b, h))

#Esta bien, pero es mejor si hacemos 2 procedimientos searados que sean elegir menu y pedir datos
# y en el programa principal solo llamamos a pedri datos. Mirar solucion de Ruth





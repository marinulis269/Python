#EJERCICIO PROPUESTO 5
# Escribe un programa modularizado que solicite al usuario una 
# hora en formato [hora, minutos y segundos] y
#  utilizando una función que calcule el número total 
# de segundos transcurridos desde la última medianoche,
#  lo muestre posteriormente por pantalla.

## ---- Modulos o subprogramas
def calculo_segundos(h,m,s):
    return (h*60 + m*60 + s)

def pedir_hora():
    h = int(input("Escribe la hora "))
    m = int(input("Escribe los minutos "))
    s = int(input("Escribe los segundos "))
    return (h,m,s)
    

## ---- Programa ppal
hora,minuto,segundo = pedir_hora()
if 0<=hora<=23 and 0<=minuto<=59 and 0<=segundo<=59:
    print("El calculo en segundos es: ", calculo_segundos(hora, minuto , segundo))

else:
    print("Datos de la hora no válidos")




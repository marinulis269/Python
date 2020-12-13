#EJERCICIO PROPUESTO 7
#Escribe una función que determine si un punto de coordenadas en 2D 
# está o no sobre la circunferencia x^2+y^2=1000.

## ---- Modulos o subprogramas
def pertenece (x,y):
    if pow(x,2)+pow(y,2)==1000: #Función pow sirve para elevar un nº a otro
        return True
    else:
        return False


## ---- Programa ppal
x = int(input("Escribe coordenada x: "))
y = int(input("Escribe coordenada y: "))
print("¿Punto está en la circinferencia? ", pertenece (x,y))









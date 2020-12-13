#EJERCICIO 7
def pedirDatos_Pila():
    for i in range(4):
        n=int(input("Introduce un numero: "))
        if (n%2) == 0 or (n%3) == 0:
            pila.append(n)
    for i in range(len(pila)):
        print(pila.pop())

pila = []
pedirDatos_Pila()


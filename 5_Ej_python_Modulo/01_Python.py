#EJERCICIO 1
def mayor (n1, n2, n3):
    if (n1 >= n2 and n1 >= n3):
        return n1
    elif (n1<= n2 and n2 >= n3):
        return n2
    else:
        return n3

a = int(input("Introduzca un número: "))
b = int(input("Introduzca otro número: "))
c = int(input("Introduzca el último número: "))
print(mayor(a,b,c))

#EJERCICIO 3
def media(lista_Numeros):
    sum_lista = lista_Numeros.copy()
    sum_lista.pop()
    return sum(sum_lista)/len(sum_lista)

def pedir_datos():
    n=0
    while n != -9999:
        n = int(input("Escribe un numero "))
        lista_Numeros.append(n)


lista_Numeros = []
pedir_datos()
print(media(lista_Numeros))

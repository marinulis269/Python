#EJERCICIO 16

def pedir_palabras():
    pila = []
    palabra = "inicio"
    while (palabra != "fin"):
        palabra = str(input("Escribe una palabra: "))
        pila.append(palabra)
    return pila

def longitudes(pila):
    longitudes = []
    for i in pila:
        longitudes.append(len(i))
    return longitudes

def estadisticas(longitudes):
    est = []
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(longitudes)):
        if longitudes[i] < 5:
            count1 +=1
        elif longitudes[i] <10:
            count2 +=1
        elif longitudes[i] >= 10:
            count3 +=1
    est = [count1, count2, count3]
    est = [round(count1/len(est)*100, 2), round(count2/len(est)*100,2), round(count2/len(est)*100,2)]
    return est

lista = pedir_palabras()
lista_longitudes = longitudes(lista)
print(longitudes(lista))
print(estadisticas(lista_longitudes))
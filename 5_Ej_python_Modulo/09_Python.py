#EJERCICIO 9

def pedir_datos():
    for i in range(5):
        notas = int(input("Escirbe la nota: "))
        lista.append(notas)

def cambiar_notas(lista):
    for i in range(len(lista)):
        if lista[i] < 5: 
            lista[i] = "Suspenso"
        elif lista[i] == 5 or lista[i] == 6: 
            lista[i] = "Aprobado"
        elif lista[i] == 7 or lista[i] == 8: 
            lista[i] = "Notable"
        elif lista[i] == 9 or lista[i] == 10: 
            lista[i] = "Sobresaliente"


lista = []
pedir_datos()
cambiar_notas(lista)
print(lista)

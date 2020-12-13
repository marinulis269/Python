#EJERCICIO 12

def suma_listas(l1, l2):
    l3 = []
    menor = min(len(l1), len(l2))
    for i in range(menor):
        l3.append(l1[i] + l2[i])

    if len(l1) == menor:
        for j in range(menor, len(l2)):
            l3.append(l2[j])
    else:
        for j in range(menor, len(l1)):
            l3.append(l1[j])
    return l3
        

a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4]

print(suma_listas(a,b))

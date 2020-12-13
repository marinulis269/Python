#EJERCICIOS TRABAJANDO LISTAS (BUCLES)

#EJERCICIO 1
magicians = ["alice", "carolina", "anne"]
for i in magicians:
    print(i)

#EJERCICIO 2
favorite_ingredients = ["pepperoni", "hawaiian" , "veggie"]
for i in favorite_ingredients:
    print(i)

for i in favorite_ingredients:
    print("I love",i, "in pizza")
print("I love all pizzass")

#EJERCICIOS CON ESTRUCTURAS DE CONTROL Y TIPOS DE DATOS
#EJERCICIO 1
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto","septiembre", "octubre", "noviembre", "diciembre")
numero = int(input("Escribe un numero: "))
while (numero !=0):
    if (numero >= 1 and numero <= len(meses)):
        print(meses[numero])
        numero = int(input("Escribe un numero: "))
    else:
        print("error")
        numero = int(input("Escribe un numero: "))
print("Fin")
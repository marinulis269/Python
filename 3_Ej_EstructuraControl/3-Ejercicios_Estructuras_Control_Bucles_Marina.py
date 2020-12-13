#EJERCICIOS CON ESTRUCTURAS REPETITIVAS
#EJERCICIO 1
numero = int(input("Escribe un numero: "))
for i in range(0,11):
    print(numero,"x",i,"=",numero*i)

#EJERCICIO 2
nombre = str(input("Escribe tu nombre: "))
numeroSaludo = int(input("Escribe un numero de saludos: "))
for i in range(1,numeroSaludo+1):
    print("Hola", nombre)

#EJERCICIO 3
x = 0
for i in range(1,101):
    x += i
print(x)
    

#EJERCICIO 4
n = int(input("Escribe un numero: "))
cont =[]
while n > 0:
    cont.append(n)
    n = int(input("Escribe un numero: "))
print(cont)

#EJERCICIO 5
usuario = str(input("Escribe el nombre de usuario: "))
contraseña = str(input("Escribe la contraseña: "))
contador = 1
while ((usuario != "admin" or contraseña != "1234&") and contador !=3):
    contador += 1
    usuario = str(input("Escribe el nombre de usuario: "))
    contraseña = str(input("Escribe la contraseña: "))

print("fin")
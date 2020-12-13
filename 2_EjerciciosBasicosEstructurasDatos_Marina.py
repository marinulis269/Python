#EJERCICIOS BASICOS ESTRUCTURAS DE DATOS

#EJERCICIOS DE LISTAS
#EJERCICIO 1
bicycles = ["trek", "cannondale","redline", "specialized"];print(bicycles)

#EJERCICIO 2
print(bicycles[2]) #Las listas comienzan en la posicion 0

#EJERCICIO 3

#EJERCICIO 4
print(bicycles[-1])

#EJERCICIO 5
print("My first bicycle was a "+ bicycles[0])

#EJERCICIO 6
motorcycles = ["honda", "yamaha", "suzuki"]; print(motorcycles) 

#EJERCICIO 7
 #se sustituye honda por ducatis

#EJERCICIO 8
motorcycles.append("honda");print(motorcycles)

#EJERCICIO 9
del motorcycles[0];print(motorcycles)

#EJERCICIO 10
motorcycles.insert(0, "ducati"); print(motorcycles)

#EJERCICIO 11
motorcycles_popped = motorcycles[3];print(motorcycles_popped, type(motorcycles_popped))
del motorcycles[3];print(motorcycles);print(motorcycles_popped)

#EJERCICIO 12
motorcycles.remove("yamaha");print(motorcycles)

#EJERCICIO 13
motorcycles = [];print(motorcycles)
motorcycles = ["yamaha", "ducati", "suzuki", "ducati", "ducati"]; print(motorcycles)
motorcycles.remove("ducati");print(motorcycles)

#EJERCICIO 14
motorcycles= ["yamaha", "suzuki","honda","ducati"]
motorcycles.sort();print(motorcycles)

#EJERCICIO 15
motorcycles[:];print(motorcycles)

#EJERCICIO 16
print(len(motorcycles))


#EJERCICIO 17
motorcycles.reverse(); print(motorcycles)

#EJERCICIO 18
#print(motorcycles[4])

#EJERCICIO 19
print(motorcycles)

#EJERCICIO 20
print(motorcycles[1:3])

#EJERCICIO 21
print(motorcycles[2:])

#EJERCICIO 22
my_foods=["pizza", "cakes", "meat"];print(my_foods)
family_foods = my_foods.copy(); print(family_foods)
print("My favorite foods are:", my_foods)
print("My family’s favorite foods are:", family_foods)

#Ejercicio 23
my_foods.insert(3,"ice-cream");print(my_foods);print(family_foods)
#Ejercicio 24

#EJERCICIOS DE TUPLAS
#EJERCICIO 1
dimensions = (100,200)
print(dimensions, type(dimensions))
#EJERCICIO 2
print(dimensions[0], type(dimensions[0]))
#EJERCICIO 3

#EJERCICIOS DE DICCIONARIOS
#EJERCICIO 1
#nombre = input ("Por favor escrie tu nombre: ")
#direccion = input ("Por favor escrie tu direccion: ")
#edad = input ("Por favor escrie tu edad: ")
#telefono = input ("Por favor escrie tu telefono: ")
#person = {"nombre": nombre, "direccion": direccion, "edad": edad, "telefono": telefono}
#print(person, type(person))
#print(person.keys())
#print(person.values())
#print(person["nombre"]+ " tiene "+ person["edad"] + " años,vive en " +person["direccion"] + " y su numero de telefono es: " + person["telefono"] )

#EJERCICIO 2
person = {}
#EJERCICIO 3
#EJERCICIO 4
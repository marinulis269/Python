#Ejercicio 1
edad = int(input("Por favor dime tu edad: "))
const = 18
if (edad >= const):
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

#Ejercicio 2
favorite_movies = ["Iron Man", "Captain America", "Avengers"]
pelicula = str(input("Escribe una pelicula: "))

if (pelicula in favorite_movies):
    print("A los dos nos gustan las mismas peliculas")
else:
    print("No nos gustan las mismas peliculas")

#Ejercicio 3
favorite_movies = ["IRON MAN", "CAPTAIN AMERICA", "AVENGERS"]
pelicula = str(input("Escribe una pelicula: ")).upper()

if (pelicula in favorite_movies):
    print("A los dos nos gustan las mismas peliculas")
else:
    print("No nos gustan las mismas peliculas")

#Ejercicio 4
edad = int(input("Dime tu edad: "))
if (edad <= 4):
    print("Acceso gratuito")
elif (edad <= 12):
    print("Entrada 4,5 €")
else:
    print("Entrada 8€")

#Ejercicio 5
edad = int(input("Dime tu edad: "))
if (edad <= 2):
    print("¡Eres un bebe!")
elif (edad <= 4):
    print("¡Eres un crí@!")
elif (edad <= 13):
    print("¡Eres un nin@!")
elif (edad <= 20):
    print("¡Eres un adolescente!")
elif (edad <= 65):
    print("¡Eres un adulto!")
else:
    print("Eres un anciano")


#Ejercicio 6
for i in range(1,10):
    if (i == 1):
        print(str(i) + "st")
    elif (i==2):
        print(str(i) + "nd")
    elif (i==3):
        print(str(i) + "rd")
    else:
        print(str(i) + "th")

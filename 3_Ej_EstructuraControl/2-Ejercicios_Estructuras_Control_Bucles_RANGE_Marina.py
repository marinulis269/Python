#EJERCICIOS CON RANGE
#EJERCICIO 1
for i in range(1,21):
    print(i)

#EJERCICIO 2
for i in range(3,31,3):
    print(i)

#EJERCICIO 3
x = range(3,31,3)
print(list(x),type(x))
for i in x:
    print(i)


#EJERCICIO 4
cubes = []

for i in range(1,11):
    cubes.append(i**3)
    print(cubes)

print(cubes,type(cubes))

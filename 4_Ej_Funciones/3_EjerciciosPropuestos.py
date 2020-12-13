# Ejercicio propuesto 3
# Implementa un programa modularizado que, leyendo la nota obtenida
# por tres alumnos en una asignatura, muestre por pantalla la media de las notas.

## ---- Modulos o subprogramas
def pedir_notas():
    a = int(input(" Introduce nota del alumno " ))
    b = int(input(" Introduce nota del alumno " ))
    c = int(input(" Introduce nota del alumno " ))
    return a,b,c

def media(n1,n2,n3):
    return (n1+n2+n3)/3

## ---- Programa ppal
nota1, nota2, nota3 = pedir_notas()
print("La media es ", media(nota1,  nota2, nota3))




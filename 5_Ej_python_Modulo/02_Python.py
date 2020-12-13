#EJERCICIO 2
def calculo_salario(h,p):
    if 0<h<=40 and p>0:
        return h*p
    elif h > 40 and p>0:
        return 40*p + (h-40)*p*1.5
    else:
        print ("Error : los datos son incorrectos .")

horas = int(input("Introduzca el numero de horas: "))
precio = int(input("Introduzca el precio por hora: "))
print(calculo_salario(horas,precio))

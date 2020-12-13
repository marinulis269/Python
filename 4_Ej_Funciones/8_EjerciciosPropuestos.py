#EJERCICIO PROPUESTO 8
#El antiguo sistema anglosajón de unidades sigue en vigor en muchos 
#lugares y su uso es frecuente en algunos contextos.
# Programa una función que determine el número de 
# pintas que contiene una cierta cantidad de líquido expresada en mililitros, 
# sabiendo que 1 pinta (pt) = 473,176473 ml.

## ---- Modulos o subprogramas
def calculo_pintas (ml):
    return round(ml/473.176473,2)

## ---- Programa ppal
mililitros = float(input("Introduce los ml "))
print("Equivale a ", calculo_pintas(mililitros), "pintas")




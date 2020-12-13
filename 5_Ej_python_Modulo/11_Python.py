#EJERCICIO 11

archivo = open(r'C:\Users\SESA513337\Documents\Master Data Science\1_FUNDAMENTOS TECNOLOGICOS\B1-Introduccion a la programacion con Python\Plan de Trabajo\code\Ejercicios_Marina\5-Ejercicios python Modulo_Marina\file_11.txt')
def extraer_lineas(archivo):
    for linea in archivo:
        lista.append(linea.split())
    return lista


lista = []
print(extraer_lineas(archivo))
archivo.close
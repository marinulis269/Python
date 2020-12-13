#EJERCICIO 10

def extraer_hashtags(texto):
    lista = []
    for i in texto.split():
        if i[0] == '#': 
            lista.append(i)
    return lista


tweet = "Inscríbete en el #CallOfData2018 para participar en el #datatón"
#hashtags = extraer_hashtags(tweet)
print(extraer_hashtags(tweet))

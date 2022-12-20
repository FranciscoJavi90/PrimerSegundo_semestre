#Diseñe un Programa que, dados como datos el tiempo que realizan los participantes en competencia de velocidad en pista y la distancia del recorrido, calcula la velocidad 
#de los mismos expresada en Kilómetros por hora.
distancia =float(input('Introduzca distancia recorrida en kilometros: '))
tiempo = float(input('Introduzca tiempo del recorrido: '))
total = (distancia / tiempo)
print('Velocidad de recorrido km/h:',total)

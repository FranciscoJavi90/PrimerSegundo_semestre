palabra = input("Introduzca una palabra: ")
contador = 0 
for letra in palabra:
    if letra == "a":
        contador = contador + 1
        print ("Numero de veces que se repite la palabra. ",contador)
        
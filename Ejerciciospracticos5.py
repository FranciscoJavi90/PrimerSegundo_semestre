peso = input("¿Cuál es tu peso en kg?")
altura = input("¿Cual es tu estatura en metros?")
imc = round(float(peso)/float(altura)**2,2)
print("Tu índice de masa corporal es " + str(imc))

#Los datos A, B, C y D representan números enteros, escriba los mismos en orden inverso.
numero = int(input("Ingresa una cadena de números: "))
i = 0

while numero > 0:
    i = i + 1
    resto = numero % 10
    numero = int(numero / 10)
    print("%d" % (resto), end = "")
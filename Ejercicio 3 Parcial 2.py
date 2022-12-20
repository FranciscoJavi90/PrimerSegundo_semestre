sumar = sum( range(0, 101, 2) )
print(sumar)

numero = 0
sumar = 0

while numero <= 100:
    if numero % 2 == 0:
        sumar += numero
    numero += 1

print(sumar)
import numpy as np
lista = [24,12,15,66,12.5]
vector = np.array(lista)
print(vector)
print("- vector original")
print(vector)

print("- Sumarle 1 a cada elemento del vector:")
print(vector+1)
print("- Multiplicar por 5 cada elemento del vector:")
print(vector*5)
print("- Suma de los elementos:")
print(np.sum(vector))
print("- Promedio (media) de los elementos:")
print(np.mean(vector))
print("- El vector sumado a si mismo:")
print(vector+vector)
print("- Suma de vectores vector1 y vector2 (mismo tamaño)")
vector2=np.array([11,55,1.2,7.4,-8])
print(vector+vector2)
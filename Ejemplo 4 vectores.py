import numpy as np 
lista_de_listas=[ [1  ,-4],
                  [12 , 3],
                  [7.2, 5]]
a = np.array(lista_de_listas)

print("Elementos individuales")
print(a[0,1])
print(a[2,1])

print("Vector de elementos de la columna 1")
print(a[1,:])

print("Vector de elementos de la columna 0")
print(a[:,0])

print("Submatriz de 2*2 con las primeras dos filas")
print(a[0:2,:])

print("Submatriz de 2*2 con las últimas dos filas")
print(a[1:3,:])
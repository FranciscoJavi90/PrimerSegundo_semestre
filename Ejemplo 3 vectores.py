import numpy as np 
print("- Matriz creada con una lista de listas:")
lista_de_listas=[ [1  ,-4],
                  [12 , 3],
                  [7.2, 5]]
matriz = np.array(lista_de_listas)
print(matriz)

print("- Matriz creada con np.zeros:")
dimensiones=(2,3)
matriz_ceros = np.zeros(dimensiones)
print(matriz_ceros)

print("- Matriz creada con np.ones:")
dimensiones=(3,2)
matriz_unos = np.ones(dimensiones)
print(matriz_unos)

print("- Copia de la matriz creada con np.ones:")
matriz_unos_copia=np.copy(matriz_unos)
print(matriz_unos_copia)
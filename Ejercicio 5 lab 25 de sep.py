import numpy as np
a = np.array ([[5, 8, 7, 8],
               [1, 2, 7, 5],
               [7, 5, 4, 3]])
b = np.array ([[7, 8, 7, 8],
               [1, 2, 7, 5],
               [7, 5, 4, 3]])

def suma():
    print("La suma de las matrices son: ")
    print(a + b)

def resta():
    print("La resta de las matrices son: ")
    print(a - b)

def división():
    print("La división de las matrices son: ")
    print(a/b)

def multiplicación():
    print("La multiplicación de las matrices son: ")
    print(a*b)
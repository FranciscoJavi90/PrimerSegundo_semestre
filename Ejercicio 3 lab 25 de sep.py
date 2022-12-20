filename = input('Ingrese el nombre del archivo: ')
cant_lineas = int(input('Ingrese la cantidad de lineas a leer: '))

with open(filename, 'r') as archivo:
    for i in range(cant_lineas):
        linea = archivo.readline()
        print(linea, end='')
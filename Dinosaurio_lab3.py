#Escriba un algoritmo en Python en donde, dado el nombre de un dinosaurio, su peso expresado en toneladas y su longitud expresada en pies; escriba el nombre del dinosaurio, su peso y longitud 
#expresadas en Kilogramos y metros respectivamente.
Dinosaurio = input('Introduzca nombre del Dinosaurio: ')
Kilogramos = 1000
Peso = float(input('Introducir peso en toneladas: '))
Kg = float(Peso * Kilogramos)
Metros = float(0.3048)
Longitud = float(input('Introducir longitud en pies: '))
Mt = float(Longitud * Metros)
print('Nombre de Dinosaurio',Dinosaurio)
print('Peso en kilogramos: ',Kg)
print('Longitud en metros: ',Mt)

#Dado el radio y la altura de un cilindro, calcule su área y su volumen.
print("Calcular Área y Volumen de un cilindro")
r = float(input('Ingrese radio del cilindro:  '))
h = float(input('Ingrese altura del cilindro:  '))
Pi = 3.1416
Area = float(2 * r * Pi)
totalA = float(Area * r * h)
print('Área de un cilindro circular',totalA)
volumen = float(Pi * pow(r,2) * h)
print('Volumen de un cilindro:',volumen)

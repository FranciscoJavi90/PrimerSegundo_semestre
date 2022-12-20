mayor = 0
maximo = 4 
 
for i in range(maximo):
    num = int(input('Ingrese cuatro números consecutivos para hallar el mayor:'))
    if num > mayor:
        mayor = num
 
print(mayor)
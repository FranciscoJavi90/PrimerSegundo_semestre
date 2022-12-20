#Dada la matrícula y 5 calificaciones de un alumno obtenidas a lo largo del semestre, construya un programa que imprima la matrícula del alumno y el promedio de sus calificaciones.
matricula =int(input("Ingrese matricula de estudiante: "))
a = int(input("Ingrese primera calificación:  "))
b = int(input("Ingrese segunda calificación:  "))
c = int(input("Ingrese tercera calificación:  "))
d = int(input("Ingrese cuarta calificación:  "))
e = int(input("Ingrese quinta calificación:  "))
print('La matricula de estudiante es: ', matricula)
resultado = (a + b + c + d + e)/5
print('Promedio de estudiante', resultado)
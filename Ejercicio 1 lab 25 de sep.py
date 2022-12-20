n = int(input("Ingrese un numero entre en 1 y 10: "))
a = "tabla_"+str(n) + ".txt"
b = open(a,"w")
for i in range (1,11):
    b.write(str(n)+ "*" +str(i)+ "=" +str(n+1)+"\n")
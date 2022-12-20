def validar(email):
    caracterEncontrar="@"
    emailCorrecto=False
    for x in email:
        if x==caracterEncontrar:
            return True
    return False
direc=input("Tu email: ")
if caracterEncontrar(direc):
    print("Dirección correcta")
else:
    print("Dirección incorrecta")
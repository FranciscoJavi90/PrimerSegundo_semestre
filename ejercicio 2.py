def validar(email):
    sim= "."
    valemail=False
    for z in email:
        if z==sim:
            return True
    return False

dir=input("Tu direccion: ")
if validar(dir):
    print("Direccion Aprobada")
else:
    print("Direccion no Aprovada")
class Humano():
def  in (self,edad,nombre,ocupación):
self.edad = edad
self.nombre = nombre
self.ocupación = ocupación
def presentar(self):
presentacion = ("Holasoy [],mi edad es [] y mi ocupación es []")
print(presentacion.format(self.nombre, self.edad, self.ocupación)
Personas1 = Humano(31, "Pedro", "Desocupado")
Personas1.presentar()

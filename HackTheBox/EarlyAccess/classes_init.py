#!/usr/bin/pythob

class Personas:
	def __init__(self, name, age):
	 self.name= name
	 self.age = age
persona1 = Personas("Axel", 19)
persona2 = Personas("Fanny", 46)
print("[+]LISTADO DE PERSONAS[+]")
print(persona1.name,"",persona1.age)
print(persona2.name,"",persona2.age)

class Alimentos:
	def __init__(self, alimento, precio):
	 self.alimento = alimento
	 self.precio= precio
a1 = Alimentos("Refresco",15)
a2 = Alimentos("Pizza", 35)
print("[+]LISTA DE ALIMENTOS[+]")
print(a1.alimento,"",a1.precio)
print(a2.alimento,"",a2.precio)

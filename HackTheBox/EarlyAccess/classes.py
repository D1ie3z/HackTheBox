#!/usr/bin/python

class Key: 
	master_key="Supermasterkey!#%$"
	magic_value= "XP"
o1 = Key() #CREANDO UN OBJETO EN LA CLASE KEY
class test:
	n=4
o2= test()
print("ESTA ES LA LLAVE MAESTRA:",o1.master_key) #LLAMANDO AL OBJETO Y UN VALOR ESPECIFICO DE LA CLASE
print("ESTE ES EL VALOR MAGICO DE LA CLASE KEY: ",o1.magic_value)
print("TEST:",o2.n)

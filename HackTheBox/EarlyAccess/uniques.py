#!/usr/bin/python
 
from itertools import product
import string

p1 = product(string.ascii_uppercase, repeat = 2)
p1 = ["".join(i) for i in p1]

uniques = {}

for i in p1:
	for j in range(0,10):
		cadena = f'XP{i}{j}' 
		value = sum(bytearray(cadena.encode()))

		uniques[value] = cadena
print(uniques.values())
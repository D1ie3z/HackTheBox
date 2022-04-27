#!/usr/bin/python3

from itertools import product
import string, sys

caracteres = string.ascii_uppercase + string.digits
p1 = product(caracteres, repeat=3) #ACE
p1 = ["".join(i)for i in p1]

p2 = product(caracteres, repeat=2) #BD
p2 = ["".join(i)for i in p2]

for x in p1:
	for y in p2:
		if sum(bytearray(x.encode())) == sum(bytearray(y.encode())):
		 print(x[0] + y[0] + x[1] + y[1] + x[2])

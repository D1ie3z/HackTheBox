#!/usr/bin/python

def la_funcion(n):
	return lambda argumento : argumento*n #lambda argumento : expresion

nose = la_funcion(3)

print(nose(11))

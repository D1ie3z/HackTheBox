#!/usr/bin/python

def calc_cs(key) -> int:
	gs = key.split('-')[:-1]
	return sum([sum(bytearray(g.encode())) for g in gs])

print(calc_cs("AAAAA-BBBBB-CCCC1-DDDDD-"))

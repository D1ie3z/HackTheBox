#!/usr/bin/python
import string, sys

if len(sys.argv) != 2:
    print("[!]Uso correcto: python3 %s <0-2>"% sys.argv[0])
    sys.exit(1)
i = int(sys.argv[1])
caracteres = string.ascii_uppercase + string.digits
for v in caracteres:
    valor = (ord(v)<<i+1)%256^ord(v)
    print(f"{v}:{valor}")

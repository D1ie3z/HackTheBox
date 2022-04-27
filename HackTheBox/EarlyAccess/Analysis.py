#!/usr/bin/env python3
import sys
from re import match

class Key:
    key = ""
    magic_value = "XP" # Static (same on API)
    magic_num = 346 # TODO: Sync with API (api generates magic_num every 30min)

    def __init__(self, key:str, magic_num:int=346): #FUNCION QUE TIENEN TODAS LAS CLASES EN GENERAL
        self.key = key #ACCEDIENDO AL ARGUMENTO KEY
        if magic_num != 0: 
            self.magic_num = magic_num

    @staticmethod
    def info() -> str:
        return f"""
        # Game-Key validator #

        Can be used to quickly verify a user's game key, when the API is down (again).

        Keys look like the following:
        AAAAA-BBBBB-CCCC1-DDDDD-1234

        Usage: {sys.argv[0]} <game-key>"""

    def valid_format(self) -> bool:
        return bool(match(r"^[A-Z0-9]{5}(-[A-Z0-9]{5})(-[A-Z]{4}[0-9])(-[A-Z0-9]{5})(-[0-9]{1,5})$", self.key))

    def calc_cs(self) -> int:
        gs = self.key.split('-')[:-1] #QUITANDO EL - CON EL SPLIT A LA CADENA
        return sum([sum(bytearray(g.encode())) for g in gs])  #SUMA TODOS LOS CARACTERES UNO POR UNO Y TODOS AL ULTIMO EJEMPLO (A+A+A+A+A)+(B+B+B+B+B),etc... 

    def g1_valid(self) -> bool: #FUNCION G1 QUE ES LA PRIMER PARTE DE LA CADENA
        g1 = self.key.split('-')[0] 
        r = [(ord(v)<<i+1)%256^ord(v) for i, v in enumerate(g1[0:3])] #TOMA LOS PRIMEROS VALORES DE LA CADENA Y HACE left shift QUE RECORRE A LA IZQUIERDA EL VALOR BINARIO
        if r != [221, 81, 145]: #COMPRUEBA QUE EL VALOR DE LOS PRIMER CARACTERES SEAN ESTOS EJEMPLO K -> 221 ESTO POR LA OPERACION DE ARRIBA
            return False
        for v in g1[3:]: #TOMA LOS DOS DIGITOS QUE SOBRAN DE LA CADENA
            try:
                int(v) #INTENTA CUALQUIER VALOR ENTERO, PODEMOS PONER DOS NUMEROS CUALQUIERA
            except:
                return False #SI NO ES UN VALOR DE ESTE TIPO NO HACE LA VALIDACION
        return len(set(g1)) == len(g1)

    def g2_valid(self) -> bool:
        g2 = self.key.split('-')[1]
        p1 = g2[::2] #TOMA LOS VALORES (POSICION) IMPARES DE LA CADENA
        p2 = g2[1::2] #TOMA LOS VALORES PARES
        return sum(bytearray(p1.encode())) == sum(bytearray(p2.encode())) #HACE UNA SUMA DEL VALOR EN DECIMAL DE LA LETRA EJEMPLO ABC -> 65+66+67 = 198 Y ESTE DEBE COINCIDIR CON LA MISMA SUMA DE LOS IMPARES  

    def g3_valid(self) -> bool:
        # TODO: Add mechanism to sync magic_num with API
        g3 = self.key.split('-')[2] #TOMA LA TERCER POSICION
        if g3[0:2] == self.magic_value: #TOMA LOS PRIMEROS 2 VALORES DE LA CADENA Y VALIDA QUE SEAN IGUAL A "XP"
            return sum(bytearray(g3.encode())) == self.magic_num #HACE UNA SUMA COMO LO ANTERIOR PERO QUE DE EL VALOR DE 346
        else:
            return False

    def g4_valid(self) -> bool:
        return [ord(i)^ord(g) for g, i in zip(self.key.split('-')[0], self.key.split('-')[3])] == [12, 4, 20, 117, 0] #TOMA EL PRIMER VALOR DE LA PRIMER POSICION Y LE APLICA XOR CON EL VALOR DE LA TERCERA POSICION Y A LADO MUESTRA EL RESULTADO DE CADA ITERACION 

    def cs_valid(self) -> bool:
        cs = int(self.key.split('-')[-1])
        return self.calc_cs() == cs

    def check(self) -> bool:
        if not self.valid_format():
            print('Key format invalid!')
            return False
        if not self.g1_valid():
            return False
        if not self.g2_valid():
            return False
        if not self.g3_valid():
            return False
        if not self.g4_valid():
            return False
        if not self.cs_valid():
            print('[Critical] Checksum verification failed!')
            return False
        return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Key.info())
        sys.exit(-1)
    input = sys.argv[1]
    validator = Key(input)
    if validator.check():
        print(f"Entered key is valid!")
    else:
        print(f"Entered key is invalid!") 

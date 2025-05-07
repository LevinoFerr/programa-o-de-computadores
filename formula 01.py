# calcular o movimento retilíneo uniformemente variado

# velocidade inicial do objeto = v0
# aceleração do objeto = a
# tempo transcorrido = t
# deslocamento do objeto = D

import sys

ds = v * t + (( a * t ** 2) / 2)

v = int (input("velocidade"))
if v <=0:
    sys.exit

a = int (input ("aceleração do objeto?"))
if a <=0:
    sys.exit

t = int (input ("tempo"))
if t <=0:
    sys.exit

    print (v * t + (( a * t ** 2) / 2))









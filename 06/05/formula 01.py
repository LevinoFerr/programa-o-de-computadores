# calcular o movimento retilíneo uniformemente variado

# velocidade inicial do objeto = v0
# aceleração do objeto = a
# tempo transcorrido = t
# deslocamento do objeto = D

from os import system

ds = v * t + (( a * t ** 2) / 2)

v = int (input("velocidade"))
if v <=0:
    system.exit

a = int (input ("aceleração do objeto?"))
if a <=0:
    system.exit

t = int (input ("tempo"))
if t <=0:
    system.exit

    print (v * t + (( a * t ** 2) / 2))












# calculo de delta

import sys

distanc=int (input("informe a distancia em km"))
if distanc <=0:
    sys.exit("informe a distancia positiva")

v_ini = int (input("informe o km/h"))
if distanc <=0:
    sys.exit ("informe a velocidade positiva")

aceler = int (input("informe m/s**"))
if aceler <=0:
    sys.exit ("informe a aceleração positiva")

distanc *= 1000
v_ini /= 3.6

delta = v_ini**2-4*aceler*distanc
if delta <=0:
    sys.exit ("não é possivel calcular o tempo")

t = (-v_ini + delta**0,5)/(2*aceler)
delta = (v_ini**2-4*aceler*distanc)

print ("tempo={hora}:{minuto}:{segundo}")
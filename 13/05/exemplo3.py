from logging import exception
import sys

try:
   intDividendo = int(input("digite o dividendo: "))
   intDivisor = int(input("digite o dividendo: "))
   fltResultado = intDividendo/intDivisor
except ValueError:
    print('ERRO informe um valor que possa ser convertido em inteiro.')
except ZeroDivisionError:
    print('ERRO não existe divisão por zero.')
except Exception as tipoExcecao:
    print(f'ERRO: {sys.exc_info()}')
else:
    print(fltResultado)




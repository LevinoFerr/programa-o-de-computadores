# Calculo da media geral do aluno


import sys

Etapa1 = int(input('informe a nota da etapa 1 :'))
if Etapa1 < 0 or Etapa1 > 100:
     sys.exit("ERRO: Nota etapa 1 invalida, informe nota entre 0 e 100")

Etapa2 = int(input('informe a nota da etapa 2 :'))
if Etapa1 < 0 or Etapa1 > 100:
     sys.exit("ERRO: Nota etapa 2 invalida, informe nota entre 0 e 100")

# calculando media do aluno
media = int( round ( ( Etapa1 * 2 + Etapa2*3) / 5,0) )
print(f"media do aluno: {media}")


#verificando situação do aluno

if media >= 60:
    print("aluno aprovado.")
elif media >= 20:
    print("aluno em prova final.")
else:
    print('aluno reprovado.') 
  
   
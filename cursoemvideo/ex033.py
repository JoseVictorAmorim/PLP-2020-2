n1 = float(input('Qual o \033[4mprimeiro\033[m número? '))
n2 = float(input('Qual o \033[4msegundo\033[m número? '))
n3 = float(input('Qual o \033[4mterceiro\033[m número? '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número dentre os escolhidos é \033[32m{}\033[m, e o menor é \033[31m{}\033[m'.format(maior, menor))

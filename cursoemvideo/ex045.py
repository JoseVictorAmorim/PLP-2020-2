import random
from time import sleep
print('\033[36m-='*10)
print('PEDRA PAPEL TESOURA')
print('-='*10)
print('''\033[36m[0] PARA ESCOLHER \033[4;36mPEDRA\033[m
\033[36m[1] PARA ESCOLHER \033[4;36mPAPEL\033[m
\033[36m[2] PARA ESCOLHER \033[4;36mTESOURA\033[m''')
print('\033[36m-='*13)
jogada = int(input('\033[mQual a sua jogada? ')) #registra a escolha do jogador
jogador = 0
if jogada == 0: #Começo das opções do jogador
    jogador = 'PEDRA'
    print('Sua jogada é {}!'.format(jogador))
elif jogada == 1:
    jogador = 'PAPEL'
    print('Sua jogada é {}!'.format(jogador))
elif jogada == 2:
    jogador = 'TESOURA'
    print('Sua jogada é {}!'.format(jogador))
else:
    print('Por favor, tente novamente e escolha um valor válido')#Término das opções do jogador
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
opc = ['PEDRA', 'PAPEL', 'TESOURA'] #lista de opções pro computador
computador = random.choice(opc) #escolha do computador dentre a lista
if computador == 'PEDRA':
    if jogador == 'PEDRA':
        print('Você escolheu {}, o computador escolheu {}, portanto, deu EMPATE!'.format(jogador, computador))
    if jogador == 'PAPEL':
        print('Você escolheu {}, o computador escolheu {}, portanto VOCÊ VENCEU!'.format(jogador, computador))
    elif jogador == 'TESOURA':
        print('Você escolheu {}, o computador escolheu {}, portanto o COMPUTADOR VENCEU!'.format(jogador, computador)) # #
elif computador == 'PAPEL':
    if jogador == 'PEDRA':
        print('Você escolheu {}, o computador escolheu {}, portanto o COMPUTADOR VENCEU!'.format(jogador, computador))
    elif jogador == 'PAPEL':
        print('Você escolheu {}, o computador escolheu {}, portanto deu EMPATE!'.format(jogador, computador))
    elif jogador == 'TESOURA':
        print('Você escolheu {}, o computador escolheu {}, portanto VOCÊ VENCEU!'.format(jogador, computador))
elif computador == 'TESOURA':
    if jogador == 'PEDRA':
        print('Você escolheu {}, o computador escolheu {}, portanto VOCÊ GANHOU!'.format(jogador, computador))
    elif jogador == 'PAPEL':
        print('Você escolheu {}, o computador escolheu {}, portanto o COMPUTADOR GANHOU!'.format(jogador, computador))
    elif jogador == 'TESOURA':
        print('Você escolheu {}, o computador escolheu {}, portanto deu EMPATE!'.format(jogador, computador))

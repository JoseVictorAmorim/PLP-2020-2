from time import sleep
from random import randint
contvitorias = 0
while True:
    print('******PAR OU IMPAR******')
    jogador = str(input('Escolha [P/I]: ')).strip().lower()[0]
    while jogador not in 'pi':
        jogador = str(input('Faça uma escolha válida [Par ou Impar]: ')).strip().lower()[0]
    if jogador == 'p':
        print('Você escolheu PAR!')
        print('O computador é IMPAR!')
    elif jogador == 'i':
        print('Você escolheu IMPAR!')
        print('O computador é PAR!')
    sleep(1)
    jogada = int(input('Agora, escolha o número que vai jogar: '))
    jogadapc = randint(0, 10)  # computador escolhe entre 0 e 10
    soma = jogadapc + jogada
    sleep(1)
    print(f'O computador jogou {jogadapc}! Portanto, a soma é {soma}!')
    sleep(1)
    if jogador == 'p' and soma % 2 == 0:
        print(f'Como {soma} é par, você VENCEU!')
        contvitorias += 1
        sleep(1)
    elif jogador == 'p' and soma % 2 != 0:
        print(f'Como {soma} é impar, você PERDEU!')
        break
    elif jogador == 'i' and soma % 2 == 0:
        print(f'Como {soma} é par, você PERDEU!')
        break
    elif jogador == 'i' and soma % 2 != 0:
        print(f'Como {soma} é impar, você VENCEU!')
        contvitorias += 1
        sleep(1)
sleep(1)
print('*-*'*20)
print(f'GAME OVER! Você venceu um total de {contvitorias} vezes!')


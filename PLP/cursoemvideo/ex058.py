from random import randint
njogadas = 0
print('JOGO DA ADVINHAÇÃO 2.0')
n = randint(1, 10) #computador escolhe um número
print('Se prepare! Já pensei no meu número!')
jogada = int(input('De 1 a 10, qual foi o número que pensei? '))
while jogada != n:
    njogadas += 1
    if jogada < n:
        jogada = int(input('Mais... tente de novo: '))
    else:
        jogada = int(input('Menos... tente novamente: '))
print('Você acertou! O número que pensei era {} e você precisou de {} jogadas para acertar!'.format(n, njogadas+1))

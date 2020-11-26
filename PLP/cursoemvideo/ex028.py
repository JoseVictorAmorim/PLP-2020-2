import random
print('\033[34m='*36)
print('\033[7;30mSeja bem vindo ao jogo de advinhação\033[m')
print('\033[34m=\033[m'*36)
n = random.randint(0, 5) #Escolhe o número do computador
print('Se prepare! Já decidi o meu \033[32mnúmero\033[m!')
guess = int(input('Agora, tente adivinhar qual foi o número que escolhi: ')) #Escolha do jogador
if guess == n:
    print('Você \033[32mganhou!\033[m O número que pensei era exatemente {}'.format(n))
else:
    print('Você \033[31mperdeu!\033[m O número que pensei era {}, e não {}!'.format(n, guess))



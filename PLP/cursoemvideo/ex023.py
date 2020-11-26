n = int(input('Escolha um numero de 0000 a 9999: '))
dig1 = n // 1 % 10
dig2 = n // 10 % 10
dig3 = n // 100 % 10
dig4 = n // 1000 % 10
print('As casas desse numero são: \nUnidade: {0} \nDezena: {1} \nCentena: {2} \nMilhar: {3}'.format(dig1, dig2, dig3, dig4))
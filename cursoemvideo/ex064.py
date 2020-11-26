n = int(input('Digite um número (999 interromperá o programa): '))
soma = cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite outro número (999 interromperá o programa): '))
if cont == 0:
    print('Você não digitou nenhum número, portanto a soma é 0!')
else:
    print('Você digitou {} número(s), e a soma do(s) número(s) digitado(s) é {}!'.format(cont, soma))

soma = 0
for c in range(1, 7):
    n = int(input('DIGITE O {}º VALOR: '.format(c)))
    if n%2 == 0:
        soma = soma+n
if soma == 0:
    print('Não houve números pares. Por isso a soma é 0')
else:
    print('A soma dos números pares, dentre os digitados, é igual a {}'.format(soma))

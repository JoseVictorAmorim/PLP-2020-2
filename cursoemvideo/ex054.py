from datetime import date
anoatual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    anonasc = int(input('Qual o ano de nascimento da pessoa {}? '.format(c)))
    idade = anoatual-anonasc
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('Ao total, tivemos {} pessoas maiores de idade e {} menores!'.format(maiores, menores))
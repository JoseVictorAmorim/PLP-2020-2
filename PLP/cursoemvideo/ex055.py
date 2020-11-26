maiorp = 0
menorp = 800
for c in range(1, 6):
    peso = (int(input('Qual o peso da {}ª pessoa? '.format(c))))
    if c == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        elif peso < menorp:
            menorp = peso
print('O maior peso é {}kg, e o menor {}kg!'.format(maiorp, menorp))


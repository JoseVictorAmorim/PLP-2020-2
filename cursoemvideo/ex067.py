n = 0
while True:
    n = int(input('Digite o número para ver sua tábuada: '))
    if n < 0:
        break
    else:
        print('-' * 15)
        for c in range (1, 11):
            print(f'{n} X {c} = {n*c}')
        print('-' * 15)
print('Progama Encerrado ☻')
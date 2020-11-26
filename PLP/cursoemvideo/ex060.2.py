from math import factorial
n = int(input('Digite um número para ver seu fatorial: '))
print('{}!= '.format(n), end='')
for c in range(n, 1, -1):
    print('{} X '.format(c,), end='')
    c -= 1
    if c == 1:
        print('{} = {}'.format(c, factorial(n)))
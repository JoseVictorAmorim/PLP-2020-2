from math import factorial
n = int(input('Digite um número para ver seu fatorial: '))
c = n
print('{}!= '.format(c), end='')
while c > 0:
    print(c, end=' ')
    print('X' if c > 1 else '=', end=' ')
    c -= 1
print(factorial(n), end='')
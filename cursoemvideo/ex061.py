a1 = int(input('Qual o primeiro termo da PA (A1)? '))
r = int(input('Qual a razão dessa PA? '))
n = 1
while n <= 10:
    an = a1 + ((n - 1) * r)
    n += 1
    print('A{}={}'.format(n-1, an), end=' ')


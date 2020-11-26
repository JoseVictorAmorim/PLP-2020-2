n = int(input('Quantos termos da sequência de fibonacci você deseja ver? '))
t1 = 0
t2 = 1
cont = 3
print('{}→{}→'.format(t1, t2), end='')
while cont <= n:
    t3 = t2+t1
    print('{}→'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
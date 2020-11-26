a1 = int(input('Qual o primeiro termo da PA (A1)? '))
r = int(input('Qual a razão dessa PA? '))
n = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while n <= total:
        an = a1 + ((n - 1) * r)
        n += 1
        print('{}→'.format(an), end='')
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja mostrar? '))
print('PA finalizada com {} termos exibidos'.format(total))

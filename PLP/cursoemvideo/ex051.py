a1 = int(input('Qual o primeiro termo da PA (A1)? '))
r = int(input('Qual a razão da PA? '))
for c in range(1, 11):
    an = a1+((c-1)*r)
    print(('A{} = {}'.format(c, an)))





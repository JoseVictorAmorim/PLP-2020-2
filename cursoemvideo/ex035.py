r1 = float(input('Qual o valor da primeira reta? '))
r2 = float(input('Qual o valor da segunda reta? '))
r3 = float(input('E o valor da terceira reta? '))
if r1<r2+r3 and r2<r1+r3 and r3<r2+r1:
    print('A junção dos tres segmentos podem formar um triangulo!')
else:
    print('Os tres segmentos não podem formar um triangulo!')
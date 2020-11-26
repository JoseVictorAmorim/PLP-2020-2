r1 = float(input('Qual o valor do primeiro segmento? '))
r2 = float(input('Qual o valor do segundo segmento? '))
r3 = float(input('Qual o valor do terceiro segmento? ' ))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    a = True
else:
    a = False
if a == True and r1 == r2 == r3:
    print('As retas podem formar um triangulo, e ele será EQUILÁTERO!')
elif a == True and r1 == r2 != r3 or r1 != r2 == r3 or r3 == r1 != r2:
    print('As retas podem formar um triangulo que será ISÓCELES!')
elif a == True and r1 != r2 != r3 != r1:
    print('As retas podem formar um triangulo que será ESCALENO!')
elif a == False:
    print('As retas não podem formar um triangulo!')
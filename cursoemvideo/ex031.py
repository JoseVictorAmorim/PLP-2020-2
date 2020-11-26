D = float(input('Qual a quilometragem total da viagem? '))
p1 = D * (0.45)
p2 = D * (0.5)
if D>200:
    print('Em uma viagem de {}KM, o valor total será \033[32mR${:.2f}\033[m'.format(D, p1))
else:
    print('Na distancia de {}KM, sua viagem sai por \033[32mR${:.2f}\033[m'.format(D, p2))

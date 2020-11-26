v = float(input('Qual a velocidade do carro, em KM/H? '))
valor = (v-80)*7
if v>80:
    print('Você foi \033[31;40mmultado\033[m por excesso de velocidade!')
    print('Como sua velocidade era de \033[4m{:.0f}Km/H\033[m, você foi multado em \033[31mR${:.2f}\033[m!'.format(v, valor))
else:
    print('Sua velocidade está dentro do permitido pela rodovia! \033[32mBoa Viagem!\033[m')

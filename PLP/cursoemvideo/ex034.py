inicial = float(input('Qual o salario inicial do funcionário? R$'))
ten = (10/100)*inicial
fit = (15/100)*inicial
if inicial > 1250:
    a = ten+inicial
    print('O salário do funcionário, apos o aumento de \033[32m10%\033[m, será de R${:.2f}'.format(a))
else:
    b = fit+inicial
    print('O salário desse funcionário, apos aumento de \033[32m15%\033[m, será de R${:.2f}'.format(b))



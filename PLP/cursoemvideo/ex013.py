sinicial = float(input('Qual o salario inicial do funcionário? '))
aumento = sinicial*15/100
sfinal = sinicial+aumento
print('O funcionário que recebe {}, após seu aumento de \033[32;m15%\033[m, passará a receber {:.2f} '.format(sinicial, sfinal))
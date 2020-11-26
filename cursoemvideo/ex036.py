print('\033[31m='*63)
print('SISTEMA DE APROVAÇÃO DE EMPRÉSTIMO BANCARIO PARA COMPRA DE CASA')
print('='*63)
Vcasa = float(input('\033[mQual o \033[4mvalor\033[m da Casa? R$ '))
Vsalario = float(input('Qual o \033[4msalario mensal\033[m do interessado no empréstimo? '))
Vanos = int(input('Em \033[4mquantos\033[m \033[4manos\033[m serão divididos o pagamento da casa? '))
meses = Vanos*12
vparcelas = Vcasa/meses
if vparcelas > (30/100)*Vsalario :
    print('Infelizmente, sua renda mensal não consegue se adequar aos requisitos, pois seria necessário mais que \033[4m30%\033[m do seu valor mensal para cobrir o valor da casa no prazo estipulado')
    print('Nesse caso, seriam necessário {} parcelas de R${:.2f}'.format(meses, vparcelas))
else:
    print('Seu empréstimo foi \033[32maceito\033[m! Você pagará {} parcelas de R${:.2f}!'.format(meses, vparcelas))

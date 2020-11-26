valor = float(input('Qual o valor da compra? R$'))
print('''\033[4mFORMAS DE PAGAMENTO\033[m
[1] À VISTA \033[34m(Dinheiro ou Cheque\033[m-10% de desconto
[2] À VISTA NO CARTÃO \033[34m(Débito ou Crédito)\033[m-5% de desconto
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO (20% de Juros)''''')
opcao = int(input('Qual a condição de pagamento? '))
if opcao == 1:
    desc = valor-((10/100)*valor)
    print('Pagando à vista (em dinheiro ou cheque), você obtém \033[4;32m10% de desconto\033[m! O valor a pagar é R${:.2f}!'.format(desc))
elif opcao == 2:
    desc = valor-((5/100)*valor)
    print('Pagando à vista no cartão, você recebe um \033[4;32mdesconto de 5%\033[m! O novo valor a pagar é de R${:.2f}!'.format(desc))
elif opcao == 3:
    parcela = valor/2
    print('Escolhendo parcelar sua compra em 2X no cartão, o valor a pagar são 2X de R${:.2f}, totalizando R${:.2f}'.format(parcela, valor))
elif opcao == 4:
    qtde = int(input('Em quantas parcelas será dividido o valor final? '))
    if qtde < 3:
        print('Por favor, escolha uma quantidade de parcelas válidas (acima de 3)')
    juros = valor+((20/100)*valor)
    parcela = juros/qtde
    print('Parcelando sua compra em {}X no cartão, serão pagas parcelas de R${:.2f}, totalizando R${:.2f}.'.format(qtde, parcela, juros))
else:
    print('Por Favor, tente novamente e escolha uma opção válida')
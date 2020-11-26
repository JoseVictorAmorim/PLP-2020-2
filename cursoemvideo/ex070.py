valorgasto = maisdecem = valorcaro = 0
maiscaro = maisbarato =''
valorbarato = 24259234590
print('=' * 20)
print('PROGRAMA DE COMPRAS')
print('=' * 20)
while True:
    nomeprod = str(input('DIGITE O NOME DO PRODUTO: '))
    valorprod = int(input('DIGITE O VALOR DO PRODUTO: '))
    print('=' * 20)
    valorgasto += valorprod
    if valorprod > valorcaro:
        valorcaro = valorprod
        maiscaro = nomeprod
    if valorprod < valorbarato:
        valorbarato = valorprod
        maisbarato = nomeprod

    if valorprod >= 1000:
        maisdecem += 1
    print('=' * 20)
    pg = str(input('Deseja cadastrar um novo produto? [Sim ou Não] ')).strip().lower()[0]
    while pg not in 'sn':
        print('Por Favor, dê uma resposta válida! [Sim ou Não]')
        pg = str(input('Deseja cadastrar um novo produto? [Sim ou Não] ')).strip().lower()[0]
    if pg == 'n':
        break
print(f'Valor Total da compra= R${valorgasto:.2f}')
print(f'Total de itens com custo superior a R$1000: {maisdecem}')
print(f'O produto de maior valor é {maiscaro}, com custo de R${valorcaro:.2f}, enquanto o mais barato é {maisbarato}, e seu valor é R${valorbarato:.2f}')

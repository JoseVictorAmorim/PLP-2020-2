from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    sleep(1)
    print('*'*20)
    print('''[1] para somar os dois números
[2] para multiplicar os números
[3] para saber qual o maior dentre os números
[4] para digitar novos números
[5] para sair''''')
    print('*'*20)
    opção = int(input('Qual a opção desejada? '))
    if opção == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif opção == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1>n2:
            print('O maior número dentre os dois é {}!'.format(n1))
        elif n2>n1:
            print('O maior número dentre os dois é {}!'.format(n2))
        else:
            print('Os dois números são iguais!')
    elif opção == 4:
        print('Certo.')
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opção == 5:
        print('OK, Volte sempre!')
    else:
        print('Opção inválida. Tente novamente!')
    print('*' * 20)


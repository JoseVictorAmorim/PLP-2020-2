n1 = float(input('Qual o valor do \033[4mprimeiro\033[m número? '))
n2 = float(input('Qual o valor do \033[4msegundo\033[m número? '))
if n1>n2:
    print('Dentre os dois, o primeiro número é maior')
elif n1<n2:
    print('Dentre os escolhidos, o maior é o segundo número')
elif n1==n2:
    print('Os números escolhidos possuem o mesmo valor')

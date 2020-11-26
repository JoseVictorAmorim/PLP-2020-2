nascimento = int(input('Qual o ano de nascimento? '))
idade = 2019-nascimento
if idade > 18:
    tempo = idade-18
    print('Já passou da hora de se alistar! Seu alistamento deveria ter sido realizado {} ano(s) atrás, em {}'.format(tempo, nascimento+18))
elif idade == 18:
    print('Está na hora de se alistar! Prepare sua documentação!')
else:
    tempo = 18-idade
    print('Ainda não é hora de se alistar! Faltam {} ano(s) para você ter de se alistar! '.format(tempo))
    print('Seu alistamento será em {}'.format(nascimento+18))
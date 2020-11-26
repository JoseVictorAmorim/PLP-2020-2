print('Exercicio de funções "is" ')
x = input('Digite algo para que possamos realizar a leitura: ')
print('Chamaremos o que foi digitado de X. Sabendo disso, confira:')
print('Qual o tipo primitivo de X?', type(x))
print('X é apenas numerico?', x.isnumeric())
print('X é apenas lexical?', x.isalpha())
print('X é digitado apenas com letras minusculas?', x.islower())
print('X é digitado apenas com letras maiusculas?', x.isupper())


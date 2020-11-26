sexo = str(input('Qual o sexo da pessoa? [M/F]  ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Por favor, digite um sexo válido (M ou F): ')).upper().strip()[0]
if sexo == 'M':
    print('Sexo masculino cadastrado com sucesso!')
elif sexo == 'F':
    print('Sexo feminino cadastrado com sucesso!')

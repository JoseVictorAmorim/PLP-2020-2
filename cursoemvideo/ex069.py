maior18 = homens = mulheres20 = 0
while True:
    print('='*20)
    print('CADASTRAMENTO')
    print('='*20)
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo? M/F')).strip().lower()[0]
    while sexo not in 'mf':
        sexo = str(input('Por favor, escolha um sexo válido! [Masculino ou Feminino] '))
    if idade >= 18:
        maior18 += 1
    if sexo == 'm':
        homens += 1
    if idade >= 20 and sexo == 'f':
        mulheres20 += 1
    pg = str(input('Deseja cadastrar uma nova pessoa? [S/N] ')).strip().lower()[0]
    while pg not in 'sn':
        print('Por favor, escolha uma resposta válida! [Sim ou Nao]')
        pg = str(input('Deseja cadastrar uma nova pessoa? [S/N] ')).strip().lower()[0]
    if pg == 'n':
        break
print(f'Você cadastrou {maior18} pessoas maiores de 18 anos, {homens} homens no total e {mulheres20} mulheres com mais de 20 anos!')
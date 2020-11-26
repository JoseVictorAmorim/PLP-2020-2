ano = int(input('Qual o ano de nascimento do participante? '))
idade = 2019-ano
if idade == 0:
    print('Você não está tentando inscrever um bebê em um campeonato de natação, está?')
elif 1 < idade <= 9:
    print('O candidato possui {} anos e pertence à categoria \033[4;34mMIRIM\033[m'.format(idade))
elif 10 < idade <= 14:
    print('O participante, de {} anos, pertence à categoria \033[4;34mINFANTIL\033[m'.format(idade))
elif 15 < idade <= 19:
    print('Este participante, com {} anos, se encaixa na categoria \033[4;34mJUNIOR\033[m'.format(idade))
elif 19 < idade <= 20:
    print('Com {} anos, o participante pertence à categoria \033[4;34mSENIOR\033[m'.format(idade))
elif idade>20:
    print('O candidato de {} anos pertence a categoria \033[4;34mMASTER\033[m'.format(idade))


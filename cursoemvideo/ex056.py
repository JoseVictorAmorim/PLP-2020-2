from time import sleep
nome = ''
idade = []
sexo = ['M', 'F']
homens = 0
mulheres = 0
hvelho = 0
hveio = ''
m20 = 0
for c in range(1, 5):
    print('='*10, 'DADOS DA {}ª PESSOA'.format(c), '='*10)
    nome = str(input('Qual o nome? ')).strip()
    inpuidade = int(input('Qual a idade? '))
    idade += [inpuidade]
    sidade = sum(idade)
    sexo = str(input('Qual o sexo? \033[34mResponda com M ou F\033[m ')).strip().upper()
    if sexo == 'F':
        mulheres += 1
        if inpuidade < 20:
            m20 += 1
    elif sexo == 'M':
        homens += 1
        if c == 1:
            hvelho = inpuidade
            hveio = nome
        else:
           if inpuidade > hvelho:
                hvelho = inpuidade
                hveio = nome
print('='*9, 'AVALIANDO RESULTADOS', '='*9)
sleep(2)
print('A media das idades das 4 pessoas é {:.1f} anos!'.format(float(sidade/c)))
print('O homem mais velho do grupo é {}, com {} anos!'.format(hveio, hvelho))
print('Dentre o grupo, há {} mulheres com menos de 20 anos!'.format(m20))


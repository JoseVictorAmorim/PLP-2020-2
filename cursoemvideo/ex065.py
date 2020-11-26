n = int(input('Digite um valor: '))
pg = str(input('Deseja digitar outro número [S/N]? ')).strip().upper()
while pg not in 'SN':
    pg = str(input('Responda com S ou N. Deseja digitar outro valor? ')).upper().strip()
cont = 1
maior = menor = soma = n
while pg != 'N':
    n = int(input('Digite outro valor: '))
    cont += 1
    soma += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    media = soma/cont
    pg = str(input('Deseja digitar outro número [S/N]? ')).strip().upper()
print('A média entre os números digitados foi {}, o maior número digitado foi {} e o menor foi {}!'.format(media, maior, menor))

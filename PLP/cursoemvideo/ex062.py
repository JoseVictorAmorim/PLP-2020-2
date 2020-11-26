a1 = int(input('Qual o primeiro termo da PA (A1)? '))
r = int(input('Qual a razão dessa PA? '))
n = 1 #número de termos
total = 0 #total de termos já somados na PA
mais = 10 #quantidade base de vezes que irá repetir a mais. 10 por padrão para mostrar os 10 primeiros
while mais != 0: #Laço acabará quando o valor a mais for igual a 0. No momento igual a 10
    total += mais #Total de termos = o número de termos a mais. Inicialmente 10. Quando somado a mais, partirá do 10
    while n <= total: #Enquanto o número de termos for menor ou igual ao total de termos a ser mostrado
        an = a1 + ((n - 1) * r) #Formula do AN
        n += 1 #N recebe +1 até ultrapassar em 1 o valor do total de termos (pela formula, n-1*r
        print('{}→'.format(an), end='') #mostra o AN
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? ')) #Input que adiciona mais algum valor a variavel mais. Esse valor será somado na quantidade total de termos apresentados +10
print('Progressão finalizada com {} termos mostrados!'.format(total))

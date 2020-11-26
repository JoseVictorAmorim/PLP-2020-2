#Utilizando a linguagem Python (3.*), escreva expressões algébricas correspondentes aos
##seguintes comandos:
##(a) A soma dos 5 primeiros inteiros positivos.
##(b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
##(c) O número de vezes que 73 cabe em 403.
##(d) O resto de quando 403 é dividido por 73.
##(e) 2 à 10a potência.
##(f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).

while True:
    print('''''(a) A soma dos 5 primeiros inteiros positivos.
'(b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31)."
'(c) O número de vezes que 73 cabe em 403.
'(d) O resto de quando 403 é dividido por 73.
'(e) 2 à 10a potência.
'(f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas). ''''''''')
    choice = input("escolha: ")
    if(choice == 'a'):
        print(1+2+3+4+5)
    elif(choice == 'b'):
        medium = (23+19+31)/3
        print(medium)
    elif(choice == 'c'):
        sevThree = 403/73
        print(sevThree)
    elif(choice == 'd'):
        remain = 403%73
        print(remain)
    elif(choice == 'e'):
        print(2**10)
    elif(choice == 'f'):
        print(3)
    elif(choice == 'j'):
        break

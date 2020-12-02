#UTF-8
import math
import sys

nome_arquivo = sys.argv[1]

cont=0
arq = open(nome_arquivo, 'r')

with open(nome_arquivo) as my_file:
    my_file.seek(0)
    primeiro = my_file.read(1)
    if not primeiro:
        print("Arquivo Vazio")
        exit()
    else:
        my_file.seek(0)
        

for linha in arq:
    cont += 1

arq.close()


dadosx = []
dadosy = []

arq1 = open(nome_arquivo, 'r')
try:
    
    for linha in arq1.readlines():
         x,y = map(float, linha.split(','))
         dadosx.append(x)
         dadosy.append(y)

    somax = 0
    somay = 0

    for soma in dadosx:
        somax += soma

    for soma in dadosy:
        somay += soma

    aritmeX = somax/cont
    aritmeY = somay/cont

    aux = 0
    somacima = 0

    while aux < cont:
        somacima = somacima + ((dadosx[aux] - aritmeX)*(dadosy[aux] - aritmeY))
        aux += 1

    aux1 = 0
    quadraX = 0
    quadraY = 0


    while aux1 < cont:
        quadraX = quadraX + ((dadosx[aux1] - aritmeX)**2)
        quadraY = quadraY + ((dadosy[aux1] - aritmeY)**2)
        aux1 += 1


    raizbaixo = math.sqrt((quadraX * quadraY))


    cp = somacima/raizbaixo

    print(cp)


except ValueError:
    print("Dados Invalidos")
    exit()

arq1.close()









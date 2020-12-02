import sys
import math

def xbar(lista):
    n1 = sum(lista)
    n2 = 1/(len(lista))
    return float(n2*n1)

def parteCima(lista1, lista2, tamanho):
    soma = 0
    xb = xbar(lista1)
    yb = xbar(lista2)
    
    for i in range(0, tamanho):
        soma += ((lista1[i]-xb)*(lista2[i]-yb))
    
    return float(soma)

def somaBaixo(lista, barrado):
    soma = 0
    for i in lista:
        soma += ((i - barrado))**2
    return float(soma)

def parteBaixo(lista1, lista2, tamanho):
    soma = 0
    xb = xbar(lista1)
    yb = xbar(lista2)
    somaX = float(somaBaixo(lista1, xb))
    somaY = float(somaBaixo(lista2, yb))
    baixo = math.sqrt(somaX) * math.sqrt(somaY)
    return float(baixo)

def person(lista1, lista2, tamanho):
    cima = parteCima(lista1, lista2, tamanho)
    baixo = parteBaixo(lista1, lista2, tamanho)
    return float((cima/baixo))
       
fileName = sys.argv[1]
dadosx = []
dadosy = []
contadorLinhas = 0
presente = False

with open(fileName, 'r') as myFile:
    myFile.seek(0)
    primeiro = myFile.read(1)
    if(primeiro):
        presente = True
        myFile.seek(0)
    else:
        print("Arquivo Vazio")
        exit()


if(presente):
    with open(fileName, 'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            contadorLinhas += 1
            x,y = line.split(',')
            dadosx.append(x)
            dadosy.append(y.strip())
    try:
        xs = [float(i) for i in dadosx]
        ys = [float(i) for i in dadosy]
    except:
        print("Impossivel converter para float")
        exit()
    print(person(xs, ys, contadorLinhas))

def meuIMC(size, weight):
    imc = weight / size**2
    round(imc, 2)
    if (imc < 18.5):
        print(f'Abaixo do peso! IMC = {imc:.2f}')
    elif ((imc >= 18.5) and (imc < 25)):
        print(f'Peso normal! IMC = {imc:.2f}')
    elif (imc >= 25):
        print(f'Sobrepeso! IMC = {imc:.2f}')


mySize = float(input('Digite sua altura: '))
myWeight = float(input('Digite seu peso: '))
meuIMC(mySize, myWeight)



num1 = float(input('Digite o 1º numero: '))
num2 = float(input('Digite o 2º numero: '))

try:
    print(num1/num2)
except:
    print("Erro, divisão por 0!")
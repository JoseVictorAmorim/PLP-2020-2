n = int(input('Qual o valor inteiro a ser convertido? '))
print('='*19)
print('TABELA DE CONVERSÃO')
print('='*19)
print('\033[4m1\033[m para \033[31mBINÁRIO\033[m'
      '\n\033[4m2\033[m para \033[32mOCTAL\033[m'
      '\n\033[4m3\033[m para \033[33mHEXADECIMAL\033[m')
print('='*19)
conv = int(input('Qual séra a base de conversão? '))
if conv == 1:
    print('O número {}, na base escolhida (Binário) é igual a: '.format(n))
    print(bin(n)[2:])
elif conv == 2:
    print('O número {}, na base escolhida (Octal) é igual a: '.format(n))
    print(oct(n)[2:])
elif conv == 3:
    print('O número {}, na base escolhida (Hexadecimal) é igual a : '.format(n))
    print(hex(n)[2:])
else:
    print('Por favor, escolha uma base válida')

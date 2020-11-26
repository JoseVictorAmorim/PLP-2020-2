print('\033[34m-'*18)
print('CALCULADORA DE IMC')
print('-'*18)
peso = float(input('\033[mQual o peso, em KG? '))
altura = float(input('Qual a altura, em M? '))
IMC = peso/(altura**2)
if IMC < 18.5:
    print('O IMC calculado, {:.1f}, está \033[4mABAIXO DO PESO\033[m'.format(IMC))
elif 18.5 < IMC <= 25:
    print('O IMC calculado, {:.1f}, está no \033[4mPESO IDEAL\033[m'.format(IMC))
elif 25 < IMC <= 30:
    print('O IMC calculado, {:.1f} está em \033[4mSOBREPESO\033[m'.format(IMC))
elif 30 < IMC < 40:
    print('O IMC calculado, {:.1f}, está em nível de \033[4mOBESIDADE\033[m'.format(IMC))
else:
    print('Os níveis de IMC apresentam quadro de \033[4mOBESIDADE MÓRBIDA\033[m, com indices de {:.1F}'.format(IMC))

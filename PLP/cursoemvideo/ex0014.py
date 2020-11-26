celsius = float(input('Qual o valor da temperatura em ºC? '))
kelvin = celsius+273
farenheit = ((celsius*9)+160)/5
print('A temperatura de {}ºC equivale a {:.2f}ºK e a {:.2f}ºF!'.format(celsius, kelvin, farenheit))

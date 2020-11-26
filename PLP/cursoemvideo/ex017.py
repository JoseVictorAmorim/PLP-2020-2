import math
CO = float(input('Qual o valor do cateto oposto do triangulo retangulo em questão? '))
CA = float(input('Qual o valor do cateto adjascente desse triangulo? '))
CO2 = math.pow(CO, 2)
CA2 = math.pow(CA, 2)
HIP = math.sqrt((CO2+CA2))
print('Um triangulo cujo Cateto Oposto valha {}, Cateto adjascente valha {}, tem como Hipotenusa {:.2f}'.format(CO, CA, HIP))

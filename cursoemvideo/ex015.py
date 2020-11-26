dias = float(input('Quantos dias o carro ficou alugado? '))
km = int(input('Quantos KM foram rodado com o carro nesse periodo? '))
vdias = dias*60
vkm = km*(0.15)
vtotal = vdias+vkm
print('Considerando que cada dia com o carro custa R$ 60,00, e cada KM rodado custa R$0,15, o valor total a se pagar pelo aluguel desse carro é {:.2f}'.format(vtotal))

cidade = str(input('Qual o nome da cidade a ser analisada? ')).strip()
low = cidade.lower()
div = low.split()
santo = 'santo'in div[0]
print('É {} que a cidade escolhida começa com Santo'.format(santo))

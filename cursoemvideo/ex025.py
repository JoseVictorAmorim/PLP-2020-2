nome = str(input('Qual o nome para ser analisado? ')).strip()
low = nome.lower()
silva = 'silva' in low
print('É {} que essa pessoa possui Silva em seu nome!'.format(silva))
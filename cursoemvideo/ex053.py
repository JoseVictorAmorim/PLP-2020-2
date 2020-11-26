frase = str(input('Qual a frase a ser analisada? ')).strip().lower()
fsem = frase.split()
j = ''.join(fsem)
nletras = len(j)
inverso = ''
for c in range(nletras-1, -1, -1):
    inverso += j[c]
if inverso == j:
    print('A frase digitada, ao contrário, fica: {}, portanto se trata de um palindromo!'.format(frase))
else:
    print('A frase ao contrario não fica igual a digitada! Portanto, não se trata de um palindromo')
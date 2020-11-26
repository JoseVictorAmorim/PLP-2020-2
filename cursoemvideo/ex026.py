frase = str(input('Digite uma frase: ')).strip()
f = frase.lower()
div = f.split()
j = ''.join(div)
a = j.count('a')
print('O numero de vezes que aparece a letra A nessa frase é: {}'.format(a))
primeira = j.find('a')
r = primeira+1
print('A  primeira vez que essa letra aparece é na{}º posição'.format(r))
ultima = j.rfind('a')
l = ultima+1
print('A ultima vez que essa letra aparece é na {}º posição'.format(l))

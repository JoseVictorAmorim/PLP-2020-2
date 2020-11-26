n = str(input('Qual o nome completo? ')).strip()
div = n.split()
primeiro = div[0]
ultimo = div[len(div)-1]
print('Primeiro nome: \033[34m{}\033[m \nUltimo nome: \033[35m{}\033[m'.format(primeiro, ultimo))

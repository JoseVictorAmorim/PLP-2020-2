n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno?  '))
media = (n1+n2)/2
if media < 5.0:
    print('O aluno, com média de {:.1f}, foi \033[31mREPROVADO\033[m'.format(media))
elif 5.0 < media < 6.9:
    print('O aluno, com média de {:.1f}, está de \033[34mRECUPERAÇÃO\033[m'.format(media))
elif media >= 7.0:
    print('O aluno obteve uma média de {:.1f} e foi \033[32mAPROVADO\033[m'.format(media))

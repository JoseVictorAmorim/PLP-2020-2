import datetime
ano = int(input('Qual a ano a ser avaliado? '))
if ano == 0:
    ano = datetime.date.today().year
if ano%4 == 0 and ano%100 !=0 or ano%400 == 0:
    print('O ano de {} é/será \033[4;32mbissexto\033[m!'.format(ano))
else:
    print('O ano de {} não é/será \033[4;31mbissexto\033[m!'.format(ano))
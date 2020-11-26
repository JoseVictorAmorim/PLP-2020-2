import cmath, math
ang = int(input('Qual o valor do angulo, em º? '))
math.radians(ang)
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O angulo {}º tem como seno: {:.2f}, como cosseno {:.2f} e como tangente {:.2f}'.format(ang, sen, cos, tg))

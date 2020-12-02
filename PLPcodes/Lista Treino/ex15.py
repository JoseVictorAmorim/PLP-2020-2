def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)

number = int(input('Digite um numero: '))
print(fatorial(number))
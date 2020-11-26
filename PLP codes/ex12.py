lista = [3, 6, 23, 67, -98, 8, 90, -8, 0]
media = sum(lista)/9

for c in range(0, 9):
    if lista[c] >= media:
        print(lista[c])

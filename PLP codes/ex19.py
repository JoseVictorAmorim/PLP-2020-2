num = input("Digite algo para ser convertido para float: ")

while True:
    try:
        #num = input("Digite algo para ser convertido para float: ")
        num = float(num)
        print(type(num))
        break
    except:
        num = input("Impossivel converter. Digite outra coisa: ")

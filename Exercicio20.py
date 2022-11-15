def escadaNumeros(numero):
    for i in range(numero):
        i += 1
        print(str(i) * i)


numero = int(input('Digite um número: '))
escadaNumeros(numero)
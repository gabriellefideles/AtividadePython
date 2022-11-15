numero = int(input('Digite um número: '))

def escadaNumero(numero):
    for i in range(1, numero + 1):
        print(('{} ').format(i), end='')
    print()

def escadaSequencia(numero):
    for numero in range(numero + 1):
        escadaNumero(numero)

escadaSequencia(numero)


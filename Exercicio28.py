def reverter(numero):
    return str(numero[::-1])

numero = str(input('Digite um número: ')).strip()
print('Numero revertido: {}'.format(reverter(numero)))
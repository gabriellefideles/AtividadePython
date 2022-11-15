def quantidade(numero):
    return len((str(numero)))

numero = str(input('Digite um numero: ')).strip()
print('Esse número tem {} dígitos'.format(quantidade(numero)))
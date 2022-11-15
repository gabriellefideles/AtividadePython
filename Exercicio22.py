def soma(numero1, numero2, numero3):
    valor = numero1 + numero2 + numero3
    return valor

print('Digite os numeros que deseja somar:')
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
numero3 = int(input('Terceiro número: '))

print ("resultado: ", soma(numero1, numero2, numero3))
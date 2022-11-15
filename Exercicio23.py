print('Digite um nujmero para saber se ele e positivo ou negativo')
numero = int(input('digite o valor: '))

def posOuNeg(numero):
    if numero > 0:
        print('P')
    elif numero <= 0:
        print('N')
        
posOuNeg(numero)
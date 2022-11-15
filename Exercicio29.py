import random

def craps():
    dado1 = random.randrange(1,7)
    dado2 = random.randrange(1,7)
    soma = dado1 + dado2
    
    print("Dado 1: ", dado1)
    print("Dado 2: ", dado2)
    print("A soma dos dados é: ", soma)
    
    return soma
    
while True:
    
    jogar = input("Rolar dados (s ou n)? ")
    
    if jogar == 'n' or jogar == 'N':
        break
    else:
        resultado = craps()
    if resultado == 7 or resultado == 11:
        print('Natural, você ganhou!')
        break
    elif resultado == 2 or resultado == 3 or resultado == 12:
        print('Craps, você perdeu!')
    else:
        print("Continue jogando")

while True:
    resultado2 = craps()
    if resultado == resultado2:
        print('Você ganhou!')
        break
    elif resultado2 == 7:
        print('Tente denovo')
        break
    else:
        print("Continue jogando")
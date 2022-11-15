nota= int(input('Dê uma nota de 1 a 10:'))
while nota < 1:
    print('Você não inseriu uma nota de 1 a 10, tente de novo.')
    int(input('Dê uma nota de 1 a 10:'))
if (nota >= 1)and(nota <= 10):
    print('Sua nota foi {}.'.format(nota))
while nota > 10:
    print('Você não inseriu uma nota de 1 a 10, tente de novo.')
    int(input('Dê uma nota de 1 a 10:'))
    
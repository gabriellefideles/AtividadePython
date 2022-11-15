largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

def retangulo(largura, altura):
    if largura > 20:
        largura = 20
    if altura > 20:
        altura = 20
    print('(-)' * largura)
    
    c = 0
    while c < altura:
        z = '|'
        print(f'{z}{z:>{(largura*3 - 1)}}')
        c += 1
    print('(-)' * largura)

retangulo(largura, altura)
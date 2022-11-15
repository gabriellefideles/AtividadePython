print('Digite os numeros que deseja colocar na lista para se fazer a media, digite 0 para fechar a lista')

def listaNumeros():
    lista = []
    numero = ''
    while (numero != 0):
        numero = int(input('Digite um numero: '))
        if (numero != 0):
            lista.append(numero)
    media = sum(lista) / len(lista)
    print('Media feita da lista: {}'.format(media))

listaNumeros()


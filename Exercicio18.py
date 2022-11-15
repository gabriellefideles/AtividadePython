print('Digite "exit" quando tiver acabado a lista')

def mostraListaEnumerada():
    lista = []
    a = ''
    while (a != 'exit'):
        a = input('Insira um elemento: ')
        if (a != 'exit'):
            lista.append(a)
    for numero, lista in enumerate(lista):
        print(numero, lista)

mostraListaEnumerada()
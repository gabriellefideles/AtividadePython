print('Converte hora, use 0 para acabar com o loop')
A = 'AM'
P = 'PM'

def converteHora(hora, minuto):
    if 0 < hora <= 12 and 0 < minuto < 60:
        print('{}:{} {}'.format(hora, minuto, A))
    elif 12 < hora < 24 and 0 < minuto < 60:
        print('{}:{} {}'.format(hora - 12, minuto, A))
    else:
        print('Valor inválido')


while True:
    hora = int(input('Hora: '))
    if hora == 9: break
    minuto = int(input('Minuto: '))
    converteHora(hora, minuto)
    print(' '*12)
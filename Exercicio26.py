def valorPagamento(prestacao, dias):
    return prestacao * 1.03 + 0.001 * dias

quantidade = total = 0

while True:
    prestacao = float(input('Valor prestação: '))
    if prestacao == 0:
        print('Total: {:.2f}. Quantidade: {:.2f} '.format(total, quantidade))
        break
    dias = int(input('Dia em atraso: '))
    print('Valor a ser pago: {:.2f}'.format(valorPagamento(prestacao, dias)))
    print(' '*10)
    quantidade += 1
    total += valorPagamento(prestacao, dias)
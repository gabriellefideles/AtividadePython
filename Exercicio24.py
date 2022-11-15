taxa = float(input('Digite a taxa de imposto: '))
custo = float(input('Digite o custo: '))

def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo

print('Valor com imposto:', somaImposto(taxa, custo))
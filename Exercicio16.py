nome= input("Qual o nome do atleta?")
salto1= float(input('Qual a distância do Primeiro salto?'))
salto2= float(input('Qual a distância do Segundo salto?'))
salto3= float(input('Qual a distância do Terceiro salto?'))
salto4= float(input('Qual a distância do Quarto salto?'))
salto5= float(input('Qual a distância do Quinto salto?'))
saltos= [salto1,salto2,salto3,salto4,salto5]

media = (salto1 + salto2 + salto3 + salto4 + salto5) // 5


print('Resultado final:')
print(f'Atleta:{nome}')
print(f'Saltos:{saltos}')
print(f"Média: {media}")




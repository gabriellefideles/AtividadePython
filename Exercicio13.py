numero = []
for ab in range(1, 6):
    numero.append(int(input("Digite um numero: ")))
somanumero = sum(numero)
quantidade = len(numero)
media = somanumero / quantidade
print('A soma dos números é ', somanumero,'e a média entre eles é', media )
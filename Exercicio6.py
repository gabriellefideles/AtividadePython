vetor1 = []
vetor2 = []
vetor3 = []

for elemento in range(0, 10):
    vetor1.append(int(input("Digite um dos elementos do primeiro grupo: ")))
    
for elemento in range(0, 10):
    vetor2.append(int(input("Digite um dos elementos do segundo grupo: ")))
    
for elemento in range(0, 10):
    vetor3.append(vetor1[elemento])
    vetor3.append(vetor2[elemento])

print(vetor3)
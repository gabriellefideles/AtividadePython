numero=[]
par=[]
impar=[]

for f in range(20):
    Digito= int(input("Digite um numero:"))
    
    numero.append(Digito)
    
    if (Digito %2)==0:
        par.append(Digito)
    else:
        impar.append(Digito)
        
print("Vetor com 20 numeros:"+ str(numero))
print("Vetor com numeros pares:" + str(par))
print("Vetor com numeros impates:" + str(impar))
        
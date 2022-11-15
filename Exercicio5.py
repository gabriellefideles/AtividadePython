Resp1= int(input("Telefonou para a vítima? 1/S ou 0/N:"))
Resp2= int(input("Esteve no local do crime? 1/S ou 0/N:"))
Resp3= int(input("Mora perto da vítima? 1/S ou 0/N:"))
Resp4= int(input("Devia para a vítima? 1/S ou 0/N:"))
Resp5= int(input("Já trabalhou com a vítima? 1/S ou 0/N:")) 

soma_respostas= Resp1+Resp2+Resp3+Resp4+Resp5

if (soma_respostas < 2):
    print("\nInocente")
elif (soma_respostas==2):
    print("\nSuspeito")
elif(3<= soma_respostas<=4):
    print("\Cúmplice")
elif(soma_respostas==5):
    print("\nAssassino")
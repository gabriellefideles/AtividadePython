média_alunos=[]
alunos_acima_media=0 

for aluno in range(10):
     soma_das_notas=0 

     for nota in range(4):
       print("Digite a ", nota+1, "ª nota do ", aluno+1, "º aluno", sep="")
       soma_das_notas += float(input()) 

     média_alunos.append(soma_das_notas/4) 

     if média_alunos[aluno]>= 7.0: 
        alunos_acima_media += 1
print("Média dos alunos:", média_alunos)
print("numeros de alunos acima da media:", alunos_acima_media)
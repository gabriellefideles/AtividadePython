print('Nome: maior que 3 caracteres, Idade: entre 0 e 150, Salário: maior que zero,Sexo: f ou m, Estado Civil: s, c, v, d')
a = str(input('Digite seu nome: '))
while len(a) <= 3 :
    a = str(input('Digite seu nome: '))

b = int(input('Digite sua idade: '))
while b < 0 or b > 150:
    b = int(input('Digite sua idade: '))
    
c = float(input('Digite o seu salário: '))
while c < 0:
    c = float(input('Digite o seu salário: '))

d = str(input('informe a inicial do seu sexo: '))
while  d !="f" and d !="m" :
	d =str(input('informe a inicial do seu sexo: '))

e = str(input('informe a inicial do seu estado civil: '))
while e != "s" and e != "c" and e != "v" and e != "d" :
	e = str(input('informe a inicial do seu estado civil: '))
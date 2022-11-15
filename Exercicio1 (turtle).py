import turtle

tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.speed(0)

x = int(input('Quantas linhas tera sua matriz quadrada? '))
y = int(input('Quantas colunas tera sua matriz quadrada? '))

for step in range(0, x):
  for step in range(0, y):
    for step in range(0, 4):
        tartaruga.forward(10)
        tartaruga.right(90)
    tartaruga.forward(10)
  
  tartaruga.back(y * 10)
  tartaruga.right(90)
  tartaruga.forward(10)
  tartaruga.left(90)
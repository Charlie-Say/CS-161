import turtle

turtle.pensize(1)
turtle.speed(0)
passi = 1
turtle.bgcolor('black')
turtle.color('red')

while True:

    for i in range(600):
        turtle.forward(passi)
        turtle.left(88)
        passi = passi + 1

    turtle.done()



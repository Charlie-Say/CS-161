import turtle
from random import randint

def water():
    turtle.hideturtle()
    turtle.fillcolor('blue')
    turtle.pencolor('blue')

    turtle.begin_fill()
    turtle.down()

    turtle.right(100)
    turtle.forward(20)
    turtle.circle(10,180)
    turtle.left(40)
    turtle.forward(35)
    
    turtle.end_fill()
    turtle.up()
    turtle.home()
    
 
water()

for i in range(20):

    xpos = randint(-230,40)
    ypos = randint(-130,-70)
    turtle.goto(xpos,ypos)
    water()



turtle.done()
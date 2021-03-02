import turtle

def cloud():

    turtle.bgcolor('sky blue')
    turtle.fillcolor('white')
    

    turtle.begin_fill()
    turtle.goto(50,0)

    turtle.circle(70,180)
    turtle.right(100)
    turtle.circle(60,150)
    turtle.right(90)
    turtle.circle(40,110)
    turtle.right(120)
    turtle.circle(50,120)
    turtle.right(100)
    turtle.circle(60,160)
    turtle.right(90)
    turtle.circle(50,170)
    turtle.right(110)
    turtle.circle(50,160)
    turtle.right(140)
    turtle.circle(70,150)
    turtle.forward(100)

    turtle.end_fill()
    turtle.up()

    turtle.done()
cloud()
import turtle


turtle.bgcolor('sky blue')
turtle.up()
turtle.goto(0,200)



def outline_head():
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()


    turtle.forward(50)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(15)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.backward(15)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)


    turtle.end_fill()

outline_head()

turtle.done()
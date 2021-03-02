'''
Draw clouds with random rain drops.

Ask the user for input to a riddle where the picture drawn is the answer.
Import turtle graphics to draw a cloud and randomly generated raindrops
whether the answer is correct or incorrect.

Charlie Say
Lab 1
January 16, 2019

ask for input(riddle)
create loop and condition of input
define cloud() - draw cloud
define rain() - draw rain
create a for loop for random rain drops

input: riddle
loops: rain(), input(riddle)
functions: cloud(), rain()
'''

import turtle
from random import randint

riddle = input("I can fly but I have no wings. I can cry but I have no eyes."
                " Wherever I go, darkness follows me. What am I? ")

while True:
   
    if(riddle != 'cloud'):
        print("Nope! Good try though! I'm a cloud!")
        break

    else:
        print("That's correct!")
        break

turtle.up()
turtle.setup(width = 900, height = 800, startx = 1000, starty = 100)

def cloud():
    '''function draws cloud'''

    turtle.speed(8)
    turtle.hideturtle()
    turtle.bgcolor('sky blue')
    turtle.fillcolor('white')
    turtle.pencolor('white')
    turtle.down()
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

    turtle.end_fill()
    turtle.up()
    turtle.home()

cloud()

turtle.goto(30,-50)

def rain():
    '''function draws rain'''

    turtle.speed(8)
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

rain()

for i in range(20):
    '''creates randomized raindrops'''

    turtle.up()
    turtle.home()
    xpos = randint(-270,60)
    ypos = randint(-260,-70)
    turtle.goto(xpos,ypos)
    rain()

turtle.done()
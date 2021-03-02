'''
use turtle graphics to draw multiple shapes and multiple colors.

Create a picture using random generated colors and prompting the user for the amount of shapes to be used. The shape will be squares being fanned out into a circular pattern in the middle of the window. Program must output a brief decription of what the program does. It will repeatedly prompt for the user unput until the user supplies values of the correct form. Prompt will say what form of input is needed.

Charlie Say
Lab 2
January 22, 2019

import turtle
import random

num = input("how many squares would you like to draw?")
    if num.isdigit():
        num_int = int(num)

def square(num):
    turtle.down()
    turtle.begin_fill()

    red = random.random()
    green = random.random()
    blue = random.random()

    turtle.color(red,green,blue)

    for i in range(4):
        turtle.forward(200)
        turtle.right(90)

    turtle.right(180 / num)
        
    turtle.end_fill()
    turtle.up()
square()

for i in range(num):
        square()
'''


import turtle
import random

print("This program draws the number of squares you input. It will then fill in the squares with a random color. The drawing will show all of the squares in a circular pattern according to how many squares you want.")

def main():
    '''
    ask for user input.
    check condition statements for errors
    define square
    '''
    num_squares = input("Enter an integer for how many squares you would like to draw? ")

    if num_squares == '0':
            print("You cannot draw zero squares. Nice try. Enter another integer please.")
            main()

    while True:

        if num_squares.isdigit():
            int_squares = int(num_squares)

        else:
            print("The input cannot be a string and at least the number 1. "
                "Please Try again.")
            main()

        def square():
            '''
            randomize color fill
            draw square
            '''
            turtle.speed(8)
            turtle.bgcolor("black")
            turtle.down()
            turtle.begin_fill()

            red = random.random()
            green = random.random()
            blue = random.random()

            turtle.color(red,green,blue)

            for sides in range(4):
                turtle.forward(100)
                turtle.right(90)

            turtle.right(360 / int_squares)

            turtle.end_fill()
            turtle.up()

        square()

        for i in range(int_squares - 1):
            square()


        turtle.done()
    

main()
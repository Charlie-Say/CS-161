'''
draw a checker board

Draw a game board for playing checkers. It is a grid of 8x8 squares, in which the square's colors alternate.

Charlie Say
Pito Libby
CS 161
10:00 AM

------ PSUEDO -----

import modules
windows settings

def first column:
    set points(x,y)
    name each point(p1, p2, p3, etc...)

    for loop to draw 4 columns:

        for loop to draw squares on y-axis:
            draw squares
            fill in colors

def second column:
    shift points equal to twice as much as the first column

    for loop to draw 4 columns:

        for loop to draw squares on y-axis:
            draw squares
            fill in colors
            # should be the opposite of first column

'''


from graphics import *

win = GraphWin('MF Checkers', 600, 600)

def first_col():
    x1, y1 = 30, 30
    x2, y2 = 70, 70

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    for r2 in range(4):
        x1 = x1 + 80
        x2 = x2 + 80

        for r in range(8):        # SQUARES IN COLUMNS
            p1 = Point(x1, y1 + 40*r)
            p2 = Point(x2, y2 + 40*r)

            rect = Rectangle(p1, p2)
            rect.draw(win)
            
            if r % 2 == 0:
                rect.setFill('black')
            else:
                rect.setFill('red')

def second_col():
    x1, y1 = 70, 30
    x2, y2 = 110, 70

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    for r2 in range(4):
        x1 = x1 + 80
        x2 = x2 + 80

        for r in range(8):        # SQUARES IN COLUMNS
            p1 = Point(x1, y1 + 40*r)
            p2 = Point(x2, y2 + 40*r)

            rect = Rectangle(p1, p2)
            rect.draw(win)
            
            if r % 2 == 0:
                rect.setFill('red')
            else:
                rect.setFill('black')

first_col()
second_col()

win.getMouse()
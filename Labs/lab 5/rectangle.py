#! /usr/bin/env python3
# # coding=utf-8

'''
 program that will display information about a rectangle drawn.

 The program will display information about a rectangle drawn by the user. The input will 
 be two mouse clicks for the opposite corners of a rectangle. Its output will draw the recangle and print the perimeter
 and area of the rectangle.

 Charlie Say
 Brandon Admire
 10:00 AM
 Lab

 ----- PSUEDO -----

 area = length * width
 perimeter = 2(length + width)

 create window
 prompt user for two clicks
 click one = first point
 click two = second point

 draw rectangle
    a = get(Point 1) (getY or getX)
    c = get(point 2)

absolute values
 width = (a - b)
 length = (b - c)
 perimeter = 2(width + length)


 output: area, perimeter


'''


from graphics import *
import math

win = GraphWin('rectangle', 400, 400)

print('Click two points in the window to draw a rectangle.')

win.setCoords(0, 0, 10, 10) 

click_1 = win.getMouse()
click_2 = win.getMouse()

rect = Rectangle(click_1, click_2)
rect.setFill('blue')
rect.draw(win)

length = abs(click_1.getX() - click_2.getX())
width = abs(click_1.getY() - click_2.getY())

perimeter = (length + width) * 2
area = length * width

message = Text(Point(5,1), f"Perimeter is {perimeter:.3} and area is {area:.3}.")
message.draw(win)

win.getMouse()
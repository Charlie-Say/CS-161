'''
program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically.

The program will take the input as an integer that will be the radius of the circle. It will then draw a circle given the radius. Another input will be taken in as an integer and that will be the y-intercept of a horizontal line. The program will then take the intersecting points of the line on the circle and give the x values textually above the graph.

Charlie Say
Pito Libby
CS 161
10:00 AM

--------- PSUEDO ----------

import modules
set coordinates of windows

input("Enter radius")
input("Enter y-intercept")

draw circle
draw line

calculate intersecting points(x = +/- sqrt(r**2 - y**2))

draw circles at the intersecting points

print text above graph

'''


from graphics import *
import math

# window settings
win = GraphWin('Intersecting Lines of a Given Circle', 600, 600)
win.setCoords(-10, -10, 10, 10)

given_radius = int(input("Enter a radius(1-10): "))
y_int = int(input("Enter the y-intercept(-10-10) of the line: "))

# draw circle
center = Point(0, 0)
circ = Circle(center, given_radius)
circ.draw(win)

# draw line
a_line = Line(Point(-10, y_int), Point(10, y_int))
a_line.draw(win)

intersect_a = (math.sqrt(given_radius**2 - y_int**2))
intersect_b = -(math.sqrt(given_radius**2 - y_int**2))

# draw points of intersections
circ_a = Circle(Point(intersect_a, y_int), .2)
circ_b = Circle(Point(intersect_b, y_int), .2)

circ_a.draw(win)
circ_a.setFill('red')
circ_b.draw(win)
circ_b.setFill('red')

message = Text(Point(0,9), f"The point of intersections are {intersect_a:.3} and {intersect_b:.3}.")

message.draw(win)


win.getMouse()
'''
This program will take 5 clicks on a window from a user to construct a house drawing.

This program will take 5 clicks on a window from a user to construct a house drawing.
The first two clicks will be the opposite sides of the main house. The third click will
be the center of the top edge of a rectangular door. The door will have a total width of 
1/5th of the width of the house frame. The fourth click will be the center of a square window,
with width of half the width of the door. The final click will indicate the peak of the
roof.

Brandon Admire
Charlie Sey

Pseudo Code
-----------
Draw window
Get click one
Get click two

House body = Draw rectangle using click one and two
Get height and width of house body
Get click three
draw door
get click four
draw window
Get click 5
draw roof.
wait for input to close window.
'''

from graphics import *

win = GraphWin("House", 800, 800)

click_1 = win.getMouse()
click_2 = win.getMouse()

house_body = Rectangle(click_1, click_2)
house_body.draw(win)

click_3 = win.getMouse()

house_body_width = abs(click_1.getX()-click_2.getX())
house_body_height = abs(click_1.getY()-click_2.getY())
door_width = house_body_width/5
# These calculate the position of the points for the door
# Point 1 is the top right of the door.
point_1 = Point(click_3.getX()+(door_width/2), click_3.getY())
# Point 2 is the bottom left of the door.
if click_1.getY() > click_2.getY():
    point_2 = Point((click_3.getX()-(door_width/2)), click_1.getY())
else:
    point_2 = Point((click_3.getX()-(door_width/2)), click_2.getY())

door = Rectangle(point_1, point_2)
door.draw(win)

click_4 = win.getMouse()

window_point_1 = Point(click_4.getX()+(door_width/2)/2,
                       click_4.getY()+(door_width/2)/2)
window_point_2 = Point(click_4.getX()-(door_width/2)/2,
                       click_4.getY()-(door_width/2)/2)

window = Rectangle(window_point_1, window_point_2)
window.draw(win)

click_5 = win.getMouse()

if click_1.getY() < click_2.getY():
    roof_point_one = Point(click_1.getX(),click_1.getY())
else:
    roof_point_one = Point(click_2.getX(),click_2.getY())

if click_1.getY() < click_2.getY():
    roof_point_two = Point(click_2.getX(),click_1.getY())
else:
    roof_point_two = Point(click_1.getX(),click_2.getY())

roof = Polygon(click_5, roof_point_one, roof_point_two)
roof.draw(win)

win.getMouse()

riddle = input("I beam, I shine, I sparkle white. I'll brighten the day with a single light."
            " I'll charm and enchant all. I'll bring the best in you all. What am I? ")

import turtle
t = turtle.Pen()
t.left(90)
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(90)
t.forward(115)
turtle.done()
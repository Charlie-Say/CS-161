'''
write a program using turtle graphics.
Mega-Man pixel drawing.
start with background of character. ask users simple questions.
'''

import turtle

def history():

    game_history = input("Do you know the story behind one of the"
                        "most iconic figures in video game history, Mega-Man? ")

    if(game_history == 'no'):
        print("Mega Man, known as Rockman in Japan, is a science fiction video game franchise created by Capcom, "
        "starring a series of robot characters each known by the moniker Mega Man. "
        "Mega Man, released for the Nintendo Entertainment System in 1987, was the first in a series of over 50 games on multiple systems. "
        "A roster of corrupted robot masters faced Mega Man in separate stages in the game. "
        "By March 2015, the series had sold about thirty million copies worldwide.")

    if(game_history == 'yes'):
        print("Well then. Enjoy this creative masterpiece. (:")

history()


def outline_head():
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()


    turtle.forward(100)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(100)


    turtle.end_fill()

outline_head()

turtle.done()







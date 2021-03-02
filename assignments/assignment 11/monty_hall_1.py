'''
Write a program to select random door as prize door and randomly select a
contestant door.

Charlie Say
Alex Nylund
CS 161 10:00AM

_____PSUEDO_____

import random
make door options as objects in list
track game counts
track win counts
for loop:
    prize door = random
    contestant = random

    if prize door == contestant door:
        win count + 1
        game count + 1

    else:
        game count + 1
'''


import random
from random import randint

doors = ['door1', 'door2', 'door3']
game_count = 0
win_count = 0

for i in range(100000):
    prize_door = random.choice(doors)
    contestant_door = random.choice(doors)
    
    if prize_door == contestant_door:
        game_count += 1
        win_count += 1
    
    else:
        game_count += 1

print(f'The contestant guessed {round((win_count/game_count)*100, 2)}% games correctly!')

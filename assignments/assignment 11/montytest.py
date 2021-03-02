import random
from random import randint

new_list = []
doors = ['door1', 'door2', 'door3']
game_count = 0
win_count = 0


for i in range(5):
    prize_door = random.choice(doors)
    contestant_door = random.choice(doors)
    new_list.append(contestant_door)

    if prize_door in doors:
        transfer_prize = doors.pop(prize_door)
        new_list.append(transfer_prize)

    elif prize_door not in doors:
        open_door = new_list.append(doors[0])


    if prize_door == contestant_door:
        game_count += 1
        win_count += 1

    else:
        game_count += 1

print(f'The contestant guessed {round((win_count/game_count)*100, 2)}% games correctly!')

'''
put random selected door in new list
if prize door in old list, open the other door
    put prize door in new list
if prize door not in old list, open a random door
    put the other door in new list
from new list, pick other door from selected door
'''


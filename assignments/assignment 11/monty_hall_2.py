'''
Write a program to select a door and always switch when prompted to choose again.

After selecting a door, but before the prize door is revealed, the contestant is shown
a losing door. The contestant now has the option of switching to the other, as-yet unopened
door. Always choose to switch to the other door and siplay the winning percentage after a
large number of simulation runs.

Charlie Say
Alex Nylund
CS 161 10:00AM

In conclusion, we found that by always switching on the second pick, it will increase
your odds of winning by twice as much. If the contestants first pick was initially
the prize door, then the contestant will automatically lose.

It makes logical sense that if you always switch doors on the second pick, you have
higher odds of winning. On your first pick, you have a 66% chance of picking the wrong
door. Most likely you will pick the wrong door, so when you switch once one of the wrong
doors is revealed, you will automatically win. Increasing your chances of winning up to
66%

__PSUEDO__
put random selected door in new list
if prize door == contestant door:
    lose
if prize_door != prize door:
    win
'''


import random

doors = ['door1', 'door2', 'door3']
game_count = 0
win_count = 0

for i in range(10000):
        prize_door = random.choice(doors)
        contestant_door = random.choice(doors)

        if prize_door == contestant_door:
            game_count += 1  # Automatically lose if this is the case

        else:
                win_count += 1  # Automatically win because it is opposite door
                game_count += 1  # of the contestant

print(f'The contestant guessed {round((win_count/game_count)*100, 2)}% games correctly!')


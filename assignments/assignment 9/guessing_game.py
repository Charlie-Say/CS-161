'''
Write a GUI program that asks the user to guess a random number between 1 and 100,
inclusive. The program should end when the user guesses correctly, but otherwise provides
hints in the form of a graphical arrow and text for guessing higher or lower.

Alex Nylund
Charlie Say
CS161 10:00am T/Th

make window
make entry box
input: guessing integer
if guess > int:
    too high
if guess < int:
    too low
'''

import random
import time
from tkinter import *
from tkinter import messagebox

random_number = random.randint(1,100)

window = Tk()
window.title('Guessing Game')
window.geometry('450x250')
heading = Label(window, text='CS 161 - Guessing Game \n'
                            'This program will generate a random number \n'
                            'See if you can guess it..')
heading.pack()

user_number = Entry(window,width=20)
user_number.pack()

def main():
    
    user_guess = int(user_number.get())
        
    if user_guess > random_number:
        print('You\'re guessing TOO HIGH')

    if user_guess < random_number:
        print('You\'re guessing TOO LOW')
        
    if user_guess == random_number:
        print(f'Your guess of {user_guess} was correct!')
        time.sleep(2)
        sys.exit()

btn_1 = Button(window, bd=5, text='Check Your Guess', command=main)
btn_1.pack()
window.mainloop()
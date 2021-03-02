'''
 write a GUI program that prompts for a credit card and determines if
 it could be valid.

 The program should print a message telling the user if it is or not,
 and in the case that it is, prints the name of the brand and its logo.
 the card brand cannot be determined but the number appears to be
 valid the program should output "Unknown Card."

 Charlie
 Say
 CS 161
 10:00 AM

 ____PSUEDO____________________
 import tkinter
 open window with a text box

 int(input: int(16 digit))
 list_numbers = list(input)
 credit_list.split()

 card number == 16
    if not: print invalid card number, try again

    for i in range(len(0, 16, 2)):
         list_numbers = list[i] * 2

         if len([i]) >= 2:
             split_nums = [i].split()
             total_nums = split_nums[0] + split_nums[1]

    for i in range(len(list_numbers):
        sum_list = sum(list_numbers)

    if sum_list % 10 == 0:
        print(valid)
        print card brand and logo
        starts with 3: American Express
        starts with 4: Visa
        Starts with 5: MasterCard
        starts with 6: Discover

    else:
        print(invalid)

'''

from tkinter import *
from tkinter import messagebox
import PIL
from PIL import ImageTk, Image

window = Tk()
window.title("Credit Card Validation")
window.geometry('450x250')

heading = Label(window, text="CS 161 - Credit Card \n This program will \n"
                            "take in a 16 digit integer and check if \n"
                            "the digit is a valid credit card number \n"
                            "and then print out the card name and logo \n")

heading.pack()

card_number = Entry(window,width=20)
card_number.pack()

def main():
    '''
    this will test the card number and see if it is valid.
    it will turn the input into an integer, multiply every
    second integer by 2. for all integers that total over 9,
    the program will split the integers and add them.
    add all the integers in the list together and mod 10 to
    check if it's a valid credit card.
    '''

    card_str = card_number.get()
    card_list = [int(i) for i in str(card_str)]
    print(card_list)

    for i in range(1, len(card_list), 2):
        card_list[i] = card_list[i] * 2
        
    str_list = [str(card_list[x]) for x in range(len(card_list))]
    print(str_list)

    for i in range(len(str_list)):
        
        if len(str_list[i]) >= 2:
            split_int = [int(i) for i in (str_list[i])]
            sum_int = sum(split_int)
            str_list[i] = (sum_int)

    card_list = [int(i) for i in (str_list)]

    mod_ten = sum(card_list) % 10
    print(mod_ten)
    if mod_ten != 0:
        heading = Label(window, text="INVALID CARD")
        heading.pack()
        
    else:
        heading = Label(window, text="VALID CARD")
        heading.pack()

        name_logo(card_list)



def name_logo(card_list):
        '''
        starts with 3: American Express
        starts with 4: Visa
        Starts with 5: MasterCard
        starts with 6: Discover
        '''
        name_of_bank = ['American Express', 'Visa', 'MasterCard', 'Discover']
        img_list = ['americanexpress.png', 'visa.png', 'mastercard.png', 'discover.png']
        display = Toplevel()
        
        if card_list[0] == 3:
            display.geometry('450x250')
            display.title(name_of_bank[0])
            image = PhotoImage(file=img_list[0])
            w = Label(display, image=image)
            w.pack()
            display.mainloop()
            
        elif card_list[0] == 4:
            display.geometry('450x250')
            display.title(name_of_bank[1])
            image = PhotoImage(file=img_list[1])
            w = Label(display, image=image) 
            w.pack()
            display.mainloop()

        elif card_list[0] == 5:
            display.geometry('450x250')
            display.title(name_of_bank[2])
            image = PhotoImage(file=img_list[2])
            w = Label(display, image=image)
            w.pack()
            display.mainloop()

        elif card_list[0] == 6:
            display.geometry('450x250')
            display.title(name_of_bank[3])
            image = PhotoImage(file=img_list[3])
            w = Label(display, image=image)
            w.pack()
            display.mainloop()

        else:
            display.geometry('450x250')
            display.title("Unknown Card")
            
            w = Label(display, text="UNKNOWN CARD")
            w.pack()
            display.mainloop()

Label(window, text="Enter a 16 digit number \n").pack()
btn_1 = Button(window, bd=5, text="Check Validation", command=main) #command=name_logo)
btn_1.pack()

window.mainloop()
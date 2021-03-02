#! /usr/bin/env python3 
# coding=utf-8

'''
create a Caesar cipher based on the idea of shifting each letter of the text
message a fixed number.

Write a program that will take a text file and shift the letters of the file to
the amount prompted from the user. The program will reverse backwards if prompted
with a negative number. The cipher will handle the shifts in the text in a circular
fashion where the next character after "z" is "a". The program will open A GUI
that will allow the user to select a text file containing plaintext using a File
Dialong. The program should then encrypt the text and write the ciphertext out
to a new file also specified by the user using a Save Dialog.

Charlie Say
Alex Nylund
10:00 AM
Assignment 5

---- PSUEDO ----

GUI: select plaintextfile
input: enter key of positions in the alphabet

open text file
read/write text file
shift letters in file given the key position

def keyloop():
    loop the alphabet used if key rotates at the end of "z"

GUI: save text file

HINTS:  pythons builtin ord() and char()
        GUI program uses graphics.py library
'''

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


def initiate_encrypt():
    # button to encrypt file for user provided key
    infilename = askopenfilename()
    open_file = open(infilename, "r")
    read_file = open_file.read()
    text_box_input = int(key_text.get())
    
    outfilename = asksaveasfilename()
    write_file = open(outfilename, "w")
    smol_list = list(read_file)


    for i in range(len(smol_list)):

        smol_list[i] = ord(smol_list[i])

        if 65 <= smol_list[i] <= 90:
            if (smol_list[i] + text_box_input) <= 90:
                smol_list[i] = smol_list[i] + text_box_input
            elif (smol_list[i] + text_box_input) >= 90:
                smol_list[i] = 65 + ((smol_list[i] + text_box_input) - 90)

        elif 97 <= smol_list[i] <= 122:
            if (smol_list[i] + text_box_input) < 122:
                smol_list[i] = smol_list[i] + text_box_input
            elif (smol_list[i] + text_box_input) > 122:
                smol_list[i] = 97 + ((smol_list[i] + text_box_input) - 122)

    for number in range(len(smol_list)):
           smol_list[number] = chr(smol_list[number])

    print(''.join(smol_list), file=write_file)
    
    open_file.close()
    write_file.close()


window = Tk()
window.title("Hail Caesar")
window.geometry('450x250')

heading = Label(window, text="CS 161 - Caesar Cypher \n \n This program will"
                            "take in a text and shift the characters \n"
                            "in the document according to the key. \n"
                            "You will be prompted to open the file and then \n"
                            "save the file. \n")
heading.pack()

key_text = Entry(window,width=10)
key_text.pack()

Label(window, text="Enter a Key \n \n").pack()
btn_1 = Button(window, bd=5, text="Initiate Program", command=initiate_encrypt)
btn_1.pack()



window.mainloop()
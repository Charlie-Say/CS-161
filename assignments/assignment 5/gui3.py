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



# opening the file
infilename = askopenfilename()
open_file = open(infilename, "r")
read_file = open_file.read()
outfilename = asksaveasfilename()
write_file = open(outfilename, "w")

key_cypher = int(input("Enter a key: "))

smol_list = list(read_file)

for i in range(len(smol_list)):
    smol_list[i] = ord(smol_list[i]) + key_cypher


for i in range(len(smol_list)):
    smol_list[i]


print(smol_list, file=write_file)
#print(''.join(smol_list), file=write_file)
open_file.close()
write_file.close()
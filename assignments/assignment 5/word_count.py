#! /usr/bin/env python3 
# coding=utf-8

'''
write a program that can report the number of times a certain
word appears in a file.

Prompt the user for the file name and the word to search for and display the 
number of times the word appears in the file. Use the getopt module to allow the user
to provide the name of a text file, preceded by a -f flag, and the word to be counted,
preceded by a -w flag at the command line.

Charlie Say
Alex Nylund
10:00 AM
Assignment 5

---- PSUEDO ----

input: file name
input: prompt word to count

open the text file
search the file for the input(word)
count(word) in text file

output: number of times word appears in file
'''

import getopt
import sys

infile = ''
word = ''

print("The syntax to open the file and choose a word is: 'python pythonfile.py -f textfile.txt -w chooseword'")
try:
    
    options, args = getopt.getopt(sys.argv[1:], "f:w:")

except getopt.GetoptError:
    print('Something isn\'t right!')
    sys.exit(2)

# opt == option
# arg == argument passed to the opt

for opt, arg in options:

    if opt == '-f':
        infile = arg
        fname = infile
        open_file = open(fname, "r")
        data = open_file.read()
        print(data)

    elif opt == "-w":
        word = arg
        str_list = data.split()
        
        count = 0
        for i in str_list:
            if i == word:
                count += 1

        print(f"The number of occurences of the word {word} in the file is {count}.")
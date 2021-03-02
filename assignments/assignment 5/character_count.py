#! /usr/bin/env python3 
# coding=utf-8

'''
write a program that can count the number of times a certain letter appears in a string

Prompt the user for the string and the letter to search for and display the number of 
times that letter appears.

Charlie Say
Alex Nylund
10:00 AM
Assignment 5

---- PSUEDO ----

input: string
input: prompt letter to search

search string index for input(letter)
keep count of each appearance of a character

output: number of times letter appears
'''


def main():
    user_string , target_letter = input('Please enter a string: ') , input('Please enter a letter to count: ')
    occurence = 0

    for i in range(len(user_string)):
        if user_string[i] == target_letter:
            occurence += 1
    print(f"That letter occurs {occurence} times")
        

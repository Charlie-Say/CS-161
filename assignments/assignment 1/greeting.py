'''
Write a program that prompts for the user's first name and stores it in a variable.
Do the same for the last name. Then, use string concatenation to greet them with their full name.

Charlie Say
Program Assignment 1
January 16, 2019

prompt users for input. first name and last name.
create variables for first and last name.
concatenate the two variables in one string.
print a greeting and full name.

inputs: first name, last name
variables: first_name, last_name
'''


first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print("Hello, {0} {1}!".format(first_name, last_name))
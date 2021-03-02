'''
 write a program that accepts a comma separated sequence of words as input and prints the unique words sorted alphabetically.

 sample words: red, white, black, red, green....

 problem_4
'''

# TRY
uni_list = input("Enter words: ").split(',')

set_list = set(uni_list)
sort_set = sorted(set_list)

print(set_list)
print(sort_set)


# SOLUTION
user_input = input("Please enter some words separated by commas: ")

list_of_words = [word for word.strip in user_input.split(',')]

print(list_of_words)

'''
problem 1
using len() will count the strint/input
'''

count = 0
string = 'cheese'


for i in range(len(string):
    count += count + 1
    print(count)


answer:

print(len(string)) ### simple




'''
problem 2
wrie a python program that prints the ASCII values of all the alphanumeric characters in a user-provided string
'''

answer:

user_input = input("enter: ")

for character in user_input:
    print(f"{character} = {ord(character):3}")
    

'''
problem 3
write program to print a string provided by the user in reverse order using string slicing.
'''

answer:


user_input = input("Enter: ")

print(user_input[::-1])



'''
problem 4
write a program to get a string from the user and produce a new string where all occurrences of its first char have been changed to '$', except the first char itself.
sample string: 'sleeplessness'
Expected result: 'sleeple$$ne$$'
'''

user_input = input("Enter: ")

for character in range(user_input):
    if character == user_input[0]:
        character = '$'
        
    print(user_input)
    

answer:

user_input = input("Enter: ")

first_character = user_input[0]
rest_of_string = user_input[1:]
string_with_replacement = rest_of_string.replace(first_character, '$')


new_string = user_input[0] + user_input[1:].replace(user_input[0], '$')

print(user_input)
print(new_string)
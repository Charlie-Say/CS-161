'''
problem 2
wrie a python program that prints the ASCII values of all the alphanumeric characters in a user-provided string
'''

# try

cheese = input("Enter: ")
print(ascii(cheese))


# answer

user_input = input("enter: ")

for character in user_input:
    print(f"{character} = {ord(character):3}")
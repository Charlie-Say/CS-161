'''
 write a python program to convert a list of characters into a string

 problem_2
'''

# TRY
char_list = ["a", "b", "c", "d"]

print(''.join(char_list))

num_list = [1, 2, 3, 4]

str_num = str(''.join(str(num) for num in num_list))

print(str_num)

# SOLUTION
import random
import string

letters = ["a", "b", "c", "d"]

my_string = ''.join(random.choic(string.ascii_letters) for _ in range(15))

print(my_string)
print(type(my_string))
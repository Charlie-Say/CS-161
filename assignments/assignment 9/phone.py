'''
 program that prompts for a phone number and determines if its a valid number.
 
 Write a program that prompts for a phone number and determines if its a valid
 number. It will only accept 10-digit numbers and ignore punctuations.
 If a number is not equal to 10 or if no number is given, the program will
 prompt for one.

 Charlie Say
 Alex Nylund
 CS 161
 10:00 AM

 ____PSUEDO_____
 
 while loop:
     input: phone number
     remove punctuations
     if statement:
         if number != 10:
             print('invalid')
         else:
             print('valid')
             break
'''


def phone_number():

    while True:

        phone_num = input("Enter a phone number: ")
        remove_punc = ''.join(i for i in phone_num if i not in '()-')
        remove_len = len(remove_punc)

        if phone_num == '':
            print("Please enter a phone number.")

        elif remove_len != 10:
            print("Invalid phone number. Try again!")

        else:
            print(f"{phone_num} is a Valid phone number")
            break

if __name__ == '__main__': phone_number()
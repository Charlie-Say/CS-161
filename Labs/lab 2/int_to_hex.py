'''
write program that takes an integer and converts it to hexadecimal and back again

Prompt the user for an integer and then convert the integer into a hexadecimal and back again. Hexadecimal is in base 16. It also includes letters A, B, C, D, E, F. The number 10 in decimal and binary equals the letter A, 11 is B, 12 is C, etc. 

Charlie Say
Lab 2
January 22, 2019

rem_list = []
hexlist= []

input("enter an integer")

if input == o:
    print invalid hexadecimal

elif input <= 0:
    print invalid for negative integer

else:
    while num != 0:
        divide integer by 16 until zero
        store remainder into into list
        convert numbers 10-15 into A-F
        convert the list into a string
        join string
    
    rem_list.reverse()
    print()

    int_to_hex = 0

    for pos in hexlist:
        do stuff to convert back into integer
        use formula/calculation

        convert remainders into hexadecimal according to position in list
        print hexadecimal

for i in range(hexlist):
    hexa = hexa + (hexlist[pos] * (16 ** [pos]))
'''


remlist = []
hexlist = []


def main():
    '''
    make the condition statements.
    appending remainders into the list and converting them into a string.
    convert numbers 10-15 into letters.
    join the list.
    '''
    while True:
        try:
            num = int(input("Enter an integer: "))

        except ValueError:
            print("Cannot use strings. Try again")
            main()

        if num == 0:
            print("Zero in hexadecimal is = 0. Enter another integer.")
            main()

        elif num < 0:
            print("Cannot convert negative into hexadecimal. Try again.")
            main()

        else:
            while num != 0:

                rem = str(num % 16)
                num = num // 16
                remlist.append(rem)
                hexlist.append(rem)

            remlist.reverse()

            for pos in range(len(remlist)):

                if remlist[pos] == '10':
                    remlist[pos] = 'A'

                if remlist[pos] == '11':
                    remlist[pos] = 'B'

                if remlist[pos] == '12':
                    remlist[pos] = 'C'

                if remlist[pos] == '13':
                    remlist[pos] = 'D'

                if remlist[pos] == '14':
                    remlist[pos] = 'E'

                if remlist[pos] == '15':
                    remlist[pos] = 'F'

            print("You're integer in Hexadecimal is: ", ''.join(remlist))
            break


main()

# converting back into integer
hexa = 0
hexlist = list(map(int, hexlist))

for pos in range(len(hexlist)):
    hexa = hexa + (hexlist[pos] * (16 ** pos))


print("Hexidecimal {0} into an integer is : {1}".format(remlist, hexa))
print("I printed out the hexidecimal list to let you know that I didn't simply print out the input.")

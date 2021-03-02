'''
conversions from integer to binary and then from binary back to integer.

Prompt the user for an integer, convert the integer to a binary number string. Take the string and and convert it back into a regular integer. The program should be able to take in both integers and binary. Regardless of input, either integer or binary, the output should be the same as the input.

Charlie Say
Lab 2
January 22, 2019


list = []
input("enter an integer or binary number")

if statement == 0:
    print invalid

if statement < 0:
    print invalid

else:
    calculate into bin
    append remainders into array
    reverse the array
    
for loop that will take placement of list and convert numbers in list to (2 ** position of list)

print binary conversion of the integer

'''


def dectobin():
    '''
    this function will create a list and ask for inputs.
    it will also set the conditions of the input.
    it will convert the input into a binary string in the array.
    '''

    remlist = []

    while True:
        try:
            num = int(input("Enter an integer: "))
            
        except ValueError:
            print("Cannot use strings. Try again")
            dectobin()
    
        # conditional statements
        # reloop if check fails
        if num == 0:
            print("Zero in binary is = 0")
            dectobin()

        elif num < 0:
            print("Cannot convert negative into binary. Try again")
            dectobin()

        else:
            while num != 0:
                rem = int(num % 2)
                num = int(num // 2)
                
                remlist.append(rem)
            # reverse the list and print into a binary string
            remlist.reverse()
            print("Your integer into binary is: ", ''.join(str(x) for x in remlist))

            remlist.reverse()
            bin_to_int = 0
            # convert every element of the array back into an integer
            for pos in range(len(remlist)):

                if remlist[pos] == 1:

                    bin_to_int = bin_to_int + (2 ** pos)

            remlist.reverse()
            remlist = str(remlist)
            print("Binary conversion of {} is: {}".format(remlist, bin_to_int))
            print("I printed out the binary list to let you know that I didn't simply print out the input.")

            dectobin()

    
dectobin()
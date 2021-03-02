'''
make a program that will take input word and print out a new word using the syllable input from user.

Make a program that will take user input and convert it into a gibberish word. The program will take a word from the user and multiple syllables, then throw it into the word everytime a vowel occurs. The first syllable will be added to the first vowel, but not the second vowel if two vowels are placed together. The first input syllable will only add to the first vowel and the second syllable will be added to the rest of the vowels in the word. The '*' input will copy the vowel in front of the syllable and place it in the front of the syllable. At the end of the program, it will prompt the user if they would like to play again.

Charlie Say
Alex Nylund
CS 161
10:00 AM
January 30, 2019

input: word
input: syllable
input: syllable 2
vowels = 'aeiouAEIOU'

for range (word):
    if second vowel in a row
    continue

    if index of syllable input is '*':
        wild = syllable index
        list[i] = list[i] + syllable[1] + wild
        set flag

        else:
            list[i] = syllable + list[i]

    join(list)
    print(string or word)
'''

def main():
    '''
    main function that will make the user_input into a list.
    then it will place the syllable next to the vowels.
    also set flags for user to use '*'
    '''
    eng_word = input('Please enter a word: ')
    eng_list = list(eng_word)
    gibberish_syl = input("Enter syllable: ")
    gibberish_syl_2 = input("Enter second syllable: ")
    vowels = ('aeiouAEIOU')
    is_first = True

    for i in range(len(eng_word)):
        #this loop searches the word for vowels, and inserts the gibberish syllable into the english list, at the appropriate index.
        if eng_word[i -1] in vowels:
            # Don't print if it's the second vowel in a row
            continue
        if eng_word[i] in vowels:
            # Testing if the wildcard flag is set
            if gibberish_syl[0] == '*':
                wild = eng_list[i]
                eng_list[i] = eng_list[i] + gibberish_syl[1:] + wild
        
            else:
                if is_first == True:
                    # Inserts first syllable if it's the first vowel in the string
                    eng_list[i] = (gibberish_syl + eng_list[i])
                    is_first = False
                
                else:
                    eng_list[i] = (gibberish_syl_2 + eng_list[i])

    eng_str = ''.join(eng_list)
    print(eng_str) 

    play_again = input("Play again? (y/n): ")
    if play_again == 'y' or 'yes':
        main()

    else:
        print("Have a nice!")

main()



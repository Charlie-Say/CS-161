''' 
This program evaluates how many scrabble scores a point is worth. 

It takes a word as an input, forces it to be lowercase, and scores it as its 
ord() value minus 97. The program will loop until the user enters 'quit.'.

Assignment 9
Alex Nylund
Charlie Say
CS161 10:00am T/Th

input: what your word?
loop through word and give value of letter
add values and print total
'''


while True:
    scrabble_word = input("What\'s your scrabble word? Enter \'quit.\' to quit"
        ": ")
        
    if scrabble_word == 'quit.':
        break
    
    else:
        lowercase_word = scrabble_word.lower()
        word_score = 0

        for i in range(len(scrabble_word)):
            word_score += (ord(lowercase_word[i]) - 97)

        print(f'Your word is worth {word_score} points')

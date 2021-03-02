eng_word = input('Please enter a word: ')
eng_list = list(eng_word)
gibberish_syl = input("Enter a syllable: ")
vowels = ('aeiouAEIOU')

for i in range(len(eng_word)):
    ''' this loop searches the word for vowels, and inserts the gibberish
        syllable into the english list, at the appropriate index. '''
    if eng_word[i] in vowels:
        eng_list[i] = (gibberish_syl + eng_list[i])
eng_str = ''.join(eng_list)
print(eng_str)   

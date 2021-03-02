'''
 problem 1
 function that prompts number of words one word at a time.
 output = longest word provided
 
'''

# TRY

word_list = []

longest = 

while True:

    word = input("Enter a word: ")

    word_list.append(word)

    if word == '':
        break

for word in word_list:

    longerstint(len(word))

print(word_list)


# DEMO

def main():
    max_length = 0
    while True:
        word = input("Enter word:")
        word_length = len(word)
        if word_length = 0:
            break
        if word_length > max_length:
            max_length = word_length
            # max_length = max(word_length, max_length)
        print(f"The longest word you entered had {max_length} characters.")


if __name__ == "__main__":
    main()
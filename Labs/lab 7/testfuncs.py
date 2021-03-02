import math
import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
    "*": 0,
}

# inFile = open("words.txt", "r")
# # wordlist: list of strings
# wordlist = []
# for line in inFile:
#     wordlist.append(line.strip().lower())


# def is_valid_word(word, hand, word_list):

#     for i in range(len(word)):
#         if word[i] in hand:
#             if word[i] == '*':
#                 if (f'{word[:i]}' + 'a' + f'{word[i + 1:]}') in word_list:
#                     new_word = (f'{word[:i]}' + 'a' + f'{word[i + 1:]}')
#                 elif (f'{word[:i]}' + 'e' + f'{word[i + 1:]}') in word_list:
#                     new_word = (f'{word[:i]}' + 'e' + f'{word[i + 1:]}')
#                 elif (f'{word[:i]}' + 'i' + f'{word[i + 1:]}') in word_list:
#                     new_word = (f'{word[:i]}' + 'i' + f'{word[i + 1:]}')
#                 elif (f'{word[:i]}' + 'o' + f'{word[i + 1:]}') in word_list:
#                     new_word = (f'{word[:i]}' + 'o' + f'{word[i + 1:]}')
#                 elif (f'{word[:i]}' + 'u' + f'{word[i + 1:]}') in word_list:
#                     new_word = (f'{word[:i]}' + 'u' + f'{word[i + 1:]}')
#                 else:
#                     return False
#             word_in_hand = True
#         else:
#             return False
#     if word_in_hand == True:
#         if word or new_word in word_list:
#             return True
#         else:
#             return False

# testing = is_valid_word('bon*r', {'b':1, 'o':1, 'n':1, 'e':1, 'r':1, '*':0}, wordlist)
# print(testing)

def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = len(hand)
    return handlen

testing = calculate_handlen({'b':1, 'o':1, 'n':1, 'e':1, 'r':1, '*':0})
print(testing)
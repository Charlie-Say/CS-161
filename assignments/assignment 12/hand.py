#! /usr/bin/env python3
# # coding=utf-8 
'''
create a hand class that acts as a container for some number of cards.

The number of cards in a Hand is specified as an argument to the Hand's __init__ method.
A Hand should always sort and store its cards in ascending order. The Hand class
should implement a __str__ magic method as well as the foloowing additional methods:
is_royal_flush, is_four_of_a_kind, is_full_house.

Charlie Say
Alex Nylund
CS 161 10:00 AM

____PSEUDO____
draw the amount of cards by size
while i < size:
    pop a card from the deck
    append to hand list

royal flush:
    split the hand
    append the 2nd element
    make the hand a set
    check if it has 1 unique element

    go through hand and make sure values >=10
    make hand into set, if length == 4: return true
    else: return false

four of a kind:
    check hand for same numbers
    if len of the list of same numbers == 3:
        return true
    else: return false

full house:
    make a list of same numbers as first element
    make list of same numbers from last element
    if len first list == 3
    and
    len second list == 2:
    return true
    else: return false
'''


import deck
import random
from random import randint



class Hand:


    def __init__(self, deck, size=5):
        self.cardlist = {'2 of Spades':2, '3 of Spades':3, '4 of Spades':4, '5 of Spades':5, '6 of Spades':6, '7 of Spades':7,
                        '8 of Spades':8, '9 of Spades':9, '10 of Spades':10, 'jack of Spades':11, 'queen of Spades':12, 'king of Spades':13, 
                        'ace of Spades':14, '2 of Diamonds':2, '3 of Diamonds':3, '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6, 
                        '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9, '10 of Diamonds':10, 'jack of Diamonds':11, 'queen of Diamonds':12, 
                        'king of Diamonds':13, 'ace of Diamonds':14, '2 of Clubs':2, '3 of Clubs':3, '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6, 
                        '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9, '10 of Clubs':10, 'jack of Clubs':11, 'queen of Clubs':12, 'king of Clubs':13, 
                        'ace of Clubs':14, '2 of Hearts':2, '3 of Hearts':3, '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6, '7 of Hearts':7, 
                        '8 of Hearts':8, '9 of Hearts':9, '10 of Hearts':10, 'jack of Hearts':11, 'queen of Hearts':12, 'king of Hearts':13, 
                        'ace of Hearts':14}
        self.hand = []

        for i in range(size):
            draw = random.choice(list(self.cardlist.keys()))
            self.hand.append(draw)
        self.hand.sort()


    def __str__(self):
        for i in range(len(self.hand)):
            self.hand[i] = str(self.hand[i])
        self.hand.sort()
        return str(self.hand)
    

    def is_royal_flush(self, some_hand):
        self.ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
                       '10':10, 'jack':11, 'queen':12, 'king':13, 'ace':14}
        self.flush = []
        self.straight = []
        self.new_hand = [i.lower() for i in some_hand]

        for i in self.new_hand:
            splitting = i.split()
            self.flush.append(splitting[2])

            get_val = splitting[0]
            act_val = self.ranks[get_val]
            self.straight.append(act_val)

        for i in self.straight:
            if i >= 10:
                continue
            else:
                return False

        if len(set(self.straight)) == 4:
            pass
            
        elif len(set(self.flush)) == 1:
            return True
        else:
            return False

    def is_four_of_a_kind(self, some_hand):
        same_nums = [i for i in self.straight if i is self.straight[0]]
        if len(same_nums) == 3:
            return True
        else:
            return False

    def is_full_house(self, some_hand):
        first_num = [i for i in self.straight if i is self.straight[0]]
        second_num = [i for i in self.straight if i is self.straight[-1]]

        if len(first_num) == 3 and len(second_num) == 2:
            return True
        else:
            return False



deck_me = deck.Deck()
test = Hand(deck_me, size=5)
print(test)

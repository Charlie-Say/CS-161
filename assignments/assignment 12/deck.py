#! /usr/bin/env python3
# # coding=utf-8 
'''
create a Deck class. Each Deck will contain the 52 cards found in a standard
deck. A __str__ method that lists all the cards currently in the deck in order
and a shuffle method that randomized the Deck. The __init__ method should take a
Boolean parameter, Jokers.

Charlie Say
Alex Nylund
CS 161 10:00 AM

____PSEUDO___
def class
def __init__:
    suit list
    rank list
    create new list with for loops
def __str__:
    turn the elements into string objects

def shuffle:
    shuffle deck
'''


import card
import random


class Deck:


    def __init__(self, jokers=False):
        self.cardlist = []
        self.suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        self.ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
                      '10':10, 'jack':11, 'queen':12, 'king':13, 'ace':14}
        # self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
        #             '10', 'jack', 'queen', 'king', 'ace']

        for suit in self.suits:
            for rank in self.ranks.keys():
                self.cardlist.append(card.Card(suit, rank))
                to_print = card.Card(suit, rank)
                print(to_print)

    def __str__(self):
        for i in range(len(self.cardlist)):
            self.cardlist[i] = str(self.cardlist[i])
        return str(self.cardlist)



    def shuffle(self):
        random.shuffle(self.cardlist)


# test = Deck()
# print(test)




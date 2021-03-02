import random
from random import randint
import card
import deck

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rank + " of " + self.suit)

    def __eq__(self, other):
       return (self.rank == other.rank)
    
    def __ne__(self, other):
        return (self.rank != other.rank)

    def __lt__(self, other):
        return (self.rank < other.rank)

    def __gt__(self, other):
        return (self.rank > other.rank)

    def __le__(self, other):
        return (self.rank <= other.rank)

    def __ge__(self, other):
        return (self.rank >= other.rank)


class Deck:

    def __init__(self, jokers=False):
        self.cardlist = []
        self.suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        self.ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
                    '10':10, 'jack':11, 'queen':12, 'king':13, 'ace':14}
        for suit in self.suits:
            for rank in self.ranks.keys():
                self.cardlist.append((Card(suit, rank)))
                
    def __str__(self):
        for i in range(len(self.cardlist)):
            self.cardlist[i] = str(self.cardlist[i])
        return str(self.cardlist)




class Hand:

    def __init__(self, size=5):
        self.hand = []

        i = 0
        while i < size:
            rand_int = random.randint(1, 52)
            deck_me = deck.Deck()
            draw = self.cardlist.pop(rand_int)
            self.hand.append(draw)
            i = i + 1

    
    def __str__(self):
        for i in range(len(self.hand)):
            self.hand[i] = str(self.hand[i])
        return str(self.hand)



print(Deck())
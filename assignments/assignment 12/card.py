#! /usr/bin/env python3
# # coding=utf-8 
'''
create a card class that represents a single card from
a standard deck. each card should know its suit.

Charlie Say
Alex Nylund
CS 161 10:00 AM

_____PSEUDO_____
define class
def __init__
def __str__
def __eq__
def __ne__
def __lt__
def __gt__
def __le__
def __ge__

'''


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (str(self.rank) + " of " + self.suit)

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


# test = Card('diamond', 7)
# print(test)
#! /usr/bin/env python3
# # coding=utf-8 
'''
Implement a Game class that instantiates an instance of a Deck
and a Hand with five cards. Game class should implement a new_deal
method, which returns all the cards in play to the Deck, shuffles it
and deals a new hand.

Charlie Say
Alex Nylund
CS 161 10:00 AM

___PSEUDO___
We tried. We attempted and put in around +20hrs.
We code bad, and it feels bad. Man.
Python Classes: Another one of life's unsolved mysteries. 
'''


import random
import deck
import hand
from random import randint

class Game:

    def __init__(self, jokers=False):
        self.dek = deck.Deck()
        self.hand_job = hand.Hand()
        
    def new_deal(self):
        self.newdek = deck.Deck()
        self.dek = self.newdek
        self.newhand_job = hand.Hand()
        self.hand_job = self.newhand_job

    def __str__(self):
        for i in self.hand:
            self.hand[i] = str(self.hand[i])
        return self.hand
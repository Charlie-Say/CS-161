#! /usr/bin/env python3
# # coding=utf-8 
'''
We tried. Have mercy on our souls.

Charlie Say
Alex Nylund
CS 161 10:00 AM

____PSEUDO___
def class
for loop:
    if royal flush
    if four of a kind
    if full house
'''


import game
import hand
import deck


class Simulation:

    def __init__(self):
        self.our_hand = hand.Hand(deck.Deck())
        self.count = 0 
        n = 10000000

        for i in range(0, n):
            
            self.type_hand = input("What type of hand? ")
            
            if self.type_hand == 'royal flush':
                if hand.is_royal_flush(self.our_hand) == True:
                    self.count += 1

            if self.type_hand == 'four of a kind':
                if hand.is_four_of_a_kind(self.our_hand) == True:
                    self.count += 1 
                
            if self.type_hand == 'full house':
                if hand.is_full_house(self.our_hand) == True:
                    self.count += 1

        
    def __str__(self):
        percentage = (self.count/n) * 100
        return print("This is your percentage:", percentage)

Simulation()
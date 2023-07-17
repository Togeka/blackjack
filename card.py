from pyrsistent import v
import numpy as np
import random


class Card():
    def __init__(self, suit, val, name):
        self.suit = suit
        self.name = name
        self.val = val

    def show(self):
        #prints 'ace of spaces'
        #future iterations would be cool to have a pixel image of the card 
       print(f'{self.val} of {self.suit}') 


class Deck:
    def __init__(self, num_decks=None) -> None:
        self.cards = []
        self.face_cards = ['King','Queen','Jack']
        self.num_decks = num_decks
        self.build() #want to build it straight in the init

    def build(self):
        for _ in range(self.num_decks):
            for suit in ['spades','hearts','diamonds','clubs']:
                self.cards.append(Card(suit,11,'Ace')) #add the cards to the deck #GOING TO NEED TO INCLUDE LOGIC FOR 1 OR 11
                for i in range(2,14):
                    if i > 10:
                        self.cards.append(Card(suit,10,self.face_cards[i-11]))#gives K,Q,J
                    else:
                        self.cards.append(Card(suit,i, i)) #add the cards to the deck

    def show(self):
        for c in self.cards:
            c.show() #show method from card class

    def full_shuffle(self):
        random.shuffle(self.cards) #full random shuffle of all our cards


if __name__ == '__main__':
    print('here')
    deck = Deck(1)
    deck.full_shuffle()
    deck.show()


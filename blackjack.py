import pandas as pd
import numpy as np

from card import Card, Deck


#goal of this file:
'''
Create a practice tester that can simulate blackjack hands and help me practice perfect strategy 
'''




class BlackJack():
    def __init__(self, shuffle_type='continuous', money=0, buy_in=False):
        self.correct_hands = 0
        self.total_hands = 0
        self.money = money
        self.buy_in = buy_in
        self.dealer_hand = []
        self.player_hand = []

        self.cards = Deck(num_decks=6) #builds the deck automatically 
        self.cards.full_shuffle()

        if shuffle_type == 'cut':
            self.shuffle_threshold = .75 #you've gone through 75% of the shoe
        else:
            self.shuffle_threshold = 0 #every card is 100% random


    def deal_cards(self):
        seen_cards = []
        seen_cards.append(self.cards.pop(0)) #pop the top card in the deck


   


    def play_hand(self, correct=True):
        '''
        function to play hand 

        prints out gives you the dealers card and prints out what your two cards are 
        asks you if you want to split/double/stand and tells you if you're right or not 
        '''
        #ask player how much they want to bet
        if self.buy_in:
            starting_bet = input('How much would you like to bet?')
            self.money -= starting_bet
            if self.money < 0:
                return Exception("Sorry, You don't have enough Money to play this hand")
                
        #deal cards 
        self.player_hand


        #ask player for action

        #deal cards based on player action

        #correct player if they want to be corrected 

        #finish dealer hand 

        #check to see if we need to shuffle




if __name__ == '__main__':
     test = BlackJack()
     print('hello world')
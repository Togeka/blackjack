import pandas as pd
import numpy as np
import random 

from card import Card, Deck


#goal of this file:
'''
Create a practice tester that can simulate blackjack hands and help me practice perfect strategy 
'''




class BlackJack():
    def __init__(self, shuffle_type='continuous', money=0, buy_in=False):

        #information about money
        self.correct_hands = 0
        self.total_hands = 0
        self.money = money
        self.buy_in = buy_in
        #information about the hands
        self.dealer_hand = []
        self.player_hand = []
        

        #creating the deck and shuffling 
        self.deck = Deck(num_decks=1) #builds the deck automatically 
        self.deck.full_shuffle()
        self.cards = self.deck.cards



        hard_strat = [['H']*10, ['H']*10, ['H']*10, ['H']*10, ['H']*10, 
              ['H'] + ['D']*4 + ['H']*5,
           ['D']*8 + ['H']*2, ['D']*10, ['H']*2 + ['S']*3 + ['H']*5, 
           ['S']*5 + ['H']*5, ['S']*5 + ['H']*5, 
              ['S']*5 + ['H']*5, ['S']*5 + ['H']*5, 
           ['S']*10,['S']*10, ['S']*10, ['S']*10,['S']*10]
        self.hard_df = pd.DataFrame(index=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21], 
                        columns=[2,3,4,5,6,7,8,9,10,11], data=hard_strat)

        soft_strat = [['H']*2 + ['S']*3 + ['H']*5, 
            ['H']*3 + ['D']*2 + ['H']*5, ['H']*3 + ['D']*2 + ['H']*5,
            ['H']*2 + ['D']*3 + ['H']*5, ['H']*2 + ['D']*3 + ['H']*5,
            ['H'] + ['D']*4 + ['H']*5, ['D']*5 + ['S']*2 + ['H']*3, 
            ['S']*4 + ['D'] + ['S']*5, ['S']*10, ['S']*10]
        self.soft_df = pd.DataFrame(index=[12,13,14,15,16,17,18,19,20,21], 
                        columns=[2,3,4,5,6,7,8,9,10,11], data=soft_strat)        

        pair_strat = [['P']*5 + ['H']*5, ['P']*5 + ['H']*5, ['H']*3 + ['P']*2 + ['H']*5,
             ['D']*8 + ['H']*2, ['P']*5 + ['H']*5, ['P']*6 + ['H']*4, ['P']*10,
             ['P']*5 + ['S'] + ['P']*2 + ['S']*2, ['S']*10, ['P']*10]
        self.pair_df = pd.DataFrame(index=[4,6,8,10,12,14,16,18,20,22], 
                        columns=[2,3,4,5,6,7,8,9,10,11], data=pair_strat) 
        

        


    def deal_card(self):
        # print(self.cards.show())
        pulled_card = random.choice(self.cards)  #pop the top card in the deck
        return pulled_card
       

    def print_hand(self, hand, dealer=False):
        if hand[0].name == 'Ace':
            card1 = 'Ace'
        else:
            card1 = hand[0].val
        if dealer:
            print(card1) #only want the value of the hand 
        else:
            if hand[1].name == 'Ace':
                card2 = 'Ace'
            else:
                card2 = hand[1].val
            
            print(f"{card1} and {card2}")


    def valid_hand(self, hand):
        total = 0
        for i in hand: #iterate through cards in the hand
            total += i.val
            if total > 21:
                return False
        return True 
        

    def correct_play(self, player_hand, dealer_hand, action_given):
        #According to basic strategy does the player play the hand correctly? 
        #If yes return true, if not return what the player should have done 
        
        if player_hand[0].val == player_hand[1].val: #if same values
            #check if the player should split 
            correct_action = self.pair_df._get_value(player_hand[0].val*2, dealer_hand.val).lower()
            print(correct_action)
            if correct_action == action_given:
                return True 
            else:
                return correct_action

        elif player_hand[0].name == 'Ace' or player_hand[1].name == 'Ace':#check if its a hard hand or a soft hand
            correct_action = self.soft_df._get_value(player_hand[0].val + player_hand[1].val, dealer_hand.val).lower()
            if correct_action == action_given:
                return True 
            else:
                return correct_action

        else: #hard hands
            correct_action = self.hard_df._get_value(player_hand[0].val + player_hand[1].val, dealer_hand.val).lower()
            if correct_action == action_given:
                return True 
            else:
                return correct_action


    def play_hand(self, continuous=False):
        '''
        function to play hand 

        prints out gives you the dealers card and prints out what your two cards are 
        asks you if you want to split/double/stand/surrender and tells you if you're right or not and plays out the hand
        '''
        total = 0
        correct = 0
        while True: 
            #deal cards 
            for _ in range(2): #deal out both cards
                self.player_hand.append(self.deal_card()) #deal your first card
                self.dealer_hand.append(self.deal_card()) #do dealers playing card

        
            #ask player for action

            print('Players Hand of: ')
            self.print_hand(self.player_hand)
            print("Dealer's Hand of")
            self.print_hand(self.dealer_hand, dealer=True)

            action = str(input('What would you like to do: ')).lower() #double:d, stand:s, hit:h, split:sp
            if action == 'end':
                break
            
            correct_play = self.correct_play(self.player_hand, self.dealer_hand[0], action)
            if correct_play == True: #need to specify its a boolean
                print('CORRECT')
                correct += 1

            else:
                print(f'INCORRECT, correct action is {correct_play}')
                break

            print()
            print()
            print()
         
            self.player_hand = []
            self.dealer_hand = []

        print(f'This session you got {correct} correct!')

       





if __name__ == '__main__':
     test = BlackJack()
     test.play_hand()

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:31:35 2017

@author: ZHENGHAN ZHANG
"""


#define the numbers and suits first

suitName = {1:'Diamonds',2:'Clubs',3:'Hearts',4:'Spades'}
numberName = {1:'Ace',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'}
class Card:
    def __init__(self,number,suit):
        self.number = number
        self.suit = suit
        
    def __str__(self):
        return str(numberName[self.number])+' of '+ str(suitName[self.suit])
    
    def __gt__(self,target):
        if self.suit > target.suit:
            return True
        elif self.suit < target.suit:
            return False
        else:
            if self.number > target.number:
                return True
            else:
                return False
            
class Deck(list):
    def __init__(self):
        super(Deck,self).__init__()
        for i in range(4):
            for j in range(13):
                card=Card(j,i)
                self.append(card)

    def deal(self):
        self.pop()
        
class Player:
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.card = ''
        
    def recieve(self,card):
        self.card=(card)
        
    def __gt__(self,other):
        if self.wins > other.wins:
            return True
        else:
            return False
        
deck = Deck()
player1=Player('Player1')
player2=Player('Player2')
for i in deck:
    player1.recieve(deck.deal())
    player2.recieve(deck.deal())
    if player1.card > player2.card:
        player1.wins += 1
    elif player2.card > player1.card:
        player2.wins += 1

if player1 > player2:
    print('Player1 wins')
elif player2 > player1:
    print('Player2 wins')
else:
    print('Draw')
    

        
        
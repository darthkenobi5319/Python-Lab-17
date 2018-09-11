# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:24:40 2017

@author: ZHENGHAN ZHANG
"""

class Player:
    def __init__(self,name):
        self.name = name
        self.power = 100
    def __str__(self):
        return self.name +' '+ str(self.power)

    
class FastPlayer(Player):
    def __init__(self,name,speed):
        super(FastPlayer,self).__init__(name)
        self.speed = speed
    def __str__(self):
        return self.name +' '+ str(self.power) + ' ' + str(self.speed)
    
    
class TallPlayer(Player):
    def __init__(self,name,height):
        super(TallPlayer,self).__init__(name)
        self.height = height
    def __str__(self):
        return self.name +' '+ str(self.power) + ' ' + str(self.height)
    
    
    
class CoolPlayer(Player):
    def __init__(self,name,awesomeness):
        super(CoolPlayer,self).__init__(name)
        self.awesomeness = awesomeness
    def __str__(self):
        return self.name +' '+ str(self.power) + ' ' + str(self.awesomeness)

    
p=Player('Player 1')
print(p)
p = FastPlayer('Player 2', 45)
print(p)
p = TallPlayer('Player 3', 197)
print(p)
p = CoolPlayer('Player 4', 9000)
print(p)
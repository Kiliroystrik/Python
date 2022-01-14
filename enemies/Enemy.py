from random import random


class Enemy:

    def __init__(self):
        self.classe = "Brigand"
        self.name = "Kaizer"
        self.strenght = 10
        self.stamina = 10
        self.life = 10
        self.level = 1
        self.attack = self.strenght / 3
        self.expDrop = round((random() * 100),2)

    def hit(self):
     hit = self.strenght/3

    def isDead(self):
        if self.life <= 0:
            return True
        else: 
            return False

# player1 = Player('Mage', 'Kiliroy', 'Striker')

"""
---TEST---
print(player1.name)
print(player1.classe)
print(player1.surname)
"""


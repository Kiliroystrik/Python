class Player:

    def __init__(self, classe, name, surname):
        self.classe = classe
        self.name = name
        self.surname = surname
        self.strenght = 10
        self.stamina = 10
        self.life = 10
        self.experience = 0
        self.level = 1

    def levelUp(self):
        if self.experience < 100:
            self.level = 1
           
        elif self.experience < 250 and self.experience >=100:
            self.level = 2
            self.strenght = +10
            self.stamina = +10
            self.life = +10
        elif self.experience < 450 and self.experience >=250:
            self.level = 3
            self.strenght = +10
            self.stamina = +10
            self.life = +10
        else:
            self.experience = 4

    def hit(self):
     hit = self.strenght/3

    def isDead(self):
     if self.life <= 0:
        print("player is dead")

player1 = Player('Mage', 'Kiliroy', 'Striker')

"""
---TEST---
print(player1.name)
print(player1.classe)
print(player1.surname)
"""


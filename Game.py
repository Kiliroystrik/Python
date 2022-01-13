from Player import Player

class Game:
    
    def __init__(self):

        self.enemyStrenght = 10
        self.enemyLife = 10
        self.enemyAttack = self.enemyStrenght / 3
        self.playerLife = 10
        self.playerStrenght = 10
        self.playerAttack = self.playerStrenght / 3
    
    """BATTLE LOGIC"""
    def battleEngine(self):

        if self.enemyLife > 0:
            print("l'ennemie attaque")
            self.enemyHit()
        else:
            print("vous avez gagné")
            return

        if self.playerLife > 0:
            print("Vous attaquez")
            self.playerHit()
        else:
            print("l'ennemie a gagné")
            return

    def battle(self):
        if self.playerLife > 0 and self.enemyLife > 0:
            self.battleEngine()

    def enemyHit(self):
        self.playerLife = self.playerLife - self.enemyAttack
        print(f"Il vous inflige {self.enemyAttack}  dégats. Il vous reste  { self.playerLife } HP")

    def playerHit(self):
        self.enemyLife = self.enemyLife - self.playerAttack
        print(f"Vous infligez {self.playerAttack}  dégats. L'ennemie a encore {self.enemyLife } HP")

player1 = Player('Mage', 'Kiliroy', 'Striker')

"""
---TEST---
print(player1.name)
print(player1.classe)
print(player1.surname)
"""


game = Game()

game.battle()
game.battle()
game.battle()
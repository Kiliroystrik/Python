from Player import Player
from enemies.Enemy import Enemy
import pygame
pygame.init()

class Game:

    def __init__(self):

        # Instance of player
        self.player = Player("Mage", "Kiliroy", "Moon")

        # Instance of enemy
        self.enemy = Enemy("brigand", "chort", "horror")

    """BATTLE LOGIC"""

    def battleEngine(self):

        # If enemy and player aren't dead 
        if self.enemy.isDead() == False and self.player.isDead() == False:
            print("Vous attaquez")
            self.playerHit()
            # If enemy and isn't dead 
            if self.enemy.isDead() == False:
                print("l'ennemie attaque")
                self.enemyHit()

        # Else if enemy is dead 
        elif self.enemy.isDead():
            self.battleWin()
            return

        # Else player is dead 
        else:
            self.battleLost()
            return

    """WIN BATTLE REWARDS"""

    def battleWin(self):
        self.enemy.drawDead()
        self.player.xp = self.player.xp + self.enemy.expDrop
        self.player.levelUp()
        print(
            f"vous avez gagné {self.enemy.expDrop} XP. Vous etes niveau {self.player.level} avec {self.player.xp} d'xps")

        

    def battleLost(self):
        print("you lose")

    """INIT BATTLE"""

    def battle(self):
        if self.player.isDead() == False and self.enemy.isDead() == False:
            self.battleEngine()
        elif self.enemy.isDead():
            self.battleWin()
        else:
            self.battleLost()

    """ENEMY DAMAGE LOGIC"""

    def enemyHit(self):
        self.player.life = self.player.life - self.enemy.attack

        if self.player.life > 0:
            print(
                f"Il vous inflige {self.enemy.attack}  dégats. Il vous reste  { self.player.life } HP")
        else:
            print(
                f"Il vous inflige {self.enemy.attack}  dégats. Vous n'avez plus de HP")

    """player DAMAGE LOGIC"""

    def playerHit(self):
        self.player.attackAnimation()
        self.enemy.life = self.enemy.life - self.player.attack

        if self.enemy.life > 0:
            print(
                f"Vous infligez {self.player.attack}  dégats. L'ennemie a encore {self.enemy.life } HP")
        else:
            print(
                f"Vous infligez {self.player.attack}  dégats. L'ennemie n'a plus de vie")

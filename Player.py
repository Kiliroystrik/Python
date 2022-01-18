import pygame
pygame.init()
class Player(pygame.sprite.Sprite):

    def __init__(self, classe, name, surname):
        super().__init__()
        self.classe = classe
        self.name = name
        self.surname = surname
        self.strenght = 90
        self.stamina = 10
        self.life = 100
        self.maxLife = 100
        self.experience = 0
        self.level = 1
        self.attack = self.strenght / 3
        self.image = pygame.image.load('assets/rpgDungeon/frames/wizzard_m_idle_anim_f0.png')
        self.resizedImage = pygame.transform.scale(self.image, (70, 120))
        self.rect = self.resizedImage.get_rect()
        self.rect.x = 70
        self.rect.y = 120

    def attackAnimation(self):
        self.image = pygame.image.load('assets/rpgDungeon/frames/wizzard_m_hit_anim_f0.png')


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
            return True
        else: 
            return False

    def healthBar(self, Surface):

        # HEALTH BAR POSITION
        BAR_POSITION = [70, 250, self.life, 10]

        # HEALTH BAR COLOR
        BAR_COLOR = (111, 210, 46)

        pygame.draw.rect(Surface, BAR_COLOR, BAR_POSITION)


# player1 = Player('Mage', 'Kiliroy', 'Striker')

"""
---TEST---
print(player1.name)
print(player1.classe)
print(player1.surname)
"""


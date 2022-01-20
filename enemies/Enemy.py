from random import random
import pygame
pygame.init()
class Enemy(pygame.sprite.Sprite):

    def __init__(self, classe, name, surname):
        super().__init__()
        self.classe = classe
        self.name = name
        self.surname = surname
        self.strenght = 10
        self.stamina = 10
        self.life = 100
        self.maxLife = 100
        self.level = 1
        self.attack = self.strenght / 3
        self.expDrop = round((random() * 100),2)

        self.image = pygame.transform.flip((pygame.image.load(f'assets/rpgDungeon/frames/{self.name}_idle_anim_f0.png')), True, False)
        self.resizedImage = pygame.transform.scale(self.image, ((self.image.get_width() * 5), (self.image.get_height() *5)))
        self.rect = self.resizedImage.get_rect()
        self.rect.x = 500
        self.rect.y = 140

    def attackAnimation(self):
        self.image = pygame.image.load(f'assets/rpgDungeon/frames/{self.name}_hit_anim_f0.png')



    def hit(self):
     hit = self.strenght/3

    def isDead(self):
        if self.life <= 0:
            return True
        else: 
            return False

    def healthBar(self, Surface):

        # HEALTH BAR POSITION
        LIFE_BAR_POSITION = [self.rect.x , (self.rect.y + 20), self.life, 10]
        # HEALTH BAR COLOR
        LIFE_BAR_COLOR = (111, 210, 46)

        # MAX HEALTH BAR POSITION
        MAX_LIFE_BAR_POSITION = [self.rect.x , (self.rect.y + 20), self.maxLife, 10]
        # MAX HEALTH BAR COLOR
        MAX_LIFE_BAR_COLOR = (15, 15, 15)

        pygame.draw.rect(Surface, MAX_LIFE_BAR_COLOR, MAX_LIFE_BAR_POSITION)
        pygame.draw.rect(Surface, LIFE_BAR_COLOR, LIFE_BAR_POSITION)

    def drawDead(self):
        self.image = pygame.transform.flip((pygame.image.load(f'assets/rpgDungeon/frames/{self.name}_idle_anim_f0.png')), True, True)


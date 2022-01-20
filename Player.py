import pygame
pygame.init()
class Player(pygame.sprite.Sprite):

    def __init__(self, classe, name, surname):
        super().__init__()
        self.classe = classe
        self.name = name
        self.surname = surname
        self.strenght = 20
        self.stamina = 10
        self.life = 100
        self.maxLife = 100
        self.xp = 0
        self.max_xp = 100
        self.level = 1
        self.attack = self.strenght / 3
        self.image = pygame.image.load('assets/rpgDungeon/frames/wizzard_m_idle_anim_f0.png')
        self.resizedImage = pygame.transform.scale(self.image, ((self.image.get_width() * 5), (self.image.get_height() *5)))
        self.rect = self.resizedImage.get_rect()
        self.rect.x = 70
        self.rect.y = 120

    def attackAnimation(self):
        self.image = pygame.image.load('assets/rpgDungeon/frames/wizzard_m_hit_anim_f0.png')


    # def levelUp(self):
    #     if self.xp < 100:
    #         self.level = 1
           
    #     elif self.xp < 250 and self.xp >=100:
    #         self.level = 2
    #         self.strenght = +10
    #         self.stamina = +10
    #         self.life = +10
    #     elif self.xp < 450 and self.xp >=250:
    #         self.level = 3
    #         self.strenght = +10
    #         self.stamina = +10
    #         self.life = +10
    #     else:
    #         self.xp = 4

    def levelUp(self):
        if self.xp >= self.max_xp:
            self.level += 1
            self.xp -= self.max_xp
            self.max_xp += 50
            self.statsUp()

    def statsUp(self):
        self.strenght = (20 + 2)
        self.stamina = (10 +2)
        self.maxLife = (100 + 10)
        self.life = self.maxLife

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

    def drawXpBar(self, Surface):

        # XP BAR POSITION
        XP_BAR_POSITION = [self.rect.x , (self.rect.y + 40), self.xp, 10]
        # XP BAR COLOR
        XP_BAR_COLOR = (250, 210, 46)

        # XP BAR POSITION
        MAX_XP_BAR_POSITION = [self.rect.x , (self.rect.y + 40), self.max_xp, 10]
        # XP BAR COLOR
        MAX_XP_BAR_COLOR = (15, 15, 15)

        pygame.draw.rect(Surface, MAX_XP_BAR_COLOR, MAX_XP_BAR_POSITION)
        pygame.draw.rect(Surface, XP_BAR_COLOR, XP_BAR_POSITION)


# player1 = Player('Mage', 'Kiliroy', 'Striker')

"""
---TEST---
print(player1.name)
print(player1.classe)
print(player1.surname)
"""


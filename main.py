import pygame

from enemies.Enemy import Enemy
pygame.init()

from Game import Game
from Player import Player

game = Game()
# print(game.player.life)
# game.battle()
# game.battle()

background = pygame.image.load('assets/main/field.png')

# player = Player("Mage", "Kiliroy", "Moon")

pygame.display.set_caption("RPG FLAIR")
screen = pygame.display.set_mode((720, 420))

running = True

while running:

    screen.blit(background, (0, 0))

    screen.blit(game.player.resizedImage, game.player.rect)

    game.player.healthBar(screen)

    if game.enemy.isDead() == False:
        while game.enemy.isDead() == False:
            game.battle()



    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()

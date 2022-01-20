import pygame

from enemies.Enemy import Enemy
pygame.init()

from Game import Game
from Player import Player

clock = pygame.time.Clock()
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

    clock.tick(60)
    screen.blit(background, (0, 0))

    screen.blit(game.player.resizedImage, game.player.rect)
    screen.blit(game.enemy.resizedImage, game.enemy.rect)

    game.enemy.healthBar(screen)
    game.player.healthBar(screen)
    game.player.drawXpBar(screen)

    # if game.enemy.isDead() == False:
    #     while game.enemy.isDead() == False:
    #         game.battle()

    if pygame.event.get(pygame.MOUSEBUTTONDOWN):
        game.battle()

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    font = pygame.font.SysFont(None, 24)
    img = font.render(f"vous avez gagné {game.enemy.expDrop} XP. Vous etes niveau {game.player.level} avec {game.player.xp} d'xps", True, "blue")
    screen.blit(img, (20, 20))

    pygame.display.update()

pygame.quit()

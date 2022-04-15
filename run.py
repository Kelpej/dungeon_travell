import pygame

from models.game import Game
from models.player.adventurer import Adventurer, Orientation

pygame.init()
game = Game()

pygame.display.set_caption('Dungeon Adventures')
window = pygame.display.set_mode((game.width, game.height))
clock = pygame.time.Clock()
bg = pygame.image.load('assets/bg.jpg').convert()

player = Adventurer(game)

while player.alive:
    window.blit(bg, (0, 0))
    clock.tick(game.fps)

    if player.anim_count > game.fps:
        player.anim_count = 0

    for event in pygame.event.get():                                            #Exit
        if event.type == pygame.QUIT:
            player.live = False

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_f]:
        if not player.attacking:
            player.anim_count = 0
        player.attack()
    else:
        player.attacking = False

    if keys_pressed[pygame.K_a] and player.x > 5:                                           #Move Left
        player.orientation = Orientation.LEFT
        player.run()
    elif keys_pressed[pygame.K_d] and player.x < 1092:                                       #Move Right
        player.orientation = Orientation.RIGHT
        player.run()
    else:
        player.running = False

    if keys_pressed[pygame.K_SPACE]:
        player.jump()

    player.move_y()

    if not (keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_a] or keys_pressed[pygame.K_d]):
        player.moving = False
        player.idle()

    player.anim_count += 1
    window.blit(player.image[player.anim_count % len(player.image)], (player.x, player.y))
    pygame.display.update()
import pygame
from adventurer import Adventurer

pygame.init()

pygame.display.set_caption('Dungeon Adventures')
win = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
bg = pygame.image.load('assets/bg.jpg').convert()

attackRight = [
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-00.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-00.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-01.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-01.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-02.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-02.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-03.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-03.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-04.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-04.png'),

    pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-00.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-01.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-01.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-02.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-03.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-04.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-04.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-05.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-05.png'),

    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-00.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-01.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-01.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-02.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-02.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-03.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-03.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-04.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-04.png'),
    pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-05.png')]

attackLeft = [
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-00.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-00.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-01.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-01.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-02.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-02.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-03.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-03.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-04.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-04.png'),

    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-00.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-01.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-01.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-02.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-03.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-04.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-04.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-05.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-05.png'),

    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-00.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-01.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-01.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-02.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-02.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-03.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-03.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-04.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-04.png'),
    pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-05.png')]

walkRight = [pygame.image.load('assets/adventurer/runRight/adventurer-run-right-00.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-00.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-01.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-01.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-02.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-02.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-03.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-03.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-03.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-04.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-04.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-05.png'),
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-05.png')]

walkLeft = [pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-00.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-00.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-01.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-01.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-02.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-02.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-03.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-03.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-03.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-04.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-04.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-05.png'),
    pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-05.png')]

playerStandRight = [pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-00.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-00.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-00.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-00.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-01.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-01.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-01.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-01.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-02.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-02.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-02.png'),
    pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-02.png')]

playerStandLeft = [pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-00.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-00.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-00.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-00.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-01.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-01.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-01.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-01.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-02.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-02.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-02.png'),
    pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-02.png')]

jumpRight = [pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-00.png'),
    pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-00.png'),
    pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-01.png'),
    pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-01.png'),
    pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-01.png'),
    pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-02.png')]

jumpLight = [pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-00.png'),
    pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-00.png'),
    pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-01.png'),
    pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-01.png'),
    pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-01.png'),
    pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-02.png')]

fallRight = [pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-00.png'),
    pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-00.png'),
    pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-00.png'),
    pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-01.png'),
    pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-01.png'),
    pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-01.png')]

fallLight = [pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-00.png'),
    pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-00.png'),
    pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-00.png'),
    pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-01.png'),
    pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-01.png'),
    pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-01.png')]

attackLeft.

# win.blit(walkLeft[self.animCount % 13], (self.x, self.y))
# self.animCount += 1

player = Adventurer()
while player.live:
    player.clock.tick(25)
    for event in pygame.event.get():                                            #Exit
        if event.type == pygame.QUIT:
            player.live = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        player.attack = True
    else:
        player.attack = False


    if keys[pygame.K_a] and player.x>5:                                           #Move Left
        player.x -= player.speed
        player.left = True
        player.right = False
        player.stand = False

    if keys[pygame.K_d] and  player.x<1092:                                       #Move Right
        player.x += player.speed
        player.left = False
        player.right = True
        player.stand = False

    if player.fall == False:
        if  not(player.isJump):
            if (keys[pygame.K_SPACE]) and (player.y <= 470) and (not(keys[pygame.K_a])) and (not(keys[pygame.K_d])):
                player.isJump = True
                player.stand = False

            if keys[pygame.K_SPACE] and (player.y <= 470) and (keys[pygame.K_a]):
                player.isJump = True
                player.stand = False
                player.left = True

            if keys[pygame.K_SPACE] and (player.y <= 470) and (keys[pygame.K_d]):
                player.isJump = True
                player.stand = False
                player.right = True

        if player.isJump:
            if player.jumpCount >= 1:
                player.y -= (player.jumpCount * abs(player.jumpCount)) * 0.9
                player.jumpCount -= 1
            else:
                player.fall = True

    if player.fall == True:
        if player.jumpCount >= -8:
            player.y -= (player.jumpCount * abs(player.jumpCount)) * 0.9
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.fall = False
            player.jumpCount = 8

    if (not (keys[pygame.K_SPACE])) and (not(keys[pygame.K_a])) and (not(keys[pygame.K_d])):
        player.stand = True

    print(player.fall)
    print(player.y)
    print(player.jumpCount)
    print(keys[pygame.K_f])
    drawWindow(player)

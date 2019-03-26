import pygame
import math
pygame.init()

clock = pygame.time.Clock()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dungeon Advantures')
bg = pygame.image.load('bg.jpg')
x = 30
y = 470
width = 168
height = 125
speed = 20
left = False
right = False
jumpCount = 0
live = True
animCount = 0

walkRight = [pygame.image.load('anims/adventurer-run-right-00.png'),
pygame.image.load('anims/adventurer-run-right-00.png'),
pygame.image.load('anims/adventurer-run-right-01.png'),
pygame.image.load('anims/adventurer-run-right-01.png'),
pygame.image.load('anims/adventurer-run-right-02.png'),
pygame.image.load('anims/adventurer-run-right-02.png'),
pygame.image.load('anims/adventurer-run-right-03.png'),
pygame.image.load('anims/adventurer-run-right-03.png'),
pygame.image.load('anims/adventurer-run-right-03.png'),
pygame.image.load('anims/adventurer-run-right-04.png'),
pygame.image.load('anims/adventurer-run-right-04.png'),
pygame.image.load('anims/adventurer-run-right-05.png'),
pygame.image.load('anims/adventurer-run-right-05.png')]

walkLeft = [pygame.image.load('anims/adventurer-run-left-00.png'),
pygame.image.load('anims/adventurer-run-left-00.png'),
pygame.image.load('anims/adventurer-run-left-01.png'),
pygame.image.load('anims/adventurer-run-left-01.png'),
pygame.image.load('anims/adventurer-run-left-02.png'),
pygame.image.load('anims/adventurer-run-left-02.png'),
pygame.image.load('anims/adventurer-run-left-03.png'),
pygame.image.load('anims/adventurer-run-left-03.png'),
pygame.image.load('anims/adventurer-run-left-03.png'),
pygame.image.load('anims/adventurer-run-left-04.png'),
pygame.image.load('anims/adventurer-run-left-04.png'),
pygame.image.load('anims/adventurer-run-left-05.png'),
pygame.image.load('anims/adventurer-run-left-05.png')]


playerStand = [pygame.image.load('anims/adventurer-idle-2-00.png'),
pygame.image.load('anims/adventurer-idle-2-01.png'),
pygame.image.load('anims/adventurer-idle-2-02.png'),
pygame.image.load('anims/adventurer-idle-2-03.png')]


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 14:
            animCount = 0
    if left:
        win.blit(walkLeft[animCount % 13], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount % 13], (x, y))
        animCount += 1
    else:
        win.blit(playerStand[animCount % 4], (x, y))
    pygame.display.update()


while live:
    clock.tick(14)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x<1092:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
    drawWindow()

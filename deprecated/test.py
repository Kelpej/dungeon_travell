import pygame
import math
pygame.init()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dungeon Advantures')
bg = pygame.image.load('bg.jpg')

walkRight = [pygame.image.load('assets/adventurer-run-right-00.png'),
             pygame.image.load('assets/adventurer-run-right-00.png'),
             pygame.image.load('assets/adventurer-run-right-01.png'),
             pygame.image.load('assets/adventurer-run-right-01.png'),
             pygame.image.load('assets/adventurer-run-right-02.png'),
             pygame.image.load('assets/adventurer-run-right-02.png'),
             pygame.image.load('assets/adventurer-run-right-03.png'),
             pygame.image.load('assets/adventurer-run-right-03.png'),
             pygame.image.load('assets/adventurer-run-right-03.png'),
             pygame.image.load('assets/adventurer-run-right-04.png'),
             pygame.image.load('assets/adventurer-run-right-04.png'),
             pygame.image.load('assets/adventurer-run-right-05.png'),
             pygame.image.load('assets/adventurer-run-right-05.png')]

walkLeft = [pygame.image.load('assets/adventurer-run-left-00.png'),
            pygame.image.load('assets/adventurer-run-left-00.png'),
            pygame.image.load('assets/adventurer-run-left-01.png'),
            pygame.image.load('assets/adventurer-run-left-01.png'),
            pygame.image.load('assets/adventurer-run-left-02.png'),
            pygame.image.load('assets/adventurer-run-left-02.png'),
            pygame.image.load('assets/adventurer-run-left-03.png'),
            pygame.image.load('assets/adventurer-run-left-03.png'),
            pygame.image.load('assets/adventurer-run-left-03.png'),
            pygame.image.load('assets/adventurer-run-left-04.png'),
            pygame.image.load('assets/adventurer-run-left-04.png'),
            pygame.image.load('assets/adventurer-run-left-05.png'),
            pygame.image.load('assets/adventurer-run-left-05.png')]

playerStand = [pygame.image.load('assets/adventurer-idle-2-00.png'),
               pygame.image.load('assets/adventurer-idle-2-00.png'),
               pygame.image.load('assets/adventurer-idle-2-01.png'),
               pygame.image.load('assets/adventurer-idle-2-01.png'),
               pygame.image.load('assets/adventurer-idle-2-02.png'),
               pygame.image.load('assets/adventurer-idle-2-02.png'),
               pygame.image.load('assets/adventurer-idle-2-03.png'),
               pygame.image.load('assets/adventurer-idle-2-03.png')]

jump = [pygame.image.load('assets/adventurer-crnr-jmpr-00.png'),
        pygame.image.load('assets/adventurer-crnr-jmpr-01.png'),
        pygame.image.load('assets/adventurer-crnr-jmpr-02.png')]

class Hero:
    x = 30
    y = 470
    width = 168
    height = 125
    speed = 20
    left = False
    right = False
    jumpCount = 8
    isJump = False
    live = True
    animCount = 0
    clock = pygame.time.Clock()



def drawWindow(self):
    win.blit(bg, (0, 0))
    if self.animCount + 1 >= 14:
        self.animCount = 0
    if self.left:
        win.blit(walkLeft[self.animCount % 13], (self.x, self.y))
        self.animCount += 1
    if self.right:
        win.blit(walkRight[self.animCount % 13], (self.x, self.y))
        self.animCount += 1
    if self.isJump:
        win.blit(jump[self.animCount % 3], (self.x, self.y))
    else:
        win.blit(playerStand[self.animCount % 8], (self.x, self.y))
    pygame.display.update()

char = Hero()
while char.live:
    char.clock.tick(14)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and char.x>5:
        char.x -= char.speed
        char.left = True
        char.right = False

    if keys[pygame.K_RIGHT] and  char.x<1092:
        char.x += char.speed
        char.left = False
        char.right = True

    if not (char.isJump):
        if keys[pygame.K_SPACE] and char.y>=470:
            char.isJump = True
    if char.isJump:
        if char.jumpCount >= -8 :
            char.y -= (char.jumpCount * abs(char.jumpCount)) * 0.7
            char.jumpCount -= 1
        else:
            char.isJump = False
            char.jumpCount = 8
    else:
        left = False
        right = False
    drawWindow(char)

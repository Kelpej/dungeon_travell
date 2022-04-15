import pygame
import math
pygame.init()


win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dungeon Advantures')
bg = pygame.image.load('assets/bg.jpg')

attack1R = [pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-00.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-00.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-01.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-01.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-02.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-02.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-03.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-03.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-04.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-04.png')]

attack1L = [pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-00.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-00.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-01.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-01.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-02.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-02.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-03.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-03.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-04.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-04.png')]

attack2R = [pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-00.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-00.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-01.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-01.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-02.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-02.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-03.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-03.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-04.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-04.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-05.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-05.png')]

attack2L = [pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-00.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-00.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-01.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-01.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-02.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-02.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-03.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-03.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-04.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-04.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-05.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-05.png')]

attack3R = [pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-00.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-00.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-01.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-01.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-02.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-02.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-03.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-03.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-04.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-04.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-05.png'),
            pygame.image.load('assets/adventurer/attackRight/adventurer-attack3r-05.png')]

attack3L = [pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-00.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-00.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-01.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-01.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-02.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-02.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-03.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-03.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-04.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-04.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-05.png'),
            pygame.image.load('assets/adventurer/attackLeft/adventurer-attack3l-05.png')]

walkRight = [pygame.image.load('assets/adventurer/runRight/adventurer-run-right-00.png'),
             pygame.image.load('assets/adventurer/runRight/adventurer-run-right-01.png'),
             pygame.image.load('assets/adventurer/runRight/adventurer-run-right-01.png'),
             pygame.image.load('assets/adventurer/runRight/adventurer-run-right-02.png'),
             pygame.image.load('assets/adventurer/runRight/adventurer-run-right-02.png'),
             pygame.image.load('assets/adventurer/runRight/adventurer-run-right-03.png'),
             pygame.image.load('assets/adventurer/runRight/adventurer-run-right-04.png'),
             pygame.image.load('assets/adventurer/runRight/adventurer-run-right-04.png'),
             pygame.image.load('assets/adventurer/runRight/adventurer-run-right-05.png'),
             pygame.image.load('assets/adventurer/runRight/adventurer-run-right-05.png')]

walkLeft = [pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-00.png'),
            pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-01.png'),
            pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-01.png'),
            pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-02.png'),
            pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-02.png'),
            pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-03.png'),
            pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-04.png'),
            pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-04.png'),
            pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-05.png'),
            pygame.image.load('assets/adventurer/runLeft/adventurer-run-left-05.png')]

playerStandR = [pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-00.png'),
                pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-00.png'),
                pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-00.png'),
                pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-01.png'),
                pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-01.png'),
                pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-01.png'),
                pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-02.png'),
                pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-02.png'),
                pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-02.png'),
                pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-02.png')]

playerStandL = [pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-00.png'),
                pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-00.png'),
                pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-00.png'),
                pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-01.png'),
                pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-01.png'),
                pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-01.png'),
                pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-02.png'),
                pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-02.png'),
                pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-02.png'),
                pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-02.png')]

jumpR = [pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-00.png'),
         pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-00.png'),
         pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-01.png'),
         pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-01.png'),
         pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-01.png'),
         pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-02.png')]

jumpL = [pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-00.png'),
         pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-00.png'),
         pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-01.png'),
         pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-01.png'),
         pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-01.png'),
         pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-02.png')]

fallR = [pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-00.png'),
         pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-00.png'),
         pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-00.png'),
         pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-01.png'),
         pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-01.png'),
         pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-01.png')]

fallL = [pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-00.png'),
         pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-00.png'),
         pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-00.png'),
         pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-01.png'),
         pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-01.png'),
         pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-01.png')]

minWalkRight = [pygame.image.load('assets/minotaur/walkR/walkR_01.png'),
                pygame.image.load('assets/minotaur/walkR/walkR_02.png'),
                pygame.image.load('assets/minotaur/walkR/walkR_03.png'),
                pygame.image.load('assets/minotaur/walkR/walkR_04.png'),
                pygame.image.load('assets/minotaur/walkR/walkR_05.png'),
                pygame.image.load('assets/minotaur/walkR/walkR_06.png'),
                pygame.image.load('assets/minotaur/walkR/walkR_07.png'),
                pygame.image.load('assets/minotaur/walkR/walkR_08.png')]

minWalkLeft = [pygame.image.load('assets/minotaur/walkL/walkL_01.png'),
               pygame.image.load('assets/minotaur/walkL/walkL_02.png'),
               pygame.image.load('assets/minotaur/walkL/walkL_03.png'),
               pygame.image.load('assets/minotaur/walkl/walkL_04.png'),
               pygame.image.load('assets/minotaur/walkL/walkL_05.png'),
               pygame.image.load('assets/minotaur/walkL/walkL_06.png'),
               pygame.image.load('assets/minotaur/walkL/walkL_07.png'),
               pygame.image.load('assets/minotaur/walkL/walkL_08.png')]

minIdleR = [pygame.image.load('assets/minotaur/idleR/idleR_01.png'),
            pygame.image.load('assets/minotaur/idleR/idleR_02.png'),
            pygame.image.load('assets/minotaur/idleR/idleR_03.png'),
            pygame.image.load('assets/minotaur/idleR/idleR_04.png'),
            pygame.image.load('assets/minotaur/idleR/idleR_05.png')]

minIdleL = [pygame.image.load('assets/minotaur/idleL/idleL_01.png'),
            pygame.image.load('assets/minotaur/idleL/idleL_02.png'),
            pygame.image.load('assets/minotaur/idleL/idleL_03.png'),
            pygame.image.load('assets/minotaur/idleL/idleL_04.png'),
            pygame.image.load('assets/minotaur/idleL/idleL_05.png')]

minAttack1R = [pygame.image.load('assets/minotaur/attackR/attackR_01.png'),
               pygame.image.load('assets/minotaur/attackR/attackR_02.png'),
               pygame.image.load('assets/minotaur/attackR/attackR_03.png'),
               pygame.image.load('assets/minotaur/attackR/attackR_04.png'),
               pygame.image.load('assets/minotaur/attackR/attackR_05.png'),
               pygame.image.load('assets/minotaur/attackR/attackR_06.png'),
               pygame.image.load('assets/minotaur/attackR/attackR_07.png'),
               pygame.image.load('assets/minotaur/attackR/attackR_08.png'),
               pygame.image.load('assets/minotaur/attackR/attackR_09.png')]

minAttack1L = [pygame.image.load('assets/minotaur/attackL/attackL_01.png'),
               pygame.image.load('assets/minotaur/attackL/attackL_02.png'),
               pygame.image.load('assets/minotaur/attackL/attackL_03.png'),
               pygame.image.load('assets/minotaur/attackL/attackL_04.png'),
               pygame.image.load('assets/minotaur/attackL/attackL_05.png'),
               pygame.image.load('assets/minotaur/attackL/attackL_06.png'),
               pygame.image.load('assets/minotaur/attackL/attackL_07.png'),
               pygame.image.load('assets/minotaur/attackL/attackL_08.png'),
               pygame.image.load('assets/minotaur/attackL/attackL_09.png')]

minAttack2R = [pygame.image.load('assets/minotaur/attack2R/attack2R_01.png'),
               pygame.image.load('assets/minotaur/attack2R/attack2R_02.png'),
               pygame.image.load('assets/minotaur/attack2R/attack2R_03.png'),
               pygame.image.load('assets/minotaur/attack2R/attack2R_04.png'),
               pygame.image.load('assets/minotaur/attack2R/attack2R_05.png'),
               pygame.image.load('assets/minotaur/attack2R/attack2R_06.png'),
               pygame.image.load('assets/minotaur/attack2R/attack2R_07.png'),
               pygame.image.load('assets/minotaur/attack2R/attack2R_08.png'),
               pygame.image.load('assets/minotaur/attack2R/attack2R_09.png')]

minAttack2L = [pygame.image.load('assets/minotaur/attack2L/attack2L_01.png'),
               pygame.image.load('assets/minotaur/attack2L/attack2L_02.png'),
               pygame.image.load('assets/minotaur/attack2L/attack2L_03.png'),
               pygame.image.load('assets/minotaur/attack2L/attack2L_04.png'),
               pygame.image.load('assets/minotaur/attack2L/attack2L_05.png'),
               pygame.image.load('assets/minotaur/attack2L/attack2L_06.png'),
               pygame.image.load('assets/minotaur/attack2L/attack2L_07.png'),
               pygame.image.load('assets/minotaur/attack2L/attack2L_08.png'),
               pygame.image.load('assets/minotaur/attack2L/attack2L_09.png')]

minStompR = [pygame.image.load('assets/minotaur/stompR/stompR_01.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_02.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_03.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_04.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_05.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_06.png')]

minStompL = [pygame.image.load('assets/minotaur/stompR/stompR_01.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_02.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_03.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_04.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_05.png'),
             pygame.image.load('assets/minotaur/stompR/stompR_06.png')]

class Hero:
    x = 30
    y = 470
    width = 168
    height = 125
    speed = 23
    left = False
    right = True
    stand = True
    jumpCount = 8
    isJump = False
    fall = False
    live = True
    animCountRun = 0
    animCountIdle = 0
    animCountJump = 0
    animCountAttack1 = 0
    animCountAttack2 = 0
    animCountAttack3 = 0
    attack = False
    clock = pygame.time.Clock()
    attackn = 1
    duration1 = 10
    duration2 = 11
    duration3 = 12.5
    attackInterval = 1000

class Enemy:
    x = 1100
    y = 499
    width = 98
    height = 96
    left = True
    right = False
    stand = True
    live = True
    animCountRun = 0
    animCountIdle = 0
    animCountStomp = 0
    animCountAttack = 0
    attack = False
    duration1 = 10
    duration2 = 11
    clock = pygame.time.Clock()

char = Hero()
min = Enemy()

def playerAttack1R(self):
    win.blit(attack1R[self.animCountAttack1 % 10], (self.x, self.y))
    self.animCountAttack1 += 1

def playerAttack1L(self):
    win.blit(attack1L[self.animCountAttack1 % 10], (self.x, self.y))
    self.animCountAttack1 += 1

def playerAttack2R(self):
    win.blit(attack2R[self.animCountAttack2 % 11], (self.x, self.y))
    self.animCountAttack2 += 1

def playerAttack2L(self):
    win.blit(attack2L[self.animCountAttack2 % 11], (self.x, self.y))
    self.animCountAttack2 += 1

def playerAttack3R(self):
    win.blit(attack3R[self.animCountAttack3 % 12], (self.x, self.y))
    self.animCountAttack3 += 1

def playerAttack3L(self):
    win.blit(attack3L[self.animCountAttack3 % 12], (self.x, self.y))
    self.animCountAttack3 += 1

def playerWalkR(self):
    win.blit(walkRight[self.animCountRun % 10], (self.x, self.y))
    self.animCountRun += 1

def playerWalkL(self):
    win.blit(walkLeft[self.animCountRun % 10], (self.x, self.y))
    self.animCountRun += 1

def playerStandRight(self):
    win.blit(playerStandR[self.animCountIdle % 10], (self.x, self.y))
    self.animCountIdle += 1

def playerStandLeft(self):
    win.blit(playerStandL[self.animCountIdle % 10], (self.x, self.y))
    self.animCountIdle += 1

def playerJumpR(self):
    win.blit(jumpR[self.animCountJump % 6], (self.x, self.y))
    self.animCountJump += 1

def playerJumpL(self):
    win.blit(jumpL[self.animCountJump % 6], (self.x, self.y))
    self.animCountJump += 1

def playerFallR(self):
    win.blit(fallR[self.animCountJump % 6], (self.x, self.y))
    self.animCountJump += 1

def playerFallL(self):
    win.blit(fallL[self.animCountJump % 6], (self.x, self.y))
    self.animCountJump += 1

def minWalkRight(self):
    win.blit(minWalkRight[min.animCountRun % 8], (min.x, self.y))
    min.animCountRun += 1

def minWalkLeft(self):
    win.blit(minWalkLeft[min.animCountRun % 8], (min.x, self.y))
    min.animCountRun += 1

def minIdleR(self):
    win.blit(minIdleR[min.animCountIdle % 5], (min.x, self.y))
    min.animCountIdle += 1

def minIdleL(self):
    win.blit(minIdleL[min.animCountIdle % 5], (min.x, self.y))
    min.animCountIdle += 1

def drawWindow(self, enemy):

    win.blit(bg, (0, 0))
    if self.y < 470:
        self.isJump = True

    if self.animCountRun + 1 >= 10:
        self.animCountRun = 1

    if self.animCountIdle + 1 >= 10:
        self.animCountIdle = 1

    if self.animCountJump + 1 >= 6:
        self.animCountJump = 1

    if self.animCountAttack1 + 1 >= 10:
        self.animCountAttack1 = 0

    if self.animCountAttack2 + 1 >= 11:
        self.animCountAttack2 = 0

    if self.animCountAttack3 + 1 >= 12:
        self.animCountAttack3 = 0

    if min.animCountRun + 1 >= 8:
        min.animCountRun = 0

    if min.animCountStomp + 1 >= 6:
        min.animCountStomp = 0

    if min.animCountAttack + 1 >= 9:
        min.animCountRun = 0

    if min.animCountIdle + 1 >= 5:
        min.animCountIdle = 0

    if self.right and not(self.isJump) and self.attack and not(self.left):
        if self.attackn == 1:
            playerAttack1R(char)
        if self.attackn == 2:
            playerAttack2R(char)
        if self.attackn == 3:
            playerAttack3R(char)

    if self.left and self.attack and not(self.isJump) and not(self.right):
        if self.attackn == 1:
            playerAttack1L(char)
        if self.attackn == 2:
            playerAttack2L(char)
        if self.attackn == 3:
            playerAttack3L(char)

    if keys[pygame.K_d] and keys[pygame.K_a] and not(self.isJump):
        playerStandRight(char)

    if self.stand and not(self.isJump) and not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and self.right and not(self.attack):
        playerStandRight(char)

    if self.stand and not(self.isJump) and not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and self.left or (not (self.isJump) and keys[pygame.K_a] and keys[pygame.K_d] and self.left):
        playerStandLeft(char)

    if self.right and not(self.stand) and self.isJump and not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and not(self.fall):
        playerJumpR(char)

    if (self.isJump) and (self.right) and not(self.left) and not(self.fall):
        playerJumpR(char)

    if self.isJump and self.left and not(self.right) and not(self.fall):
        playerJumpL(char)

    if (self.left) and (self.isJump) and (not (self.stand)) and not(keys[pygame.K_a]) and not(keys[pygame.K_d]) and not(self.fall):
        playerJumpL(char)

    if self.right and self.fall:
        playerFallR(char)

    if self.left and self.fall:
        playerFallL(char)

    if not(keys[pygame.K_c]):
        if (keys[pygame.K_d]) and not(keys[pygame.K_a]) and not(self.isJump):
            playerWalkR(char)

        if (keys[pygame.K_a]) and not(self.isJump) and not(keys[pygame.K_d]):
            playerWalkL(char)



    pygame.display.update()

while char.live:
    char.clock.tick(15)
    min.clock.tick(15)
    for event in pygame.event.get():                                            #Exit
        if event.type == pygame.QUIT:
            char.live = False

    keys = pygame.key.get_pressed()

    if char.y >= 470:
        char.isJump = False
    else:
        char.isJump = True


    if keys[pygame.K_c] and not(char.isJump) and not(keys[pygame.K_a] and keys[pygame.K_d]):
        char.stand = False
        char.attack = True

        if char.attackn == 1 and char.duration1 > 0:
            char.duration1 -= 1
        elif char.duration1 <= 0:
            char.attackn += 1
            char.animCountAttack1 = 0
            char.duration1 = 10

        if char.attackn == 2 and char.duration2 > 0:
            char.duration2 -= 1
        elif char.duration2 <= 0:
            char.attackn += 1
            char.animCountAttack2 = 0
            char.duration2 = 11

        if char.attackn == 3 and char.duration3 > 0:
            char.duration3 -= 1
        elif char.duration3 <= 0:
            char.attackn = 1
            char.animCountAttack3 = 0
            char.duration3 = 12.5

    else:
        char.attack = False
        char.duration1 = 10
        char.duration2 = 11
        char.duration3 = 12.5
        char.animCountAttack1 = 0
        char.animCountAttack2 = 0
        char.animCountAttack3 = 0



    if keys[pygame.K_a] and char.x>5 and not(keys[pygame.K_c]):                                       #Move Left
        char.x -= char.speed
        char.left = True
        char.right = False
        char.stand = False

    if keys[pygame.K_d] and char.x<1092 and not(keys[pygame.K_c]):                                   #Move Right
        char.x += char.speed
        char.left = False
        char.right = True
        char.stand = False

    if char.fall == False:
        if  not(char.isJump):
            if (keys[pygame.K_SPACE] and not(keys[pygame.K_a] and keys[pygame.K_d])) or (keys[pygame.K_SPACE] and keys[pygame.K_a] and keys[pygame.K_d]):
                char.isJump = True
                char.stand = False

            if keys[pygame.K_SPACE] and keys[pygame.K_a] and not(keys[pygame.K_d]):
                char.isJump = True
                char.stand = False
                char.left = True

            if keys[pygame.K_SPACE] and (keys[pygame.K_d]) and not(keys[pygame.K_a]):
                char.isJump = True
                char.stand = False
                char.right = True

        if char.isJump:
            if char.jumpCount >= 1:
                char.y -= (char.jumpCount * abs(char.jumpCount)) * 0.9
                char.jumpCount -= 1
            else:
                char.fall = True

    if char.fall == True:
        if char.jumpCount >= -8:
            char.y -= (char.jumpCount * abs(char.jumpCount)) * 0.9
            char.jumpCount -= 1
        else:
            char.fall = False
            char.jumpCount = 8
            char.stand = True
	
    if not(keys[pygame.K_d] and keys[pygame.K_a] and char.fall and keys[pygame.K_SPACE] and keys[pygame.K_c]):
        char.stand = True
		
    print(char.animCountAttack1)
    print(char.animCountAttack2)
    print(char.animCountAttack3)
    print('\n')
    drawWindow(char, min)

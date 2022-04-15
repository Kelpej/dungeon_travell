import pygame
pygame.init()


win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dungeon Adventures')
bg = pygame.image.load('assets/bg.jpg')

attack1L = [
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-00.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-00.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-01.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-01.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-02.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-02.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-03.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-03.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-04.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack1l-04.png')]

attack2L = [
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-00.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-01.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-01.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-02.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-03.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-04.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-04.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-05.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-05.png')]

attackR = [
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-00.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-01.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-01.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-02.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-03.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-04.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-04.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-05.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-05.png')]

attack1R = [
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-00.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-00.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-01.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-01.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-02.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-02.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-03.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-03.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-04.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack1r-04.png')]

attack2R = [
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-00.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-01.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-01.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-02.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-02.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-03.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-03.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-04.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-04.png'),
pygame.image.load('assets/adventurer/attackRight/adventurer-attack2r-05.png')]

attack3R = [
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


attack2L = [
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-00.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-01.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-01.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-02.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-02.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-03.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-03.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-04.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-04.png'),
pygame.image.load('assets/adventurer/attackLeft/adventurer-attack2l-05.png')]

attack3L = [
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

class Hero:
    x = 30
    y = 470
    width = 168
    height = 125
    speed = 20
    left = False
    right = True
    stand = True
    jumpCount = 8
    isJump = False
    fall = False
    live = True
    animCount = 0
    attack = False
    clock = pygame.time.Clock()
    attack = pygame.time.Clock()
    attack1AnimTime = 100

def playerWalkR(self):
    walkRight = [
    pygame.image.load('assets/adventurer/runRight/adventurer-run-right-00.png'),
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

    win.blit(walkRight[self.animCount % 13], (self.x, self.y))
    self.animCount += 1

def playerWalkL(self):
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

    win.blit(walkLeft[self.animCount % 13], (self.x, self.y))
    self.animCount += 1

def playerStandR(self):
    playerStandR = [pygame.image.load('assets/adventurer/idleRight/idle_1/adventurer-idler-00.png'),
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

    win.blit(playerStandR[self.animCount % 12], (self.x, self.y))
    self.animCount += 1

def playerStandL(self):
    playerStandL = [pygame.image.load('assets/adventurer/idleLeft/idle_1/adventurer-idlel-00.png'),
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

    win.blit(playerStandL[self.animCount % 12], (self.x, self.y))
    self.animCount += 1

def playerJumpR(self):
    jumpR = [pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-00.png'),
             pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-00.png'),
             pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-01.png'),
             pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-01.png'),
             pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-01.png'),
             pygame.image.load('assets/adventurer/jumpRight/adventurer-crnr-jmpr-02.png')]

    win.blit(jumpR[self.animCount % 6], (self.x, self.y))
    self.animCount += 1

def playerJumpL(self):
    jumpL = [pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-00.png'),
             pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-00.png'),
             pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-01.png'),
             pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-01.png'),
             pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-01.png'),
             pygame.image.load('assets/adventurer/jumpLeft/adventurer-crnr-jmpl-02.png')]

    win.blit(jumpL[self.animCount % 6], (self.x, self.y))
    self.animCount += 1

def playerFallR(self):
    fallR = [pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-00.png'),
             pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-00.png'),
             pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-00.png'),
             pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-01.png'),
             pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-01.png'),
             pygame.image.load('assets/adventurer/fallRight/adventurer-fallr-01.png')]

    win.blit(fallR[self.animCount % 6], (self.x, self.y))
    self.animCount += 1

def playerFallL(self):
    fallL = [pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-00.png'),
             pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-00.png'),
             pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-00.png'),
             pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-01.png'),
             pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-01.png'),
             pygame.image.load('assets/adventurer/fallLeft/adventurer-falll-01.png')]

    win.blit(fallL[self.animCount % 6], (self.x, self.y))
    self.animCount += 1


def drawWindow(self):

    win.blit(bg, (0, 0))
    if self.y < 470:
        self.isJump = True

    if self.animCount + 1 >= 14:
        self.animCount = 0

    if (keys[pygame.K_f]) and (self.right):
        win.blit(attack1R[self.animCount % 10], (self.x, self.y))
        self.animCount += 1
    if (keys[pygame.K_f]) and (self.left):
        win.blit(attack1L[self.animCount % 10], (self.x, self.y))
        self.animCount += 1

    if (keys[pygame.K_d]) and (keys[pygame.K_a]) and (not(self.isJump)) and (not((keys[pygame.K_f]))):
        playerStandR(char)

    if (self.stand) and (not (self.isJump)) and (not(keys[pygame.K_a])) and (not(keys[pygame.K_d])) and (self.right) and (not((keys[pygame.K_f]))):
        playerStandR(char)

    if ((self.stand) and (not (self.isJump)) and (not(keys[pygame.K_a])) and (not(keys[pygame.K_d])) and (self.left)) or ((not (self.isJump)) and (keys[pygame.K_a]) and (keys[pygame.K_d]) and (self.left)) and (not((keys[pygame.K_f]))):
        playerStandL(char)

    if (self.right) and (not (self.stand)) and (self.isJump) and (not(keys[pygame.K_a])) and (not(keys[pygame.K_d])) and (not(self.fall)) and (not((keys[pygame.K_f]))):
        playerJumpR(char)

    if (self.isJump) and (self.right) and (not(self.left)) and (not(self.fall)) and (not((keys[pygame.K_f]))):
        playerJumpR(char)

    if (self.isJump) and (self.left) and (not(self.right)) and (not(self.fall)) and (not((keys[pygame.K_f]))):
        playerJumpL(char)

    if (self.left) and (not (self.stand)) and (self.isJump) and (not(keys[pygame.K_a])) and (not(keys[pygame.K_d])) and (not(self.fall)) and (not((keys[pygame.K_f]))):
        playerJumpL(char)

    if self.right and self.fall and not((keys[pygame.K_f])):
        playerFallR(char)

    if self.left and self.fall and not((keys[pygame.K_f])):
        playerFallL(char)
    if (keys[pygame.K_d]) and (not(keys[pygame.K_a])) and (not(self.isJump)) and (not((keys[pygame.K_f]))):
        playerWalkR(char)

    if (keys[pygame.K_a]) and (not(self.isJump)) and (not(keys[pygame.K_d])) and (not((keys[pygame.K_f]))):
        playerWalkL(char)

    pygame.display.update()

char = Hero()
while char.live:
    char.clock.tick(25)
    for event in pygame.event.get():                                            #Exit
        if event.type == pygame.QUIT:
            char.live = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        char.attack = True
    else:
        char.attack = False


    if keys[pygame.K_a] and char.x>5:                                           #Move Left
        char.x -= char.speed
        char.left = True
        char.right = False
        char.stand = False

    if keys[pygame.K_d] and  char.x<1092:                                       #Move Right
        char.x += char.speed
        char.left = False
        char.right = True
        char.stand = False

    if char.fall == False:
        if  not(char.isJump):
            if (keys[pygame.K_SPACE]) and (char.y<=470) and (not(keys[pygame.K_a])) and (not(keys[pygame.K_d])):
                char.isJump = True
                char.stand = False

            if keys[pygame.K_SPACE] and (char.y<=470) and (keys[pygame.K_a]):
                char.isJump = True
                char.stand = False
                char.left = True

            if keys[pygame.K_SPACE] and (char.y<=470) and (keys[pygame.K_d]):
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
            char.isJump = False
            char.fall = False
            char.jumpCount = 8

    if (not (keys[pygame.K_SPACE])) and (not(keys[pygame.K_a])) and (not(keys[pygame.K_d])):
        char.stand = True

    print(char.fall)
    print(char.y)
    print(char.jumpCount)
    print(keys[pygame.K_f])
    drawWindow(char)

from enum import Enum
from models.game import Game

from models.player.animations import *


class Orientation(Enum):
    LEFT = 1
    RIGHT = 2


class Adventurer:
    x, y = 30, 470
    vel_x, vel_y = 20, 20
    jump_pos = y
    anim_count = 0

    image = idleRight
    orientation = Orientation.RIGHT

    alive = True
    moving = False
    running = False
    jumping = False
    falling = False
    attacking = False

    def __init__(self, game: Game):
        self.game = game

    def move_x(self):
        if not self.attacking:
            self.moving = True
            if self.orientation == Orientation.RIGHT:
                self.x += self.vel_x
            else:
                self.x -= self.vel_x

    def move_y(self):
        if self.jumping and self.y >= self.jump_pos - self.game.jump_height:
            self.y -= self.vel_y
            if self.orientation == Orientation.RIGHT:
                self.image = jumpRight
            else:
                self.image = jumpLeft
        elif (self.jumping or self.falling)\
                and self.y < self.jump_pos:
            self.jumping = False
            self.falling = True
            self.y += self.vel_y
            if self.orientation == Orientation.RIGHT:
                self.image = fallRight
            else:
                self.image = fallLeft
        elif self.falling and self.y >= self.jump_pos:
            self.y = self.jump_pos
            self.falling = False
            self.moving = False

    def run(self):
        if not self.attacking:
            self.move_x()
        if not (self.jumping or self.falling or self.attacking):
            self.running = True
            if self.orientation == Orientation.RIGHT:
                self.image = runRight
            else:
                self.image = runLeft

    def idle(self):
        if not (self.moving or self.running or self.jumping or self.falling or self.attacking):
            if self.orientation == Orientation.RIGHT:
                self.image = idleRight
            else:
                self.image = idleLeft

    def attack(self):
        if not (self.jumping or self.falling):
            self.attacking = True
            self.running = False
            self.moving = False

            if self.orientation == Orientation.RIGHT:
                self.image = attackRight
            elif self:
                self.image = attackLeft

    def jump(self):
        if not (self.attacking or self.jumping or self.falling):
            self.jump_pos = self.y
            self.jumping = True

from enum import Enum


class Orientation(Enum):
    LEFT = 1
    RIGHT = 2

class Adventurer:
    x, y = 30, 470
    vel_x, vel_y = 20, 10
    animCount = 0
    orientation = Orientation.RIGHT
    alive = True
    idle = True
    running = False
    jumping = False
    falling = False
    attacking = False

    def __init__(self):
        pass
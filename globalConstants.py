from enum import Enum

class Direction:
    EAST   = 0
    WEST   = 1
    NORTH  = 2
    SOUTH  = 3

class FieldType:
    EMPTY  = 0
    SNAKE  = 1
    FOOD   = 2
    BORDER = 3

class BoardColor:
    DARKGREEN = (0, 180, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (60, 60, 60)

HEAD = 0
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

HEAD = 0
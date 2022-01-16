from direction import Direction

class Snake:

    __length = None
    __headPosition_X = None
    __headPosition_Y = None


    def __init__(self, length, headPosition_X, headPosition_Y):
        self.__length = length
        self.__headPosition_X = headPosition_X
        self.__headPosition_Y = headPosition_Y

    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length

    def getHeadPosition_X(self):
        return self.__headPosition_X
    
    def setHeadPosition_X(self, headPosition_X):
        self.__headPosition_X = headPosition_X

    def getHeadPosition_Y(self):
        return self.__headPosition_Y
    
    def setHeadPosition_Y(self, headPosition_Y):
        self.__headPosition_Y = headPosition_Y


# 0 for right, 1 for left, 2 for up, 3 for down
    def moveHeadInDirection(self, direction):
        if direction == Direction.RIGHT:
            self.__headPosition_X += 1
        elif direction == Direction.LEFT:
            self.__headPosition_X -= 1
        elif direction == Direction.UP:
            self.__headPosition_Y += 1
        elif direction == Direction.DOWN:
            self.__headPosition_Y -= 1
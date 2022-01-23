from random import random
import numpy as np
from snake import Snake
from globalConstants import FieldType
import random

class Field:

    __snakeCoordsX = []
    __snakeCoordsY = []
    # np array __fields
    # __squareSize
    
    def __init__(self, squareSize):
        self.__fields = np.zeros([squareSize, squareSize], dtype=int)
        
        for y in range(0, squareSize):
            self.__fields[y][0] = FieldType.BORDER
            self.__fields[y][squareSize-1] = FieldType.BORDER
        
        for x in range(0, squareSize):
            self.__fields[0][x] = FieldType.BORDER
            self.__fields[squareSize-1][x] = FieldType.BORDER
        
        self.__squareSize = squareSize

    
    def getSquareSize(self):
        return self.__squareSize

    def getFields(self, atX, atY):
        return self.__fields[atY][atX]

    def setSnakeFields(self, snake):     
        self.__removeSnakeFromField()

        for i in range(0, snake.getLength()):
            self.__fields[snake.getSnakeCoordY(i)][snake.getSnakeCoordX(i)] = FieldType.SNAKE
            self.__snakeCoordsX.append(snake.getSnakeCoordX(i))
            self.__snakeCoordsY.append(snake.getSnakeCoordY(i))


    def __removeSnakeFromField(self):
        snakeLength = len(self.__snakeCoordsX)
        for i in range(0, snakeLength):
    
            if self.__fields[self.__snakeCoordsY[i]][self.__snakeCoordsX[i]] == FieldType.SNAKE:
                self.__fields[self.__snakeCoordsY[i]][self.__snakeCoordsX[i]] = FieldType.EMPTY

        self.__snakeCoordsX = []
        self.__snakeCoordsY = []

    def spawnFood(self):
    
        x = random.randint(1, self.__squareSize-2)
        y = random.randint(1, self.__squareSize-2)

        while (self.__fields[y][x] == FieldType.SNAKE):
            x = random.randint(1, self.__squareSize-2)
            y = random.randint(1, self.__squareSize-2)

        self.__fields[y][x] = FieldType.FOOD

    
import numpy as np
from snake import Snake
from globalConstants import FieldType

class Field:
    
    def __init__(self, squareSize):
        self.fields = np.zeros([squareSize, squareSize], dtype=int)
        
        for y in range(0, squareSize):
            self.fields[y][0] = FieldType.BORDER
            self.fields[y][squareSize-1] = FieldType.BORDER
        
        for x in range(0, squareSize):
            self.fields[0][x] = FieldType.BORDER
            self.fields[squareSize-1][x] = FieldType.BORDER


    def setSnakeFields(self, snake):
        for i in range(0, snake.getLength()):
            self.fields[snake.getSnakeCoordY(i)][snake.getSnakeCoordX(i)] = FieldType.SNAKE

    def performSnakeMove(self, snake, nextContainsFood=False):
        if nextContainsFood == True:
            tmpX = snake.getSnakeCoordX(snake.getLength()-1)
            tmpY = snake.getSnakeCoordY(snake.getLength()-1)

        snake.moveInDirection()


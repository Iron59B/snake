import numpy as np
from snake import Snake
from globalConstants import FieldType

class Field:

    snakeCoordsX = []
    snakeCoordsY = []
    
    def __init__(self, squareSize):
        self.fields = np.zeros([squareSize, squareSize], dtype=int)
        
        for y in range(0, squareSize):
            self.fields[y][0] = FieldType.BORDER
            self.fields[y][squareSize-1] = FieldType.BORDER
        
        for x in range(0, squareSize):
            self.fields[0][x] = FieldType.BORDER
            self.fields[squareSize-1][x] = FieldType.BORDER

        self.__squareSize = squareSize

    
    def getSquareSize(self):
        return self.__squareSize

    def setSnakeFields(self, snake):     
        self.removeSnakeFromField()

        for i in range(0, snake.getLength()):
            self.fields[snake.getSnakeCoordY(i)][snake.getSnakeCoordX(i)] = FieldType.SNAKE
            self.snakeCoordsX.append(snake.getSnakeCoordX(i))
            self.snakeCoordsY.append(snake.getSnakeCoordY(i))


    def removeSnakeFromField(self):
        snakeLength = len(self.snakeCoordsX)
        for i in range(0, snakeLength):
    
            if self.fields[self.snakeCoordsY[i]][self.snakeCoordsX[i]] == FieldType.SNAKE:
                self.fields[self.snakeCoordsY[i]][self.snakeCoordsX[i]] = FieldType.EMPTY

        self.snakeCoordsX = []
        self.snakeCoordsY = []
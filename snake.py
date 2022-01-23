from globalConstants import HEAD, Direction, FieldType

class Snake:

    __length        = None
    __color         = None
    __snakeCoordX   = []
    __snakeCoordY   = []
    __direction     = None

    def __init__(self, length, headPositionX, headPositionY, color, direction):
        self.__length = length
        self.__color = color
        self.__snakeCoordX.append(headPositionX)
        self.__snakeCoordY.append(headPositionY)
        self.__direction = direction
        self.initSnakeBody(direction, length)

    def initSnakeBody(self, direction, length):
        if length > 6:
            print("snake initially too long")
            exit()

        # TODO implement other starting directions
        if direction == Direction.EAST:
            for i in range(1, length):
                self.__snakeCoordY.append(self.__snakeCoordY[HEAD])
                self.__snakeCoordX.append(self.__snakeCoordX[HEAD] - i)
                
        else:
            print("snake must start in direction RIGHT")
            exit()

    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length

    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.color = color

    def getDirection(self):
        return self.__direction

    def setDirection(self, direction):
        self.__direction = direction

    def getSnakeCoordX(self, index):
        return self.__snakeCoordX[index]

    def getSnakeCoordY(self, index):
        return self.__snakeCoordY[index]


    # head of snake is moving in given direction
    # rest of the snake is moving forward (replacing previous piece respectively)
    # this is done using two tmp variables for x and y coordinates each
    # one tmp is used to store current value of the piece and afterwards current value changes to previously created tmp
    # tmp0 and tmp1 to hold correct order (alternating dependent on remainder of division by 2)
    def moveInDirection(self, direction, field):
        eating = False
        tmpX_0 = self.__snakeCoordX[HEAD]
        tmpY_0 = self.__snakeCoordY[HEAD]

        if direction == Direction.EAST:
            self.__snakeCoordX[HEAD] += 1
        elif direction == Direction.WEST:
            self.__snakeCoordX[HEAD] -= 1
        elif direction == Direction.NORTH:
            self.__snakeCoordY[HEAD] -= 1
        elif direction == Direction.SOUTH:
            self.__snakeCoordY[HEAD] += 1

        print(direction)

        # field only holds current part of snake after calling field.drawSnake()
        if field.getFields(self.__snakeCoordX[HEAD], self.__snakeCoordY[HEAD]) == FieldType.FOOD:
            eating = True
        elif field.getFields(self.__snakeCoordX[HEAD], self.__snakeCoordY[HEAD]) == FieldType.SNAKE:
            return 0
        elif field.getFields(self.__snakeCoordX[HEAD], self.__snakeCoordY[HEAD]) == FieldType.BORDER:
            return 0

        for i in range(1, len(self.__snakeCoordX)):
            if i % 2 == 1:
                tmpX_1 = self.__snakeCoordX[i]
                tmpY_1 = self.__snakeCoordY[i]
                self.__snakeCoordX[i] = tmpX_0
                self.__snakeCoordY[i] = tmpY_0

                if eating == True and i == len(self.__snakeCoordX) -1:
                    self.__snakeCoordX.append(tmpX_1)
                    self.__snakeCoordY.append(tmpY_1)
                    self.__length += 1

            elif i % 2 == 0:
                tmpX_0 = self.__snakeCoordX[i]
                tmpY_0 = self.__snakeCoordY[i]
                self.__snakeCoordX[i] = tmpX_1
                self.__snakeCoordY[i] = tmpY_1

                if eating == True and i == len(self.__snakeCoordX) -1:
                    self.__snakeCoordX.append(tmpX_0)
                    self.__snakeCoordY.append(tmpY_0)
                    self.__length += 1

        return 1
            

    
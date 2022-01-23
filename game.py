from turtle import Screen, screensize
from snake import Snake
from globalConstants import BoardColor, Direction, FieldType
from field import Field
import pygame


def main():
    global SCREEN, CLOCK
    screenSize = 510

    snake = Snake(4, 6, 8, "green", Direction.EAST)
    field = Field(15)

    pygame.init()

    SCREEN = pygame.display.set_mode(([screenSize, screenSize]))
    CLOCK = pygame.time.Clock()

    running = True
    field.setSnakeFields(snake)
    keyPressed = "none"

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        KEY_UP = pygame.key.get_pressed()[pygame.K_UP]
        KEY_DOWN = pygame.key.get_pressed()[pygame.K_DOWN]
        KEY_LEFT = pygame.key.get_pressed()[pygame.K_LEFT]
        KEY_RIGHT = pygame.key.get_pressed()[pygame.K_RIGHT]
    
        if KEY_RIGHT:
            keyPressed = "right"
            snake.setDirection(Direction.EAST)
        elif KEY_LEFT:
            snake.setDirection(Direction.WEST)
            keyPressed = "left"
        elif KEY_UP:
            snake.setDirection(Direction.NORTH)
            keyPressed = "up"
        elif KEY_DOWN:
            keyPressed = "down"
            snake.setDirection(Direction.SOUTH)

        snake.moveInDirection(snake.getDirection())
        print(snake.getDirection())
        print(keyPressed)
        field.setSnakeFields(snake)
        drawFields(screenSize, field)
        pygame.display.flip()
        CLOCK.tick(2)

    
def drawFields(screenSize, field):
    blockSize = int(screenSize / field.getSquareSize())

    fieldCountX = 0
    fieldCountY = 0
    for x in range(0, screenSize, blockSize):
        fieldCountY = 0
        for y in range(0, screenSize, blockSize):
            fieldType = field.fields[fieldCountY][fieldCountX]
            rect = pygame.Rect(x, y, blockSize, blockSize)
            if (fieldType == FieldType.BORDER):
                pygame.draw.rect(SCREEN, BoardColor.BLACK, rect)
            elif (fieldType == FieldType.EMPTY):
                pygame.draw.rect(SCREEN, BoardColor.WHITE, rect)
            elif (fieldType == FieldType.SNAKE):
                pygame.draw.rect(SCREEN, BoardColor.GREEN, rect)
            fieldCountY += 1

        fieldCountX += 1

    # print(field.fields)
    # print()

    # snake.moveInDirection(Direction.NORTH)

    # field.setSnakeFields(snake)

    # print(field.fields)
    # print()

    # i = 0
    # while i < 3:
    #     snake.moveInDirection(Direction.NORTH)
    #     field.setSnakeFields(snake)
    #     print(field.fields)
    #     print()
    #     i = i +1 

    # snake.moveInDirection(Direction.WEST)
    # field.setSnakeFields(snake)
    # print(field.fields)
    # print()

    # i = 0
    # while i < 3:
    #     snake.moveInDirection(Direction.SOUTH)
    #     field.setSnakeFields(snake)
    #     print(field.fields)
    #     print()
    #     i = i +1 

    # snake.moveInDirection(Direction.SOUTH, True)
    # field.setSnakeFields(snake)
    # print(field.fields)
    # print()

    # i = 0
    # while i < 5:
    #     snake.moveInDirection(Direction.EAST)
    #     field.setSnakeFields(snake)
    #     print(field.fields)
    #     print()
    #     i = i +1 


if __name__ == "__main__":
    main()
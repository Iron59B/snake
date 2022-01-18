from turtle import screensize
from snake import Snake
from globalConstants import Direction
from field import Field
import pygame


def main():
    screenSize = 500

    snake = Snake(4, 6, 8, "green", Direction.EAST)
    field = Field(15)

    pygame.init()


    screen = pygame.display.set_mode(([screenSize, screenSize]))
    running = True

    # while running:
    #     screen.fill(255)

    field.setSnakeFields(snake)

    print(field.fields)
    print()

    snake.moveInDirection(Direction.NORTH)

    field.setSnakeFields(snake)

    print(field.fields)
    print()

    i = 0
    while i < 3:
        snake.moveInDirection(Direction.NORTH)
        field.setSnakeFields(snake)
        print(field.fields)
        print()
        i = i +1 

    snake.moveInDirection(Direction.WEST)
    field.setSnakeFields(snake)
    print(field.fields)
    print()

    i = 0
    while i < 3:
        snake.moveInDirection(Direction.SOUTH)
        field.setSnakeFields(snake)
        print(field.fields)
        print()
        i = i +1 

    snake.moveInDirection(Direction.SOUTH, True)
    field.setSnakeFields(snake)
    print(field.fields)
    print()

    i = 0
    while i < 5:
        snake.moveInDirection(Direction.EAST)
        field.setSnakeFields(snake)
        print(field.fields)
        print()
        i = i +1 

#incomplete
# def drawFields(screenSize, field):
#     blockSize = screenSize / field.getSquareSize()

#     for x in range(0, screenSize, blockSize):
#         for y in range(0, screenSize, blockSize):
#             rect = pygame.Rect(x, y, blockSize, blockSize)
#             pygame.draw.rect(S)

if __name__ == "__main__":
    main()
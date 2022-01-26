from turtle import Screen, screensize
from snake import Snake
from globalConstants import BoardColor, Direction, FieldType
from field import Field
import pygame

def main():
    global SCREEN, CLOCK
    screenSize = 900

    snake = Snake(4, 6, 8, "green", Direction.EAST)
    field = Field(30)

    direction = snake.getDirection()

    pygame.init()

    SCREEN = pygame.display.set_mode(([screenSize, screenSize]))
    CLOCK = pygame.time.Clock()

    running = True
    score = 0
    field.spawnFood()

    previousSnakeLength = snake.getLength()

    while running:
        CLOCK.tick(10)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.getDirection() != Direction.WEST:
                    direction = Direction.EAST
                elif event.key == pygame.K_LEFT and snake.getDirection() != Direction.EAST:
                    direction = Direction.WEST
                elif event.key == pygame.K_UP and snake.getDirection() != Direction.SOUTH:
                    direction = Direction.NORTH
                elif event.key == pygame.K_DOWN and snake.getDirection() != Direction.NORTH:
                    direction = Direction.SOUTH
                    
        
        success = snake.moveInDirection(direction, field)
        
        if snake.getLength() > previousSnakeLength:
            previousSnakeLength = snake.getLength()
            score += 1
            field.spawnFood()
            
        if success:
            field.setSnakeFields(snake)
            drawFields(screenSize, field)
            pygame.display.flip()
        else:
            running = False
            f = open("score.txt", "a")
            f.write(str(score) + "\n")
            f.close()

    
def drawFields(screenSize, field):
    blockSize = int(screenSize / field.getSquareSize())

    fieldCountX = 0
    fieldCountY = 0
    for x in range(0, screenSize, blockSize):
        fieldCountY = 0
        for y in range(0, screenSize, blockSize):
            fieldType = field.getFields(fieldCountX, fieldCountY)
            rect = pygame.Rect(x, y, blockSize, blockSize)
            if (fieldType == FieldType.BORDER):
                pygame.draw.rect(SCREEN, BoardColor.BLACK, rect)
            elif (fieldType == FieldType.EMPTY):
                pygame.draw.rect(SCREEN, BoardColor.GRAY, rect)
            elif (fieldType == FieldType.SNAKE):
                pygame.draw.rect(SCREEN, BoardColor.DARKGREEN, rect)
            elif (fieldType == FieldType.FOOD):
                pygame.draw.rect(SCREEN, BoardColor.RED, rect,)
            fieldCountY += 1

        fieldCountX += 1


if __name__ == "__main__":
    main()

from snake import Snake
from globalConstants import Direction
from field import Field
import pygame


def main():
    snake = Snake(4, 6, 8, "green", Direction.EAST)
    field = Field(15)

    field.setSnakeFields(snake)

    print(field.fields)


if __name__ == "__main__":
    main()
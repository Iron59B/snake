from snake import Snake
from direction import Direction


def main():
    snake = Snake(3, 3, 4)
    print(snake.getHeadPosition_X())

    snake.moveHeadInDirection(Direction.RIGHT)
    print(snake.getHeadPosition_X())


if __name__ == "__main__":
    main()
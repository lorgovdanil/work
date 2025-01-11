from random import random
from project_snake.Snake import Segment


def create_apple(apple, apple_2, POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas):
    create = False
    while not create:
        x = random.randint(0, CELL_WEIGHT-1)
        y = random.randint(0, CELL_HEIGHT-1)
        if POLE[y][x] == 0:
            create = True
            POLE[y][x] = 2
            apple.append([x,y])
            apple_2.append(Segment(x * SEG_SIZE, y * SEG_SIZE, "red", 2, canvas, SEG_SIZE))
def delete_apple(x, y, apple, apple_2, canvas):
    for i in range(len(apple)):
        x_apple, y_apple = apple[i]
        if x_apple == x and y_apple == y:
            apple.pop(i)
            canvas.delete(apple_2[i].instance)
            apple_2.pop(i)
            break
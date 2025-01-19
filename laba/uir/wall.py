import random



def create_wall(POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas):
    # горизонтали
    for i in range(random.randint(1, 5)):
        a = random.randint(0, CELL_WEIGHT - 4)
        b = random.randint(1, CELL_HEIGHT - 2)
        for x in range(a, a+3):
            POLE[b][x] = 1
            canvas.create_rectangle(x*SEG_SIZE, b*SEG_SIZE,
                                    x*SEG_SIZE + SEG_SIZE, b*SEG_SIZE + SEG_SIZE,
                                    fill="brown")
    for i in range(random.randint(1, 5)):
        a = random.randint(0, CELL_WEIGHT - 6)
        b = random.randint(1, CELL_HEIGHT - 2)
        for x in range(a, a+5):
            POLE[b][x] = 1
            canvas.create_rectangle(x*SEG_SIZE, b*SEG_SIZE,
                                    x*SEG_SIZE + SEG_SIZE, b*SEG_SIZE + SEG_SIZE,
                                    fill="brown")
    # вертикали
    for i in range(random.randint(1, 5)):
        a = random.randint(0, CELL_WEIGHT - 1)
        b = random.randint(1, CELL_HEIGHT - 4)
        for x in range(b, b + 3):
            POLE[x][a] = 1
            canvas.create_rectangle(a * SEG_SIZE, x * SEG_SIZE,
                                    a * SEG_SIZE + SEG_SIZE, x * SEG_SIZE + SEG_SIZE,
                                    fill="brown")
    for i in range(random.randint(1, 5)):
        a = random.randint(0, CELL_WEIGHT - 1)
        b = random.randint(1, CELL_HEIGHT - 6)
        for x in range(b, b + 5):
            POLE[x][a] = 1
            canvas.create_rectangle(a * SEG_SIZE, x * SEG_SIZE,
                                    a * SEG_SIZE + SEG_SIZE, x * SEG_SIZE + SEG_SIZE,
                                    fill="brown")
import random

class TableHP:
    def __init__(self, name1, name2, canvas,CELL_WEIGHT, SEG_SIZE, font="Arial 10"):
        self.x = CELL_WEIGHT * SEG_SIZE // 2
        self.y = 30
        self.name1 = name1
        self.name2 = name2
        self.text = "{} : {}\n {} : {}".format(self.name1, self.name2, 3, 3)
        self.font = font
        self.color = "yellow"
        self.text_id = None
        self.text_id = canvas.create_text(self.x, self.y, text=self.text, font=self.font, fill=self.color)
    def update_text_hp(self, hp1, hp2, canvas):
        self.text = "{} : {}\n  {} : {}".format(self.name1, self.name2, hp1, hp2)
        canvas.itemconfigure(self.text_id, text=self.text)

class Timer:
    def __init__(self, times, canvas, CELL_WEIGHT, SEG_SIZE,  font = "Arial 10"):
        self.x = CELL_WEIGHT * SEG_SIZE // 2
        self.y = 30
        self.times = times
        self.text = "Time: {}".format(self.times)
        self.font = font
        self.canvas = canvas
        self.color = "yellow"
        self.text_id = None
        self.text_id = canvas.create_text(self.x, self.y, text=self.text, font=self.font, fill=self.color)
    def update_time(self):
        self.times -= 1
        self.text = "Time: {}".format(self.times)
        self.canvas.itemconfigure(self.text_id, text=self.text)

class Score:
    def __init__(self, name1, name2, canvas, font="Arial 10"):
        self.x = 70
        self.y = 30
        self.name1 = name1
        self.name2 = name2
        self.text = "{} : {}\n {} : {}".format(self.name1, self.name2, 0, 0)
        self.font = font
        self.color = "yellow"
        self.text_id = None
        self.text_id = canvas.create_text(self.x, self.y, text=self.text, font=self.font, fill=self.color)


    def update_text(self, score1, score2,  canvas):
        self.text = "{} : {}\n {} : {}".format(self.name1, self.name2, score1, score2)
        canvas.itemconfigure(self.text_id, text=self.text)
class Score2:
    def __init__(self, canvas, font="Arial 10"):
        self.x = 70
        self.y = 30
        self.text = "счёт: {}".format(0)
        self.font = font
        self.color = "yellow"
        self.text_id = None
        self.text_id = canvas.create_text(self.x, self.y, text=self.text, font=self.font, fill=self.color)


    def update_text2(self, score, canvas):
        self.text = "счёт: {}".format(score)
        canvas.itemconfigure(self.text_id, text=self.text)
class Segment(object):
    """ Сегмент змейки """

    def __init__(self, x, y, color, kind, canvas, SEG_SIZE):
        if kind == 1:
            self.instance = canvas.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill=color)
        elif kind == 2:
            self.instance = canvas.create_oval(x, y,
                                                    x + SEG_SIZE, y + SEG_SIZE,
                                                    fill=color)
class Snake:
    def __init__(self, x, y,CELL_WEIGHT,CELL_HEIGHT, color, name, up, down, left, right, canvas, POLE, SEG_SIZE):
        self.color = color
        self.name = name
        self.segments = []
        self.segments_2 = []
        self.x = x
        self.y = y
        self.CELL_WEIGHT = CELL_WEIGHT
        self.CELL_HEIGHT = CELL_HEIGHT
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.rez = 0
        self.direction = self.right
        self.hp = 3
        for i in range(3):
            self.segments.append([x + i, y])
            POLE[y][x+i] = 1
            self.segments_2.append(Segment((x+i) * SEG_SIZE, y * SEG_SIZE, color,1, canvas, SEG_SIZE))
    def add_segment(self, x, y, canvas, POLE, SEG_SIZE):

        POLE[y][x] = 1
        self.segments.append([x,y])
        self.segments_2.append(Segment(x * SEG_SIZE, y * SEG_SIZE, self.color, 1, canvas, SEG_SIZE))

    def next_step(self):
        head_x, head_y = self.segments[-1]
        if self.direction == self.right:
            head_x += 1
        elif self.direction ==  self.left:
            head_x -= 1
        elif self.direction == self.up:
            head_y -= 1
        elif self.direction == self.down:
            head_y += 1
        if 0 > head_x:
            head_x = self.CELL_WEIGHT - 1
        elif head_x >= self.CELL_WEIGHT:
            head_x = 0
        if 0 > head_y:
            head_y = self.CELL_HEIGHT - 1
        elif head_y >= self.CELL_HEIGHT:
            head_y = 0
        return [head_x, head_y]
    def change_POLE(self, POLE, x_1, y_1):
        self.segments.append([x_1, y_1])
        POLE[y_1][x_1] = 1
        POLE[self.segments[0][1]][self.segments[0][0]] = 0
        self.segments.pop(0)
    def change_canvas(self, canvas, x_1, y_1, SEG_SIZE):
        for index in range(len(self.segments_2) - 1):
            segment = self.segments_2[index].instance
            x1, y1, x2, y2 = canvas.coords(self.segments_2[index + 1].instance)
            canvas.coords(segment, x1, y1, x2, y2)
        canvas.coords(self.segments_2[-1].instance,
                      x_1 * SEG_SIZE, y_1 * SEG_SIZE,
                      x_1 * SEG_SIZE + SEG_SIZE, y_1 * SEG_SIZE + SEG_SIZE)

    def move(self, sp, canvas, POLE, SEG_SIZE):
        x_1, y_1 = sp
        self.change_POLE(POLE, x_1, y_1)
        self.change_canvas(canvas, x_1, y_1, SEG_SIZE)
    def change_direction(self, new_direction):
        """Изменяет направление движения змейки."""
        if new_direction in [self.up, self.down, self.left, self.right]:
              # Змейка не может двигаться в противоположном направлении
            if (self.direction == self.up and new_direction == self.down or
                self.direction == self.down and new_direction == self.up or
                self.direction == self.left and new_direction == self.right or
                self.direction == self.right and new_direction == self.left):
                   pass
            else:
                self.direction = new_direction
        else:
            raise ValueError("Недопустимое направление движения змейки.")
    def restart(self,x,y, POLE, canvas, SEG_SIZE):
        self.segments.append([x, y])
        POLE[y][x] = 1
        self.segments_2.append(Segment(x * SEG_SIZE, y * SEG_SIZE, self.color, 1, canvas, SEG_SIZE))
        self.direction = self.right
    def delete_snake(self, POLE, canvas):
        for segm in range(len(self.segments) - 1, -1, -1):
            x,y = self.segments[segm]
            POLE[y][x] = 0
            self.segments.pop(segm)
            canvas.delete(self.segments_2[segm].instance)
            self.segments_2.pop(segm)
    def delete_segments(self, POLE, canvas):
        n = len(self.segments) * 2 // 3
        for i in range(n):
            x,y = self.segments[0]
            POLE[y][x] = 0
            self.segments.pop(0)
            canvas.delete(self.segments_2[0].instance)
            self.segments_2.pop(0)
    def revival (self, POLE, canvas, SEG_SIZE, apple, apple_2):
        self.delete_snake(POLE, canvas)
        flag = True
        for i in range(3):
            if POLE[self.y][self.x + i] == 0:
                self.restart(self.x + i, self.y, POLE, canvas, SEG_SIZE)
            elif POLE[self.y][self.x + i] == 1:
                self.delete_snake(POLE, canvas)
                flag = False
            elif POLE[self.y][self.x + i] == 2:
                delete_apple(self.x + i, self.y, apple, apple_2, canvas)
                self.restart(self.x + i, self.y, POLE, canvas, SEG_SIZE)
        return flag



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
def create_mega_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas):
    create = False
    while not create:
        a = random.randint(1, CELL_WEIGHT - 2)
        b = random.randint(1, CELL_HEIGHT - 2)
        if POLE[b][a] == 0:
            create = True
            POLE[b][a] = 5
            MEGA_APPLE = canvas.create_oval(a * SEG_SIZE, b * SEG_SIZE,
                                  a*SEG_SIZE + SEG_SIZE, b*SEG_SIZE + SEG_SIZE,
                                  fill="darkorchid4")
    return MEGA_APPLE
def delete_mega_apple(MEGA_APPLE, canvas):
    canvas.delete(MEGA_APPLE)
def create_black_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas):
    create = False
    while not create:
        a = random.randint(1, CELL_WEIGHT - 2)
        b = random.randint(1, CELL_HEIGHT - 2)
        if POLE[b][a] == 0:
            create = True
            POLE[b][a] = 6
            MEGA_APPLE = canvas.create_oval(a * SEG_SIZE, b * SEG_SIZE,
                                  a*SEG_SIZE + SEG_SIZE, b*SEG_SIZE + SEG_SIZE,
                                  fill="black")
    return MEGA_APPLE
def delete_black_apple(BLACK_APPLE, canvas):
    canvas.delete(BLACK_APPLE)

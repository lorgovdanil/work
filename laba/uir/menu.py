import tkinter as tk
from tkinter import ttk


from tkinter import Canvas

from project_snake.Snake import Snake, create_apple, delete_apple, Score, delete_mega_apple, create_mega_apple, \
    delete_black_apple, create_black_apple, Score2
from project_snake.game_file_rezult import update_data, show_rezult
from project_snake.wall import create_wall



CELL_WEIGHT = 30
CELL_HEIGHT = 30
SEG_SIZE = 20
POLE = [[0 for _ in range(CELL_WEIGHT)]for _ in range(CELL_HEIGHT)]
apple = []
apple_2 = []
IN_GAME = True
count = 0
time = 60000
speed = 100
destroy_mega_apple = True
destroy_black_apple = True


sn1_IN_GAME = True
sn2_IN_GAME = True
def end_game(t, v1, v2 ):
    canvas.destroy()
    menu.restart()
    update_data(t, v1, v2)
def create_game_dual(root):
    def move(sn1, sn2, canvas, apple, apple_2):
        flag = True
        x, y = sn1.next_step()
        if POLE[y][x] == 0:
            sn1.move([x,y], canvas, POLE, SEG_SIZE)
        elif POLE[y][x] == 1:
            flag = sn1.revival(POLE, canvas, SEG_SIZE, apple, apple_2)
            sn2.rez += 3
        elif POLE[y][x] == 2:
            sn1.rez += 1
            sn1.add_segment(x,y,canvas, POLE, SEG_SIZE)
            delete_apple(x,y,apple,apple_2, canvas)
        elif POLE[y][x] == 5:
            global MEGA_APPLE
            global destroy_mega_apple
            destroy_mega_apple = True
            delete_mega_apple(MEGA_APPLE, canvas)
            POLE[y][x] = 1
            sn1.rez += 15
            sn1.add_segment(x, y, canvas, POLE, SEG_SIZE)
        elif POLE[y][x] == 6:
            global BLACK_APPLE
            global destroy_black_apple
            destroy_black_apple = True
            delete_black_apple(BLACK_APPLE, canvas)
            POLE[y][x] = 1
            sn1.rez -= 5
            sn1.add_segment(x, y, canvas, POLE, SEG_SIZE)
            sn1.delete_segments(POLE, canvas)
        return flag

    def main1():
        """ Моделируем игровой процесс """
        global count
        global apple
        global apple_2
        global IN_GAME
        global sn1_IN_GAME
        global sn2_IN_GAME
        global MEGA_APPLE
        global BLACK_APPLE
        global canvas
        global root1
        global destroy_mega_apple
        global destroy_black_apple
        if IN_GAME:
            count += 1
            if sn1_IN_GAME:
                sn1_IN_GAME = move(snake_1, snake_2, canvas, apple, apple_2)
            else:
                sn1_IN_GAME = snake_1.revival(POLE, canvas, SEG_SIZE, apple, apple_2)
            if sn2_IN_GAME:
                sn2_IN_GAME = move(snake_2, snake_1, canvas, apple, apple_2)
            else:
                sn2_IN_GAME = snake_2.revival(POLE, canvas, SEG_SIZE, apple, apple_2)
            score.update_text(snake_1.rez, snake_2.rez, canvas)
            if count % 10 == 0 and len(apple) < 50:
                create_apple(apple, apple_2, POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
            if count % 50 == 0 and destroy_mega_apple:
                destroy_mega_apple = False
                MEGA_APPLE = create_mega_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)
            if count % 50 - 10== 0 and destroy_black_apple:
                destroy_black_apple = False
                BLACK_APPLE = create_black_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)

            if count % time == 0:
                IN_GAME = False

            root1.after(speed,main1)
        else:
            end_game(1, snake_1.rez, snake_2.rez)

    def snake_key_press(event):
        """Функция-обработчик нажатий клавиш для змейки"""
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            snake_2.change_direction(event.keysym)
        elif event.keysym in ["w", "s", "a", "d"]:
            snake_1.change_direction(event.keysym)
        else:
            pass

    def create_snake1():
        return Snake(0,0,CELL_WEIGHT,CELL_HEIGHT,"red", "Амёба", "w", "s", "a", "d", canvas, POLE, SEG_SIZE)
    def create_snake2():
        return Snake(0,CELL_HEIGHT - 1,CELL_WEIGHT,CELL_HEIGHT, "green", "Агуша", "Up", "Down", "Left", "Right", canvas, POLE, SEG_SIZE)
    def start_game(canvas, root1):
        global snake_1
        global snake_2
        global score
        snake_1 = create_snake1()
        snake_2 = create_snake2()
        score = Score(snake_1.name, snake_2.name, canvas)
        canvas.bind("<KeyPress>", snake_key_press)
        create_wall(POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
        main1()
    def update():
        global POLE
        global apple
        global apple_2
        global IN_GAME
        global count
        global destroy_mega_apple
        global destroy_black_apple
        global sn1_IN_GAME
        global sn2_IN_GAME
        global speed

        POLE = [[0 for _ in range(CELL_WEIGHT)] for _ in range(CELL_HEIGHT)]
        apple = []
        apple_2 = []
        IN_GAME = True
        count = 0
        speed = 100

        destroy_mega_apple = True
        destroy_black_apple = True

        sn1_IN_GAME = True
        sn2_IN_GAME = True

    global canvas
    canvas = Canvas(root, width=CELL_WEIGHT*SEG_SIZE, height=CELL_HEIGHT*SEG_SIZE, bg="#111100")
    global root1
    root1 = root
    update()
    canvas.grid()
    canvas.focus_set()
    start_game(canvas, root1)

def create_single_game(root):
    def move_snake(sn1, canvas, apple, apple_2):
        x, y = sn1.next_step()
        if POLE[y][x] == 0:
            sn1.move([x,y], canvas, POLE, SEG_SIZE)
        elif POLE[y][x] == 1:
            global rezult
            rezult = max(rezult, sn1.rez)
            sn1.rez = 0
            sn1.revival(POLE, canvas, SEG_SIZE, apple, apple_2)
        elif POLE[y][x] == 2:
            sn1.rez += 1
            sn1.add_segment(x,y,canvas, POLE, SEG_SIZE)
            delete_apple(x,y,apple,apple_2, canvas)
            global speed
            speed = 100
        elif POLE[y][x] == 5:
            global MEGA_APPLE
            global destroy_mega_apple
            destroy_mega_apple = True
            delete_mega_apple(MEGA_APPLE, canvas)
            POLE[y][x] = 1
            sn1.rez += 15
            sn1.add_segment(x, y, canvas, POLE, SEG_SIZE)
        elif POLE[y][x] == 6:
            global BLACK_APPLE
            global destroy_black_apple
            destroy_black_apple = True
            delete_black_apple(BLACK_APPLE, canvas)
            POLE[y][x] = 1
            sn1.rez -= 5
            sn1.add_segment(x, y, canvas, POLE, SEG_SIZE)
            sn1.delete_segments(POLE, canvas)

    def main_single():
        """ Моделируем игровой процесс """
        global count
        global apple
        global apple_2
        global IN_GAME
        global sn1_IN_GAME
        global sn2_IN_GAME
        global MEGA_APPLE
        global BLACK_APPLE
        global canvas
        global root1
        global rezult
        global score
        global destroy_mega_apple
        global destroy_black_apple
        global speed
        if IN_GAME:
            count += 1

            move_snake(snake_1, canvas, apple, apple_2)
            score.update_text2(snake_1.rez, canvas)
            if count % 5 == 0 and len(apple) < 90:
                create_apple(apple, apple_2, POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
            if count % 50 == 0 and destroy_mega_apple:
                destroy_mega_apple = False
                MEGA_APPLE = create_mega_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)
            if count % 250 - 10== 0 and destroy_black_apple:
                destroy_black_apple = False
                BLACK_APPLE = create_black_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)
            if count % time == 0:
                IN_GAME = False

            if speed > 30:
                speed = 100 - len(snake_1.segments) * 2
            root1.after(speed,main_single)
        else:
            rezult = max(rezult, snake_1.rez)
            end_game(2, rezult, 0)

    def snake_key_press_single(event):
        """Функция-обработчик нажатий клавиш для змейки"""
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            snake_1.change_direction(event.keysym)
        else:
            pass

    def create_snake():
        return Snake(0,0,CELL_WEIGHT,CELL_HEIGHT,"red", "Амёба", "Up", "Down", "Left", "Right", canvas, POLE, SEG_SIZE)

    def start_single_game(canvas, root1):
        global snake_1
        global rezult
        global score
        rezult = 0
        snake_1 = create_snake()
        score = Score2(canvas)
        canvas.bind("<KeyPress>", snake_key_press_single)
        create_wall(POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
        main_single()
    def update():
        global POLE
        global apple
        global apple_2
        global IN_GAME
        global count
        global destroy_mega_apple
        global destroy_black_apple
        global sn1_IN_GAME
        global sn2_IN_GAME
        global speed

        POLE = [[0 for _ in range(CELL_WEIGHT)] for _ in range(CELL_HEIGHT)]
        apple = []
        apple_2 = []
        IN_GAME = True
        count = 0
        speed = 100

        destroy_mega_apple = True
        destroy_black_apple = True

        sn1_IN_GAME = True
        sn2_IN_GAME = True

    global canvas
    canvas = Canvas(root, width=CELL_WEIGHT*SEG_SIZE, height=CELL_HEIGHT*SEG_SIZE, bg="#111100")
    global root1
    root1 = root
    update()
    canvas.grid()
    canvas.focus_set()
    start_single_game(canvas, root1)
def create_survival_game(root):
    def move_survival(sn1, canvas, apple, apple_2):
        flag = True
        x, y = sn1.next_step()
        if POLE[y][x] == 0:
            sn1.move([x, y], canvas, POLE, SEG_SIZE)
        elif POLE[y][x] == 1:
            flag = False
        elif POLE[y][x] == 2:
            sn1.rez += 1
            sn1.add_segment(x, y, canvas, POLE, SEG_SIZE)
            delete_apple(x, y, apple, apple_2, canvas)
        elif POLE[y][x] == 5:
            global MEGA_APPLE
            global destroy_mega_apple
            destroy_mega_apple = True
            delete_mega_apple(MEGA_APPLE, canvas)
            POLE[y][x] = 1
            sn1.rez += 15
            sn1.add_segment(x, y, canvas, POLE, SEG_SIZE)
        elif POLE[y][x] == 6:
            global BLACK_APPLE
            global destroy_black_apple
            destroy_black_apple = True
            delete_black_apple(BLACK_APPLE, canvas)
            POLE[y][x] = 1
            sn1.rez -= 5
            sn1.add_segment(x, y, canvas, POLE, SEG_SIZE)
            sn1.delete_segments(POLE, canvas)
        return flag

    def main_survival():
        """ Моделируем игровой процесс """
        global count
        global apple
        global apple_2
        global IN_GAME
        global sn1_IN_GAME
        global sn2_IN_GAME
        global MEGA_APPLE
        global BLACK_APPLE
        global canvas
        global root1
        global destroy_mega_apple
        global destroy_black_apple
        global rezult_game
        if IN_GAME:
            count += 1
            sn1_IN_GAME = move_survival(snake_1, canvas, apple, apple_2)
            sn2_IN_GAME = move_survival(snake_2, canvas, apple, apple_2)
            if not sn1_IN_GAME and not sn2_IN_GAME:
                rezult_game = 0.5
            elif not sn1_IN_GAME:
                rezult_game = 0
            else:
                rezult_game = 1
            if count % 10 == 0 and len(apple) < 50:
                create_apple(apple, apple_2, POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
            if count % 50 == 0 and destroy_mega_apple:
                destroy_mega_apple = False
                MEGA_APPLE = create_mega_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)
            if count % 50 - 10== 0 and destroy_black_apple:
                destroy_black_apple = False
                BLACK_APPLE = create_black_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)
            if not (sn1_IN_GAME and sn2_IN_GAME):
                IN_GAME = False

            root1.after(100,main_survival)
        else:



            end_game(3, rezult_game, 1 - rezult_game)

    def snake_key_press_survival(event):
        """Функция-обработчик нажатий клавиш для змейки"""
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            snake_2.change_direction(event.keysym)
        elif event.keysym in ["w", "s", "a", "d"]:
            snake_1.change_direction(event.keysym)
        else:
            pass

    def create_snake1():
        return Snake(0, 0, CELL_WEIGHT, CELL_HEIGHT, "red", "Амёба", "w", "s", "a", "d", canvas, POLE, SEG_SIZE)

    def create_snake2():
        return Snake(0, CELL_HEIGHT - 1, CELL_WEIGHT, CELL_HEIGHT, "green", "Агуша", "Up", "Down", "Left", "Right",
                     canvas, POLE, SEG_SIZE)
    def start_survival_game(canvas, root1):
        global snake_1
        global snake_2
        snake_1 = create_snake1()
        snake_2 = create_snake2()
        canvas.bind("<KeyPress>", snake_key_press_survival)
        create_wall(POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
        main_survival()
    def update():
        global POLE
        global apple
        global apple_2
        global IN_GAME
        global count
        global destroy_mega_apple
        global destroy_black_apple
        global sn1_IN_GAME
        global sn2_IN_GAME
        global speed
        POLE = [[0 for _ in range(CELL_WEIGHT)] for _ in range(CELL_HEIGHT)]
        apple = []
        apple_2 = []
        IN_GAME = True
        count = 0
        speed = 100
        destroy_mega_apple = True
        destroy_black_apple = True

        sn1_IN_GAME = True
        sn2_IN_GAME = True

    global canvas
    canvas = Canvas(root, width=CELL_WEIGHT*SEG_SIZE, height=CELL_HEIGHT*SEG_SIZE, bg="#111100")
    global root1
    root1 = root
    update()
    canvas.grid()
    canvas.focus_set()
    start_survival_game(canvas, root1)
class MenuWindow:
    def __init__(self, root):
        self.menu_frame = None
        self.root = root
        self.root.title("Snake Game Menu")
        self.root.geometry("600x600")  # Увеличиваем размер окна
        self.root.configure(bg="green")  # Устанавливаем цвет фона окна

        self.current_view = "menu"
        self.create_menu_widgets()
        self.root.bind("<Return>", self.handle_enter)

    def create_menu_widgets(self):
        """Создаем виджеты для меню."""
        self.menu_frame = ttk.Frame(self.root, padding=20, style="Menu.TFrame")  # Стиль для рамок меню
        self.menu_frame.pack(expand=True, pady=50) # Увеличиваем отступ сверху

        # Стили для кнопок (стили)
        button_style = ttk.Style()
        button_style.configure("Menu.TButton", font=("Arial", 14), padding=10, width=40,
                                background="#444444", foreground="red") # Фон кнопок, шрифт, ширина

        # Кнопка для игры в дуэли
        duel_game_button = ttk.Button(self.menu_frame, text="Snake Duel", command=self.start_duel_game, style="Menu.TButton", cursor="spider")
        duel_game_button.pack(pady=10)

        # Кнопка для игры на одного игрока
        single_game_button = ttk.Button(self.menu_frame, text="Single Snake", command=self.start_single_game, style="Menu.TButton")
        single_game_button.pack(pady=10)
        # Кнопка для выживания
        survival_game_button = ttk.Button(self.menu_frame, text="Survival", command=self.start_survival_game, style="Menu.TButton")
        survival_game_button.pack(pady=10)

        # Кнопка для просмотра результатов
        scores_button = ttk.Button(self.menu_frame, text="Scores", command=self.show_scores, style="Menu.TButton")
        scores_button.pack(pady=10)

        setting_button = ttk.Button(self.menu_frame, text="Setting", command=self.setting, style="Menu.TButton")
        setting_button.pack(pady=10)
    def setting(self):
        pass


    def clear_window(self):
        """Очищает текущее содержимое окна."""
        for widget in self.root.winfo_children():
            widget.destroy()
    def start_duel_game(self):
        """Запускает игру в дуэли."""

        self.clear_window()
        self.current_view = "game_duel"
        create_game_dual(self.root)

    def start_single_game(self):
        """Запускает игру на одного игрока."""
        self.clear_window()
        self.current_view = "game_single"
        create_single_game(self.root)
    def start_survival_game(self):
        """Запускает игру на выживание."""
        self.clear_window()
        self.current_view = "game_survival"
        create_survival_game(self.root)
    def show_scores(self):
        """Очищает экран и показывает результаты."""
        self.clear_window()
        self.current_view = "scores"
        # Здесь будет код для отображения результатов
        ttk.Label(self.root, text="Displaying Scores!",width=20, font=("Arial", 20)).pack()
        ttk.Label(self.root, text="Dual Game ",width=20,font=("Arial", 20)).pack()
        s = show_rezult(1)
        ttk.Label(self.root, text=s,width=30, font=("Arial", 15)).pack()
        ttk.Label(self.root, text="Single game: ",width=20, font=("Arial", 20)).pack()
        s = show_rezult(2)
        ttk.Label(self.root, text=s,width=30, font=("Arial", 15)).pack()
        ttk.Label(self.root, text="Survival game: ",width=20, font=("Arial", 20)).pack()
        s = show_rezult(3)
        ttk.Label(self.root, text=s,width=30, font=("Arial", 15)).pack()

    def restart(self):
        self.clear_window()
        self.create_menu_widgets()
        self.current_view = "menu"
    def handle_enter(self, event):
        """Обрабатывает нажатие Enter и возвращает в меню."""
        if self.current_view != "menu":
             self.clear_window()
             self.create_menu_widgets()
             self.current_view = "menu"

def main():
    global menu
    rooot = tk.Tk()
    menu = MenuWindow(rooot)
    rooot.mainloop()
if __name__ == "__main__":
    main()
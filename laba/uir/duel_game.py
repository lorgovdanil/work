


import tkinter as tk
from tkinter import ttk


from tkinter import Canvas
from project_snake.Snake import Snake, create_apple, delete_apple, Score, delete_mega_apple, create_mega_apple
from project_snake.wall import create_wall



CELL_WEIGHT = 30
CELL_HEIGHT = 30
SEG_SIZE = 20
POLE = [[0 for _ in range(CELL_WEIGHT)]for _ in range(CELL_HEIGHT)]
apple = []
apple_2 = []
IN_GAME = True
count = 0

destroy_mega_apple = True
destroy_black_apple = True


sn1_IN_GAME = True
sn2_IN_GAME = True

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
    global canvas
    global root1
    global destroy_mega_apple
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
        if count % 600 == 0:
            IN_GAME = False

        root1.after(100,main1)
    else:

        print(123)

        canvas.destroy()
        menu.restart()

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

    POLE = [[0 for _ in range(CELL_WEIGHT)] for _ in range(CELL_HEIGHT)]
    apple = []
    apple_2 = []
    IN_GAME = True
    count = 0

    destroy_mega_apple = True
    destroy_black_apple = True

    sn1_IN_GAME = True
    sn2_IN_GAME = True
def create_game_dual(root):
    global canvas
    canvas = Canvas(root, width=CELL_WEIGHT*SEG_SIZE, height=CELL_HEIGHT*SEG_SIZE, bg="#111100")
    global root1
    root1 = root
    update()
    canvas.grid()
    canvas.focus_set()

    start_game(canvas, root1)
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
        #self.clear_window()
        self.current_view = "game_single"

        ttk.Label(self.root, text="Single Game is starting...").pack() # Заменить на запуск Single game
    def start_survival_game(self):
        """Запускает игру на выживание."""
        self.clear_window()
        self.current_view = "game_survival"

        ttk.Label(self.root, text="Survival is starting...").pack()  # Заменить на запуск Survival game
    def show_scores(self):
        """Очищает экран и показывает результаты."""
        self.clear_window()
        self.current_view = "scores"
        # Здесь будет код для отображения результатов
        ttk.Label(self.root, text="Displaying Scores!").pack()
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

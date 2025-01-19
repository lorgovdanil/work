import tkinter as tk
from tkinter import ttk, colorchooser

from tkinter import Canvas

from project_snake.Snake import Snake, create_apple, delete_apple, Score, delete_mega_apple, create_mega_apple, \
    delete_black_apple, create_black_apple, Score2, Timer, TableHP
from project_snake.game_file_rezult import update_data, show_rezult, write_file
from project_snake.setting_file import write_setting_file, read_setting_file
from project_snake.wall import create_wall

CELL_WEIGHT = 30
CELL_HEIGHT = 30
SEG_SIZE = 20
POLE = [[0 for _ in range(CELL_WEIGHT)]for _ in range(CELL_HEIGHT)]
apple = []
apple_2 = []

IN_GAME = True
count = 0
speed = 100
destroy_mega_apple = True
destroy_black_apple = True



sn1_IN_GAME = True
sn2_IN_GAME = True


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
                sn2_IN_GAME = move(snake_2, snake_1, canvas, apple, apple_2 )
            else:
                sn2_IN_GAME = snake_2.revival(POLE, canvas, SEG_SIZE, apple, apple_2)
            score.update_text(snake_1.rez, snake_2.rez, canvas)
            if count % 10 == 0 and len(apple) < 30:
                create_apple(apple, apple_2, POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
            if count % 50 == 0 and destroy_mega_apple:
                destroy_mega_apple = False
                MEGA_APPLE = create_mega_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)
            if count % 50 - 10== 0 and destroy_black_apple:
                destroy_black_apple = False
                BLACK_APPLE = create_black_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)
            if count % 10 == 0:
                timer.update_time()
            if count == time:
                IN_GAME = False

            root1.after(speed,main1)
        else:
            menu.end_game(1, snake_1.rez, snake_2.rez)

    def snake_key_press(event):
        """Функция-обработчик нажатий клавиш для змейки"""
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            snake_2.change_direction(event.keysym)
        elif event.keysym in ["w", "s", "a", "d"]:
            snake_1.change_direction(event.keysym)
        elif event.char in ["ц", "ы", "ф", "в"]:
            if event.char == "ц":
                snake_1.change_direction("w")
            elif event.char == "ы":
                snake_1.change_direction("s")
            elif event.char == "ф":
                snake_1.change_direction("a")
            elif event.char == "в":
                snake_1.change_direction("d")
        else:
            pass

    def create_snake1(color1, name1):
        return Snake(0,0,CELL_WEIGHT,CELL_HEIGHT,color1, name1, "w", "s", "a", "d", canvas, POLE, SEG_SIZE)
    def create_snake2(color2, name2):
        return Snake(0,CELL_HEIGHT - 1,CELL_WEIGHT,CELL_HEIGHT, color2, name2, "Up", "Down", "Left", "Right", canvas, POLE, SEG_SIZE)
    def start_game(canvas, root1):
        global snake_1
        global snake_2
        global score
        global timer
        sp = read_setting_file()
        snake_1 = create_snake1(sp[0], sp[3])
        snake_2 = create_snake2(sp[1],sp[4])

        canvas.bind("<KeyPress>", snake_key_press)

        create_wall(POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)

        score = Score(snake_1.name, snake_2.name, canvas)
        timer = Timer(time//10, canvas, CELL_WEIGHT, SEG_SIZE)
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
        global time
        sp = read_setting_file()
        time = int(sp[-1])
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
            if len(snake_1.segments) < 5:
                speed = 100
            elif 5 <= len(snake_1.segments) < 12:
                speed = 80
            elif 12 <= len(snake_1.segments) < 17:
                speed = 70
            elif 17 <= len(snake_1.segments) < 21:
                speed = 60
            else:
                speed = 50
            root1.after(speed,main_single)
        else:
            rezult = max(rezult, snake_1.rez)
            menu.end_game(2, rezult, 0)

    def snake_key_press_single(event):
        """Функция-обработчик нажатий клавиш для змейки"""
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            snake_1.change_direction(event.keysym)
        else:
            pass

    def create_snake(color, name):
        return Snake(0,0,CELL_WEIGHT,CELL_HEIGHT,color, name, "Up", "Down", "Left", "Right", canvas, POLE, SEG_SIZE)

    def start_single_game(canvas, root1):
        global snake_1
        global rezult
        global score
        sp = read_setting_file()
        snake_1 = create_snake(sp[2], sp[5])
        rezult = 0

        canvas.bind("<KeyPress>", snake_key_press_single)
        create_wall(POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
        score = Score2(canvas)

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
        global time
        sp = read_setting_file()
        time = int(sp[-1])
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
            sn1.hp -= 1
            if sn1.hp == 0:
                flag = False
            if not sn1.revival(POLE, canvas, SEG_SIZE, apple, apple_2):
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
            sn1.hp += 1
            sn1.add_segment(x, y, canvas, POLE, SEG_SIZE)
        elif POLE[y][x] == 6:
            global BLACK_APPLE
            global destroy_black_apple
            destroy_black_apple = True
            delete_black_apple(BLACK_APPLE, canvas)
            POLE[y][x] = 1
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
        global speed_game_survival
        if IN_GAME:
            count += 1

            sn1_IN_GAME = move_survival(snake_1, canvas, apple, apple_2)
            sn2_IN_GAME = move_survival(snake_2, canvas, apple, apple_2)

            table_hp.update_text_hp(snake_1.hp, snake_2.hp, canvas)
            if not sn1_IN_GAME and not sn2_IN_GAME:
                rezult_game = 0.5
            elif not sn1_IN_GAME:
                rezult_game = 0
            else:
                rezult_game = 1
            if count % 10 == 0 and len(apple) < 50:
                create_apple(apple, apple_2, POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
            if count % 250 == 0 and destroy_mega_apple:
                destroy_mega_apple = False
                MEGA_APPLE = create_mega_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)
            if count % 50 - 10== 0 and destroy_black_apple:
                destroy_black_apple = False
                BLACK_APPLE = create_black_apple(CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, POLE, canvas)
            if not (sn1_IN_GAME and sn2_IN_GAME):
                IN_GAME = False
            if count % 750 == 0:
                speed_game_survival = int(speed_game_survival * 4 / 5)
            root1.after(speed_game_survival,main_survival)
        else:
            menu.end_game(3, rezult_game, 1 - rezult_game)

    def snake_key_press_survival(event):
        """Функция-обработчик нажатий клавиш для змейки"""
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            snake_2.change_direction(event.keysym)
        elif event.keysym in ["w", "s", "a", "d"]:
            snake_1.change_direction(event.keysym)
        elif event.char in ["ц", "ы", "ф", "в"]:
            if event.char == "ц":
                snake_1.change_direction("w")
            elif event.char == "ы":
                snake_1.change_direction("s")
            elif event.char == "ф":
                snake_1.change_direction("a")
            elif event.char == "в":
                snake_1.change_direction("d")
        else:
            pass

    def create_snake1(color1,name1):
        return Snake(0, 0, CELL_WEIGHT, CELL_HEIGHT, color1, name1, "w", "s", "a", "d", canvas, POLE, SEG_SIZE)

    def create_snake2(color2,name2):
        return Snake(0, CELL_HEIGHT - 1, CELL_WEIGHT, CELL_HEIGHT, color2, name2, "Up", "Down", "Left", "Right",
                     canvas, POLE, SEG_SIZE)
    def start_survival_game(canvas, root1):
        global snake_1
        global snake_2
        global table_hp
        sp = read_setting_file()
        snake_1 = create_snake1(sp[0], sp[3])
        snake_2 = create_snake2(sp[1], sp[4])
        canvas.bind("<KeyPress>", snake_key_press_survival)
        create_wall(POLE, CELL_WEIGHT, CELL_HEIGHT, SEG_SIZE, canvas)
        table_hp = TableHP(snake_1.name, snake_2.name, canvas, CELL_WEIGHT, SEG_SIZE)
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
        global speed_game_survival
        global time
        sp = read_setting_file()
        time = int(sp[-1])
        POLE = [[0 for _ in range(CELL_WEIGHT)] for _ in range(CELL_HEIGHT)]
        apple = []
        apple_2 = []
        IN_GAME = True
        count = 0
        speed_game_survival = 100
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
        self.root.title("Snake Game")
        self.root.geometry("600x600+500+50")  # Увеличиваем размер окна
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
        duel_game_button = ttk.Button(self.menu_frame, text="Дуэль", command=self.start_duel_game, style="Menu.TButton", cursor="spider")
        duel_game_button.pack(pady=10)

        # Кнопка для игры на одного игрока
        single_game_button = ttk.Button(self.menu_frame, text="Одна змейка", command=self.start_single_game, style="Menu.TButton")
        single_game_button.pack(pady=10)
        # Кнопка для выживания
        survival_game_button = ttk.Button(self.menu_frame, text="Выживание", command=self.start_survival_game, style="Menu.TButton")
        survival_game_button.pack(pady=10)

        # Кнопка для просмотра результатов
        scores_button = ttk.Button(self.menu_frame, text="Результаты", command=self.show_scores, style="Menu.TButton")
        scores_button.pack(pady=10)

        setting_button = ttk.Button(self.menu_frame, text="Настройки", command=self.setting, style="Menu.TButton")
        setting_button.pack(pady=10)
    def setting(self):
        setup_window = tk.Toplevel(self.root)
        setup_window.geometry("300x300")
        setup_window.title("Настройка игры")

        def choose_color1():
            """Выбирает цвет из диалогового окна."""
            color = colorchooser.askcolor()[1]
            color_label.config(bg=color)
            write_setting_file(0,color)
        def choose_color2():
            """Выбирает цвет из диалогового окна."""
            color = colorchooser.askcolor()[1]
            color_label.config(bg=color)
            write_setting_file(1, color)
        def choose_color3():
            """Выбирает цвет из диалогового окна."""
            color = colorchooser.askcolor()[1]
            color_label.config(bg=color)
            write_setting_file(2, color)
        def back_to_menu():
            if snake_name1.get() == "":
                pass
            else:
                write_setting_file(3, snake_name1.get())
            if snake_name2.get() == "":
                pass
            else:
                write_setting_file(4, snake_name2.get())
            if time_entry.get() == "":
                pass
            else:
                if time_entry.get().isdigit():
                    write_setting_file(6, str(int(time_entry.get()) * 10))
            setup_window.destroy()

        setup_window.resizable(width=False, height=False)
        # Создание виджетов в окне настроек
        color_label = tk.Label(setup_window, text="Цвет змейки:", width=21, height=2, bg="white")
        color_label.pack()
        color_button1 = ttk.Button(setup_window, text="Выбрать для змейки 1", width=25, command=choose_color1)
        color_button1.pack()
        color_button2 = ttk.Button(setup_window, text="Выбрать для змейки 2",width=25, command=choose_color2)
        color_button2.pack()
        color_button3 = ttk.Button(setup_window, text="Выбрать для одной змейки", width=25, command=choose_color3)
        color_button3.pack()

        snake_name_label = ttk.Label(setup_window, text="Имя змейки 1:")
        snake_name_label.pack()
        snake_name1 = tk.Entry(setup_window, width=25)
        snake_name1.pack()

        snake_name_label = ttk.Label(setup_window, text="Имя змейки 2:")
        snake_name_label.pack()
        snake_name2 = tk.Entry(setup_window, width=25)
        snake_name2.pack()

        time_label = ttk.Label(setup_window, text="Время в секундах: ")
        time_label.pack()
        time_entry = tk.Entry(setup_window, width=25)
        time_entry.pack()

        back_button = ttk.Button(setup_window, text="Назад", command=back_to_menu)
        back_button.pack(pady = 10)
        self.root.mainloop()



    def clear_window(self):
        """Очищает текущее содержимое окна."""
        for widget in self.root.winfo_children():
            widget.destroy()
    def start_duel_game(self):
        """Запускает игру в дуэли."""
        self.clear_window()
        self.current_view = "game_duel"
        create_game_dual(self.root)
    def end_game(self, t, v1, v2):
        canvas.destroy()
        update_data(t, v1, v2)
        sp = read_setting_file()
        if t == 1:
            if v1 > v2:
                victory = f"ПОБЕДИЛ {sp[3]}!!!"
            elif v1 < v2:
                victory = f"ПОБЕДИЛ {sp[4]}!!!"
            else:
                victory = "НИЧЬЯ"
            ttk.Label(self.root, text=f"Результаты:\n{victory}\n{sp[3]} набрал {v1} очков,\n{sp[4]} набрал {v2} очков", width=30, font=("Arial", 20)).pack()
        elif t == 2:
            ttk.Label(self.root, text=f"Результаты:\nВы набрали {v1} очков", width=30, font=("Arial", 20)).pack()
        elif t == 3:
            if v1 > v2:
                victory = f"ПОБЕДИЛ {sp[3]}!!!"
            elif v1 < v2:
                victory = f"ПОБЕДИЛ {sp[4]}!!!"
            else:
                victory = "НИЧЬЯ"
            ttk.Label(self.root, text=f"Результаты:\n{victory}", width=30, font=("Arial", 20)).pack()
        # menu.restart()
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

    def delete_rezult(self):
        for i in range(1, 4):
            write_file(i, "")
        self.show_scores()

    def show_scores(self):
        """Очищает экран и показывает результаты."""
        button_style = ttk.Style()
        button_style.configure("Menu.TButton", font=("Arial", 14), padding=10, width=40,
                               background="#444444", foreground="red")  # Фон кнопок, шрифт, ширина

        self.clear_window()
        self.current_view = "Результаты:"

        # Создаем фрейм для центрального выравнивания
        frame = ttk.Frame(self.root)
        frame.pack(expand=True)  # Разрешаем фрейму расширяться, чтобы занять все доступное пространство

        # Заголовки
        ttk.Label(frame, text="Просмотр результатов!", width=20, font=("Arial", 20)).grid(row=0, column=0, columnspan=2,
                                                                                          pady=10)  # columnspan=2 расширяет на 2 колонки.

        # Дуэль
        ttk.Label(frame, text="Дуэль:", width=15, font=("Arial", 18)).grid(row=1, column=0, sticky="w",
                                                                           padx=30)  # sticky="w" прижимает к левой границе
        s = show_rezult(1)
        ttk.Label(frame, text=s, width=30, font=("Arial", 15)).grid(row=1, column=1, sticky="w",
                                                                    padx=10)  # sticky="w" прижимает к правой границе

        # Одна змейка
        ttk.Label(frame, text="Одна змейка:", width=15, font=("Arial", 18)).grid(row=2, column=0, sticky="w", pady=5,
                                                                                 padx=10)
        s = show_rezult(2)
        ttk.Label(frame, text=s, width=30, font=("Arial", 15)).grid(row=2, column=1, sticky="w", pady=5, padx=10)

        # Выживание
        ttk.Label(frame, text="Выживание:", width=15, font=("Arial", 18)).grid(row=3, column=0, sticky="w", pady=5,
                                                                               padx=10)
        s = show_rezult(3)
        ttk.Label(frame, text=s, width=30, font=("Arial", 15)).grid(row=3, column=1, sticky="w", pady=5, padx=10)

        # Кнопка
        delete_button = ttk.Button(self.root, text="Очистить результаты", width=40, command=self.delete_rezult,style="Menu.TButton")
        delete_button.pack(pady=10)
        close_button = ttk.Button(self.root, text="Закрыть окно",width=40, command=self.restart, style="Menu.TButton")
        close_button.pack(pady=10)

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
    rooot.resizable(width=False, height=False)
    rooot.mainloop()
if __name__ == "__main__":
    main()

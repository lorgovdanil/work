import os

# Определите имя папки, которую хотите создать
folder_name = 'rezult'
# Определите путь к папке проекта
project_directory = os.getcwd()

folder_path = os.path.join(project_directory, folder_name)

def show_rezult(type):
    if type == 1:
        sp = read_file(1)
        if not sp:
            s = "no rezult"
        else:
            s = f"count victory:\n1 player: {sp[0]} 2 player: {sp[1]} \nbest rezult\n1 player: {int(sp[2])} 2 player: {int(sp[3])}"
        return s
    elif type == 2:

        sp = read_file(2)
        if not sp:
            s = "no rezult"
        else:
            s = f"Best rezult:\n1. {int(sp[0])}\n2. {int(sp[1])}\n3. {int(sp[2])}"
        return s
    elif type == 3:
        sp = read_file(3)
        if not sp:
            s = "no rezult"
        else:
            s = f"Count victory:\n1 player: {sp[0]}\n2 player: {sp[1]}\n"
        return s
def file_dual_game(value1, value2):
    if value1 > value2:
        count_player1 = 1
    elif value1 < value2:
        count_player1 = 0
    else:
        count_player1 = 0.5
    sp = read_file(1)

    if not sp:
        write_file(1, f"{count_player1} {1 - count_player1} {value1} {value2}") # количество побед 1, 2 игрока, наилучшие результаты 1, 2 игрока
    else:
        sp[0] += count_player1
        sp[1] += 1 - count_player1
        sp[2] = max(sp[2], value1)
        sp[3] = max(sp[3], value2)
        write_file(1, f"{sp[0]} {sp[1]} {sp[2]} {sp[3]}")


def file_survival_game(value1, value2):
    sp = read_file(3)
    if not sp:
        write_file(3, f"{value1} {value2}")
    else:
        sp[0] += value1
        sp[1] += value2
        write_file(3, f"{sp[0]} {sp[1]}")


def update_data(type, value1, value2):
    if not os.path.exists(folder_path):
        create_dir(folder_path)
    if type == 1:
        file_dual_game(value1, value2)
    elif type == 2:
        file_single_game(value1)
    elif type == 3:
        file_survival_game(value1, value2)

def file_single_game(val):
    sp = read_file(2)
    if not sp:
        write_file(2, f"{val} 0 0")
    else:
        sp.append(val)
        sp = sorted(sp, reverse = True)
        sp.pop(-1)
        write_file(2, f"{sp[0]} {sp[1]} {sp[2]}")
def read_file(num):
    file_path= os.path.join(project_directory, folder_name)
    if num == 1:
        file_path = os.path.join(file_path, 'file1.txt')
    elif num == 2:
        file_path = os.path.join(file_path, 'file2.txt')
    elif num == 3:
        file_path = os.path.join(file_path, 'file3.txt')
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readline()
            if not content:
                return []
            sp = list(map(float, content.strip().split()))
            return sp
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []
def write_file(num, s):
    file_path= os.path.join(project_directory, folder_name)
    if num == 1:
        file_path = os.path.join(file_path, 'file1.txt')
    elif num == 2:
        file_path = os.path.join(file_path, 'file2.txt')
    elif num == 3:
        file_path = os.path.join(file_path, 'file3.txt')
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(s)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
def create_dir(name):
    os.makedirs(name)
    file_names = ['file1.txt', 'file2.txt', 'file3.txt']
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w') as file:
            file.write("")



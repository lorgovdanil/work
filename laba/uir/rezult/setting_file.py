import os
folder_name = 'rezult'
project_directory = os.getcwd()

file_path = os.path.join(project_directory, "setting")
def read_setting_file():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readline()
            if not content:
                return []
            sp = content.strip().split(";")
            return sp
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []
def write_setting_file(n, s):
    sp = read_setting_file()
    if sp is []:
        pass
    else:
        sp[n] = s
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                d = ";".join(sp)
                file.write(d)
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

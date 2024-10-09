import math
import random

def f1():
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    if (y1 != y2):
        k = (x1 - x2) / (y1 - y2)
    else:
        k = 0
    b = y1 - k * x1

    print(f"y = {k}x + {b}")

def f2(n):
    match n:
        case 1:
            x = float(input("x = "))
            y = float(input("y = "))
            z = float(input("z = "))
        case 2:
            x = random.random() + random.randint(-10 ** 6, 10 ** 6)
            y = random.random() + random.randint(1, 10 ** 6) * (-1) ** random.randint(1, 2)
            z = random.random() + random.randint(1, 10 ** 6) * (-1) ** random.randint(1, 2)
            print(f"x = {x:.2}")
            print(f"y = {y:.2}")
            print(f"z = {z:.2}")

    a = (abs(x - 1) ** (1 / 2) - abs(y) ** (1 / 2)) / (1 + x * x / 2 + y * y / 4)
    b = x * (math.atan(z) + 5)
    print(f"a = {a:.2}")
    print(f"b = {b:.2}")

def f3(n):
    match n:
        case 1:
            a = float(input("Введите 1 сторону "))
            b = float(input("Введите 2 сторону "))
            c = float(input("Введите 3 сторону "))
            p = (a + b + c) / 2
            s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
        case 2:
            a = float(input("Введите 1 сторону "))
            b = float(input("Введите 2 сторону "))
            s = a * b
        case 3:
            r = float(input("Введите радиус "))
            s = math.pi * r * r
    print(f"s = {s:.2}")

def f4(nomer):
    n = int(input("Введите номер элемента = "))
    match nomer:
        case 1:
            a = 1
            b = 1
            c = 1
            for n in range(3, n + 1):
                c = a + b
                b = a
                a = c
            print(c)
        case 2:
            n = n - 1
            def f(matr, n):
                if n == 0:
                    return [[1, 0], [0, 1]]
                elif n == 1:
                    return matr
                elif n % 2 == 0:
                    x = f(matr, n / 2)
                    return [[sum(x[i][k] * x[k][j] for k in range(len(x))) for j in range(len(x))] for i in range(len(x))]
                else:
                    x = f(matr, n - 1)
                    return [[sum(x[i][k] * matr[k][j] for k in range(len(x))) for j in range(len(x))] for i in range(len(x))]

            sp = [[1, 1], [1, 0]]
            print(f(sp, n)[0][0])

def f5():
    x = int(input("i = "))
    y = int(input("j = "))
    z = int(input("k = "))
    s1 = 0
    s2 = 1
    s3 = 0
    s4 = 0

    for i in range(1, 9):
        for j in range(1, i + 1):
            s1 = y * y + s1

    for i in range(1, 9):
        for j in range(1, 2 * i + 1):
            s2 = (y ** 3 + x ** 2) * s2
        s3 = s2 + s3
        s2 = 1

    for i in range(1, 9):
        for j in range(1, i + 1):
            for k in range(1, 4):
                s4 = y * y + x * z + s4

    print("Первое выражение = ", s1)
    print("Второе выражение = ", s3)
    print("Третье выражение = ", s4)

def f6():
    p = int(input("p = "))
    x = int(input("x = "))

    k = 1
    while (k == 1):
        yn = float(input("y0 = "))
        if (yn < math.floor(math.exp((math.log(x * (p + 1))) / p))):
            k = 0
        else:
            print("Ваше значение не подходит под начальное условие!")
    temp = yn
    s = 2
    print("Точность", 7 * " ", "Корень", 8 * " ", "Число итераций")
    for i in range(2, 7):
        n = 0
        e = 10 ** (-i)
        yn = temp
        yn1 = 1 / p * ((p - 1) * yn + x / math.pow(yn, p - 1))
        while abs(yn1 - yn) > e:
            yn = yn1
            yn1 = 1 / p * ((p - 1) * yn + x / math.pow(yn, p - 1))
            n = n + 1
        print(" " * s, e, 8 * " ", f"{round(yn,5):.5}", 13 * " ", n)
        if (i == 2 or i > 3):
            s = 1
        else:
            s = 0

flag = True
number = int(input("Введите номер задания\n"))
while (flag):
    if (number > 6 or number < 1):
        print("Такого задания не существует")
        quit()

    match number:
        case 1:
            f1()

        case 2:
            var = int(input("Если вы хотите записать числа сами - введите 1,\nЕсли вы хотите генерацию рандомных чисел - введите 2\n"))
            if (var > 2 or var < 1):
                quit()
            f2(var)

        case 3:
            var = int(input("Если вы хотите площадь треугольника - введите 1,\nЕсли вы хотите площадь прямоугольника - введите 2,\nЕсли вы хотите площадь круга - введите 3\n"))
            if (var > 3 or var < 1):
                quit()
            f3(var)

        case 4:
            var = int(input("Если вы хотите найти элемент ряда с помощью динамического программирования - введите 1,\nЕсли вы хотите найти элемент ряда с помощью матриц - введите 2\n"))
            if (var > 2 or var < 1):
                quit()
            f4(var)

        case 5:
            f5()

        case 6:
            f6()
    number = int(input("\nЕсли хотите продолжить - введите номер задания,\nЕсли желаете выйти - введите 0\n"))
    if (number > 6 or number < 1):
        flag = False
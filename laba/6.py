import math

p = int(input("p = "))
x = int(input("x = "))
yn = float(input("y0 = "))

print("Точность", 20 * " ", "Корень", 10 * " ", "Число итераций")
for i in range(2, 7):
    n = 0
    e = 10 ** (-i)
    yn = 1#math.floor(math.exp((math.log(x * (p + 1))) / p))
    yn1 = 1/p*((p-1)*yn + x/ math.pow(yn,p-1))
    while abs(yn1 - yn) > e:
        yn = yn1
        yn1 = 1 / p * ((p - 1) * yn + x / math.pow(yn, p - 1))
        n = n + 1
    print(e, 13 * " ", yn, 13 * " ", n)
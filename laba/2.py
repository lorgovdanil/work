import math
import random

x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
a = (abs(x - 1) ** (1/2) - abs(y) ** (1/2)) / (1 + x*x/2 + y*y/4)
b = x * (math.atan(z) + 5)
print("a = ", a)
print("b = ", b, "\n")

x = random.random() + random.randint(-10**6, 10**6)
y = random.random() + random.randint(1, 10**6) * (-1)**random.randint(1, 2)
z = random.random() + random.randint(1, 10**6) * (-1)**random.randint(1, 2)
a = (abs(x - 1) ** (1/2) - abs(y) ** (1/2)) / (1 + x*x/2 + y*y/4)
b = x * (math.atan(z) + 5)

print("x = ", x)
print("y = ", y)
print("z = ", z, "\n")

print("a = ", a)
print("b = ", b)
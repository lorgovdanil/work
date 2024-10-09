x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
k = (x1 - x2) / (y1 - y2)
b = y1 - k * x1
print(f"y = {k}x + {b}")

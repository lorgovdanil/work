x = int(input("i = "))
y = int(input("j = "))
z = int(input("k = "))
s1 = 0
s2 = 1
s3 = 0
s4 = 0

for i in range(1, 9):
    for j in range(1, i + 1):
        s1 = y*y + s1

for i in range(1, 9):
    for j in range(1, 2 * i + 1):
        s2 = (y**3 + x**2) * s2
    s3 = s2 + s3
    s2 = 1

for i in range(1, 9):
    for j in range(1, i + 1):
        for k in range(1, 4):
            s4 = y*y + x*z + s4

print("Первое выражение = ", s1)
print("\nВторое выражение = ", s3)
print("\nТретье выражение = ", s4)
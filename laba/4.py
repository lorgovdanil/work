a = 1
b = 1
c = 1
n = int(input())
for n in range(3, n + 1):
    c = a + b
    b = a
    a = c
print(c)
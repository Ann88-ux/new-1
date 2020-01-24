from random import *

i, j = 0, 0
min1, min2 = 101, 101
max1, max2 = 0, 0
for i in range(10):
    a = randint(10, 100)
    print(a)
    if a < min1:
        min1 = a
    elif min1 < a < min2:
        min2 = a
print(min1, min2)
for j in range(10):
    b = uniform(5, 35)
    print(b)
    if b > max1:
        max1 = b
    elif max1 > b > max2:
        max2 = b
print(max1, max2)

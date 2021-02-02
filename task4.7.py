from itertools import count
from math import factorial

def deff():
    for el in count(1):
        yield factorial(el)

y = deff()
x = 0
for i in y:
    if x < 15:
        print(i)
        x += 1
    else:
        break
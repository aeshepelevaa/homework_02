from itertools import cycle

с = 0
for el in cycle("привет"):
    if с > 11:
        break
    print(el)
    с += 1
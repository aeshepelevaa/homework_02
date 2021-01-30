from functools import reduce


def my_func(x, y):
    return x * y

print(f'Список чисел: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Итог: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')


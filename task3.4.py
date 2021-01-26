x = int(input("Введите первое число"))
y = int(input("Введите второе число"))
def my_func(x, y):
    if x > y and y < 0:
        return x ** y
    if y > 0:
        return "Не подходит по условию"
print(f'Итог : {my_func((x), (y))}')
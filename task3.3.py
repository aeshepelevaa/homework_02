arg1 = int(input("Введите первое число"))
arg2 = int(input("Введите второе число"))
arg3 = int(input("Введите третье число"))
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Итог : {my_func((arg1), (arg2), (arg3))}')

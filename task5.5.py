def s():
    try:
        with open('sum.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            num = line.split()

            print(sum(map(int, num)))
    except ValueError:
        print('Неправильный ввод цифр')
s()

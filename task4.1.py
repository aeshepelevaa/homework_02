def wages():
    try:
        time = float(input('Выработка в часах: '))
        bid = int(input('Ставка в часах: '))
        prize = int(input('Премия: '))
        res = time * bid + prize
        print(f'Итог:  {res}')
    except ValueError:
        return print('Введите число!')
wages()

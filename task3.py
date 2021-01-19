month = int(input("Введите меясц числом от 1 до 12: "))
season1 = ['winter', 'spring', 'summer', 'autumn']
season2 = {1: 'winter',
           2: 'spring',
           3: 'summer',
           4: 'autumn'}
if month == 1 or month == 2 or month == 12:
    print(season1[0])
if month == 3 or month == 4 or month == 5:
    print(season1[1])
if month == 6 or month == 7 or month == 8:
    print(season1[2])
if month == 9 or month == 10 or month == 11:
    print(season1[3])
else:
    print("Не подходит по условию")






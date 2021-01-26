def my_sum():
    sum_result = 0
    ex = False
    while ex == False:
        number = input('Введите число ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'a' or number[el] == 'A':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_result = sum_result + res
        print(f'Текущая сумма:{sum_result}. Если хотите получит конечную сумму введите а или А ')
    print(f'Конечная сумма: {sum_result}')

my_sum()

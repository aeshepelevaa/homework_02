f = open("for_lesson_5.txt", "a")
data_for_file = ['Milk\n', 'Bread\n', 'Sugar\n', 'Salad']
f.writelines(data_for_file)
print(f'Количество строк в файле - {len(data_for_file)}')
f = open("for_lesson_5.txt", "a")
data_for_file = ['Milk\n', 'Bread\n']
f.writelines(data_for_file)
print(f'Количество строк в файле - {len(data_for_file)}')
for el in range(len(data_for_file)):
    print(f'Общее колличество строк {len(data_for_file[el])}')
f.close()

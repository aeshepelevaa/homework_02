f_obj = open('test.txt', 'w')
line = input('Введите имя \n')
line2 = input('Введите фамилию \n')
line3 = input('Введите место работы \n')
while line:
    f_obj.writelines(line)
    f_obj.writelines(line2)
    f_obj.writelines(line3)
    line = input('Введите имя \n')
    line2 = input('Введите фамилию \n')
    line3 = input('Введите место работы \n')
    if not line:
        break

f_obj.close()
f_obj = f_obj .readlines()
f_obj = open('test.txt', 'r')
print(f_obj)
f_obj.close()

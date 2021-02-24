f_obj = open('test.txt', 'w')
line = input('Введите имя \n')
line2 = input('Введите фамилию \n')
line3 = input('Введите место работы \n')
while line:
    f_obj.writelines(line)
    line = input('Введите имя \n')
    line2 = input('Введите фамилию \n')
    line3 = input('Введите место работы \n')
    if not line:
        break

f_obj.close()
content = f_obj .readlines()
f_obj = open('test.txt', 'w')
print(content)
f_obj.close()

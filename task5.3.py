with open('salary.txt', 'r') as my_file:
    s = []
    p = []
    my_list = my_file.read().split('\n')
    for el in my_list:
        el = el.split()
        if int(el[1]) < 20000:
           p.append(el[0])
        s.append(el[1])
f = sum(map(int, s)) / len(s)
print(f'Оклад меньше 20.000 {p}, средний оклад {f}')
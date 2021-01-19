num = int(input("Введите количество элементов списка "))
list1 = []
a = 0
b = 0
while a < num:
    list1.append(input("Введите значение списка "))
    a += 1

for elem in range(int(len(list1) / 2)):
        list1[b], list1[b + 1] = list1 [b + 1], list1[b]
        b += 2 
print(list1)

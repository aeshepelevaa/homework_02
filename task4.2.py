list1 = [0, 666, 44, 7, 678, 1000, 78, 408]
print(f'Исходный список {list1}')
list2 = [el for num, el in enumerate(list1) if list1[num - 1] < list1[num]]
print(f'Новый список {list2}')
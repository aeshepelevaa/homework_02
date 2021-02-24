words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
words2 = []
with open('words.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        words2.append(words[i[0]] + '  ' + i[1])
    print(words2)

with open('words2.txt', 'w') as file_obj2:
    file_obj2.writelines(words2)

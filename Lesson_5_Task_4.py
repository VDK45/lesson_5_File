rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
file = open('text_4.txt', 'r', encoding="utf-8")
for i in file:
    i = i.split(' ', 1)
    new_list.append(rus[i[0]] + '  ' + i[1])
file.close()

file_create = open('rus_test.txt', 'w', encoding="utf-8")
file_create.writelines(new_list)
file_create.close()
print('Читаем с файла rus_test.txt: ')
with open('rus_test.txt', 'r', encoding='utf-8') as text:
    print(text.readlines())

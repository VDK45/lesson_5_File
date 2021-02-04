file = open(f'test.txt', 'w', encoding="utf-8")
line = input('Введите текст ')
while line:
    file.writelines(line + '\n')
    line = input('Введите текст ')
    if not line:
        break

file.close()
print('-' * 9, 'Проверка юни код не работает!?', '-' * 9)

file = open('test.txt', 'r')
content = file.read()
print(content)
file.close()

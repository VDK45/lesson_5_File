file = open(f'sum_numbers.txt', 'w', encoding="utf-8")
line = input('Введите цифры через пробел: ')
file.writelines(line + '\n')
file.close()

file_open = open(f'sum_numbers.txt', 'r', encoding="utf-8")
digit = file_open.readline()
digit = digit.split()

suma = 0
for x in digit:
    suma += int(x)
print(' + '.join(digit), '=', suma)
file_open.close()

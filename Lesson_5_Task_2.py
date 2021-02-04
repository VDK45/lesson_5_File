file = open("ozon.txt", "r", encoding='utf-8')
data = file.readlines()
print("В файле ", len(data), "строк.")
x = 0
for i in data:
    x += 1
    #print('В', x, 'строке', len(i), 'Букв.')
file.close()
file = open(f"ozon.txt", "r", encoding='utf-8')
n = 0
while x > 0:
    x -= 1
    n += 1
    data = file.readline()
    data = data.split()
    print('В', n, 'строке', len(data), 'слов.')
file.close()

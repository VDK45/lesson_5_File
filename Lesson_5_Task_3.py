file = open("text_3.txt", "r", encoding='utf-8')

person = []
cost = []  # 209003.6
per_low = []
n = 0
for i in file:
    n += 1
    # print(i, end="")
    h = i.split()
    person.append(h[0])
    cost.append(float(h[1]))
    if float(h[1]) < 20000:
        per_low.append(h[0])
print('Сотрудники с доходом меньше 20000: ', ', '.join(per_low))
suma = 0
for x in cost:
    suma += x
print('Средний доход сотрудников ', suma / len(person))

file.close()

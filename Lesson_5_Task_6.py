dic = {}
file = open("text_6.txt", encoding='utf-8')
lines = file.readlines()
for line in lines:
    data = line.replace('(', ' ').split()
    s = []
    for i in data:
        if i.isdigit() == True:
            s.append(int(i))
    dic[data[0]] = sum(s)
for i in dic:
    print(i, dic[i], 'lessons')
print(dic)
file.close()
print('-'*7, 'with Regular Expressions', '-'*7)
'''task6 with Regular Expressions'''
import re

dic = {}
with open('text_6.txt', encoding='utf-8') as in_file:
    lines = in_file.readlines()
    for line in lines:
        line_str = line.split(" ")
        digital = r"\d+"
        i = re.findall(digital, line)
        s = 0
        for dig in i:
            s += int(dig)
            dic[line_str[0]] = s
print(dic)

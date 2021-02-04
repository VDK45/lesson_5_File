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

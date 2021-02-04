import json

firm = {}
average = {}

with open('text_7.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    n = 0
    x = 0
    for line in lines:
        # print(line, end='')
        data = line.split()
        for i in data:
            minus = int(data[-2]) + -int(data[-1])
        if minus >= 0:
            n += minus
            firm[data[0]] = minus
            x += 1
    # print(n)
    # print(x)
    profit = n / x
    average['average_profit'] = profit
ok = [firm, average]
print(ok)

with open(f'text_77.json', 'w', encoding='utf-8') as json_file:
    json.dump(ok, json_file, ensure_ascii=False, indent=4)

with open(f'text_77.json', 'r', encoding='utf-8') as json_f:
    data = json.load(json_f)
    print(' \n \nLoad from json File \n \n ', data, ' \n \n its ok')


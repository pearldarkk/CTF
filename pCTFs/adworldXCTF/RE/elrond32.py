def choose(num):
    switcher = {
        0: 'i',
        1: 'e',
        3: 'n',
        4: 'd',
        5: 'a',
        6: 'g',
        7: 's',
        9: 'r',
    }
    return switcher.get(num, '')

flag = ''
num = 0
for i in range(0, 20):
    flag += choose(num)
    num = (num + 1) * 7 % 11
print(flag)
cipher = 'KanXueCTF2019JustForhappy'
apb = 'abcdefghiABCDEFGHIJKLMNjklmn0123456789opqrstuvwxyzOPQRSTUVWXYZ'
encode = []

for i in cipher:
    encode.append(apb.find(i))

flag = 'flag{'
for c in encode:
    if (0x0 <= c <= 0x9):
        flag += chr(c + 0x30)
    elif (0x24 <= c <= 0x3d):
        flag += chr(c + 0x1D)
    else:
        flag += chr(c + 0x57)
flag += '}'
print(flag)
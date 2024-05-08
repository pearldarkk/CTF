flag = 'ajygkFm.\x7f_~-SV{8mLn\x00'
flag = list(flag)

for i in range(18, -1, -1):
    if (i == 18):
        flag[i] = chr(ord(flag[i]) ^ 0x13)
    elif i % 2 != 0:
        flag[i] = chr((ord(flag[i]) ^ i) + i)
    else:
        flag[i + 2] = chr(ord(flag[i]) ^ i)
for i in flag:
    print(i, end='')

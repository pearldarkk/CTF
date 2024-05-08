s = 'c61b68366edeb7bdce3c6820314b7498'
flag = ''
for i in range(len(s)):
    if i & 1:
        flag += chr(ord(s[i]) + 1)
    else:
        flag += chr(ord(s[i]) - 1)
print('harifCTF{' + flag + '}')

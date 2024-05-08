buf = '\\8koIw\\f4Sk6u\\'
flag = ''
for c in buf:
    if ('0' <= c <= '9'):
        flag += chr((ord(c)-ord('0') +10 - 3) % 10 + ord('0'))
    elif ('a' <= c <= 'z'):
        flag += chr((ord(c)-ord('a') +26 - 3) % 26 + ord('a'))
    elif ('A' <= c <= 'Z'):
        flag += chr((ord(c)-ord('A') +26 - 3) % 26 + ord('A'))
    else:
        flag += chr((ord(c) + 3))

print(flag)        
unk = '??????????????'
print(len(unk))
print(len(buf))
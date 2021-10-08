import base64

cipher = 'XlNkVmtUI1MgXWBZXCFeKY+AaXNt'
cipher = base64.b64decode(cipher)
flag = ''
for i in cipher:
    flag += chr((i - 16) ^ 32)
print(flag)
flag = b'\xbb\xb6\xd3\xad\xc0\xb4\xb5\xbdDUTCTF\xdf\xcf\n\x00\x00\x00'
for i in flag:
    print(chr(i), end='')

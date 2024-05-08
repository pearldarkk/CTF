s = b'\xff\xff\xff\xff\xff\xff\xff\xffN\xe6@\xbb\xb1\x19\xbfD\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff\x01\x00\x00\x00~}|{zyxwvutsrqponmlkjihgfedcba`_^]\\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)(\'&%$#"! '
enc = b'DDCTF{reverseME}'
flag = b''
print(len(s))
for c in enc:
    flag += s[c].to_bytes(1, 'little')
flag = str(flag)[2:-1]

print('flag{' + flag + '}')
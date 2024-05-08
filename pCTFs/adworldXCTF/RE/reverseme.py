from base64 import *

byte = 'you_know_how_to_remove_junk_code'
flag = ''

for i in byte:
    flag += chr(ord(i) ^ 0x25)

flag = b64encode(flag.encode('ascii')).decode('utf-8')
print(flag)

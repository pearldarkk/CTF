enc = b'327a6c4304ad5938eaf0efb6cc3e53dc'
s = b'flag{'

for byte in enc:
    byte -= 11
    byte ^= 0x13
    byte -= 23
    byte ^= 0x50
    s += byte.to_bytes(1, 'little')

s += b'}'
print(s)
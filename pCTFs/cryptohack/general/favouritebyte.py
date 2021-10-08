from pwn import xor

flag = bytes.fromhex(
    '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

byte = xor(b'c', flag[0])
flag = xor(byte, flag)
print(flag)
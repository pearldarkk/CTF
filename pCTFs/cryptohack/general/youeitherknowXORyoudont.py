from pwn import xor

flag = bytes.fromhex(
    '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
)
byte = xor(flag[0:7], b'crypto{')
print(byte)
byte = b'myXORkey'
flag = xor(flag, byte)
print(flag)

from binascii import unhexlify
from pwn import xor
from random import randint

strs = [
    b'my encryption method', b'is absolutely impenetrable',
    b'and you will never', b'ever', b'break it'
]

with open('enc.txt', 'rb') as f:
    enc = unhexlify(f.read())

# f = open('text.out', 'w')

while True:
    for s in strs:
        for m in range(randint(0, pow(2, 0))):
            enc = xor(enc, s)
    prefix = b'picoCTF{'
    # key = xor(enc[:len(prefix)], prefix)
    # if key.decode().isprintable():
    # print(key)
    key = b'Africa!'
    flag = xor(key, enc)
    if flag.startswith(prefix):
        print(flag)
        exit()

# f.close()
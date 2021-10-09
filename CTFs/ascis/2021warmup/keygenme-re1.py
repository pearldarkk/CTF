# 9235474F-3878CAE5
# Brian Baker
from pwn import *

r = remote('125.235.240.166', '20100')


def __ROR__(num, count, bits=32):
    return ((num >> count) | (num << (bits - count))) & ((0b1 << bits) - 1)


def gen_name(name="Anthony Adams"):
    l = len(name)
    res = 0
    i = 0
    while True:
        tmp = ord(name[i]) + res
        i += 1
        res = (__ROR__(tmp, 12)) ^ 0x55aa
        if i >= l:
            break
    return res


r.recvuntil(b'Name: ')
name = str(r.recvline())[2:-3]

# name = input()
lenn = len(name)

v7 = 0
ind = 0
while True:
    v7 = __ROR__((ord(name[ind]) + v7), 4)
    ind += 1
    if ind >= lenn:
        break

s1 = hex(v7)[2:].upper()
s2 = hex(gen_name(name))[2:].upper()
print("{0}-{1}".format(s1, s2))
s = s1 + '-' + s2
r.sendlineafter(b'Serial:', s)
flag = r.recvline()
print(flag)
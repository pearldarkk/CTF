from pwn import *

r = remote('125.235.240.166', '20103')
op = '+-*/%'
while(True):
    r.recvuntil("problems?")
    line = r.recvline()
    for c in line:
        if c in op:
            a,b = int(line.split(c))


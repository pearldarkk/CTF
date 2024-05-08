import subprocess
from pwn import *
import re

r = remote('125.235.240.166', '20123')


def scanQR():
    r.recvuntil(':\n')
    qr = str(r.recvuntil('ID'), 'utf-8').split('\n')

    for i in range(len(qr)):
        qr[i] = re.subn('^\xa0\xa0\xa0\xa0+', '', qr[i])
    matrix = [['_' for _ in range(len(qr) * 2)] for i in range(len(qr) * 2)]
    qr.pop(0)
    qr.pop(0)
    qr.pop(len(qr) - 2)
    qr.pop(len(qr) - 2)
    qr.pop(len(qr) - 1)
    for i in range(len(qr)):
        qr[i] = str(qr[i])
        for j in range(len(qr[i])):
            if qr[i][j] == '█':
                matrix[2 * i][j] = 'X'
                matrix[2 * i + 1][j] = 'X'
            elif qr[i][j] == '▀':
                matrix[2 * i][j] = 'X'
                matrix[2 * i + 1][j] = '_'
            elif qr[i][j] == '▄':
                matrix[2 * i][j] = '_'
                matrix[2 * i + 1][j] = 'X'

    f = open('text.out', 'w')
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            f.write(matrix[i][j])
        f.write('\n')

    ans = subprocess.check_output("python2 ./sqrd.py text.out")
    ans = ans.split('|')
    r.sendlineafter('Number: ', ans[0])
    r.sendlineafter('Name: ', ans[1])
    r.sendlineafter('Expired Date:', ans[3])


if __name__ == '__main__':
    while True:
        scanQR()
        s = r.recvline()
        print(s)
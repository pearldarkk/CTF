from itertools import combinations
from hashlib import md5
import string

alphabet = string.ascii_letters + string.digits + '_'

com = list(combinations(alphabet, 1))
com += list(combinations(alphabet, 2))
com += list(combinations(alphabet, 3))

s = ''
with open('c.txt', 'r') as f:
    dat = f.read().split("\n")
    for l in dat:
        flag = 0
        for salt in com:
            saltstr = ''.join(salt)
            for c in alphabet:
                if md5((s + saltstr + c).encode('utf-8')).hexdigest() == l:
                    print(c, end='')
                    s = saltstr + c
                    flag = 1
                    break
            if (flag):
                break

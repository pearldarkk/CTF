from sympy.ntheory.modular import *
import itertools
import gmpy2
from Crypto.Util.number import *

f = open("encrypted-messages.txt")
a = f.readlines()
n_list = []
c_list = []
for i in range(0, len(a), 4):
    n_list.append(int(a[i].split()[-1]))
    c_list.append(int(a[i + 2].split()[-1]))

tmp = [i for i in range(len(n_list))]
for lis in itertools.combinations(tmp, 3):  #bruteforce
    candi = list(lis)
    m3, n = crt([n_list[candi[0]], n_list[candi[1]], n_list[candi[2]]],
                [c_list[candi[0]], c_list[candi[1]], c_list[candi[2]]])
    m, ch = gmpy2.iroot(int(m3), 3)
    if ch: print(long_to_bytes(int(m)))
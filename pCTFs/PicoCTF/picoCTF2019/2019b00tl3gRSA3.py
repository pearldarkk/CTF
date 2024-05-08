from pwn import *
from egcd import egcd
from Crypto.Util.number import *
import sympy

def totient(n):
    factor = sympy.factorint(n)
    rst = 1
    for i, j in factor.items():
        rst *= pow(i,j )

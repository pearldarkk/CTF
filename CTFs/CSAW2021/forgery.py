from random import randint
from Crypto.Util.number import bytes_to_long
# Elgamal Signature
# https://blog.cryptohack.org/cyber-apocalypse-2021 forge of empires

g = 3
MASK = 2**1024 - 1


def forgery(y: int):
    e = randint(1, p - 1)
    r = y * pow(g, e, p) % p
    s = -r % (p - 1)
    m = (e * s) % (p - 1)
    m += (bytes_to_long(b'Cisco') << 1200)
    M = hex(m)[2:]
    return (M, r, s)


p = int(input('p: '))
y = int(input('y: '))
M, r, s = forgery(y)
print(f'M: {M}')
print(f'r: {r}')
print(f's: {s}')

from Crypto.Util.number import long_to_bytes, inverse
import owiener
from gmpy2 import isqrt, is_square
from Crypto.PublicKey import RSA
from pwn import *

r = remote('crypto.chal.csaw.io', 5008)


def quiz1():
    r.recvuntil(b"N = ")
    n = int(r.recvline().split()[-1])
    e = int(r.recvline().split()[-1])
    c = int(r.recvline().split()[-1])
    d = owiener.attack(e, n)
    # r.recvuntil('What is the plaintext?')
    m = long_to_bytes(pow(c, d, n))
    r.sendlineafter(b' plaintext?', m)
    print('Part 1: ', m)


def quiz2():
    # sexy primes: pair of (p, p + 6)
    # n = p * (p + 6) = (p + 3) ** 2 - 9
    # n + 9 = (p + 3)** 2

    r.recvuntil(b"N = ")
    n = int(r.recvline().split()[-1])
    e = int(r.recvline().split()[-1])
    c = int(r.recvline().split()[-1])
    p = isqrt(n + 9) - 3
    d = inverse(e, (p - 1) * (p + 5))
    m = long_to_bytes(pow(c, d, n))
    r.sendlineafter(b' plaintext?', m)
    print('Part 2: ', m)


def quiz3():
    # https://ctftime.org/writeup/16651
    # https://github.com/ashutosh1206/Crypton/blob/master/RSA-encryption/Attack-LSBit-Oracle/lsbitoracle.py
    # https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-3/

    r.recvuntil(b"N = ")
    n = int(r.recvline().split()[-1])
    e = int(r.recvline().split()[-1])
    c = int(r.recvline().split()[-1])

    prev = str('0').encode()
    m = '1'
    print('Part 3: ')
    for i in range(1, 400):
        inv = inverse(2**i, n)
        query = (c * pow(inv, e, n)) % n
        r.sendlineafter(b'an integer)', str(query).encode())
        r.recvuntil(b" responds with: ")
        lsb = int(r.recvline())
        char = (lsb - (int(m, 2) * inv) % n) % 2
        m = str(char) + m
        if len(m) % 8 == 0:
            if prev == long_to_bytes(int(m, 2)):
                r.sendlineafter(b'(yes/no)', b'no')
                r.sendlineafter(b' plaintext?', prev)
                break
            else:
                prev = long_to_bytes(int(m, 2))
                print(prev)
        r.sendlineafter(b'(yes/no)', b'yes')

def quiz4():
    # https://www.jianshu.com/p/d8d2ce53041b
    d = 3609078160294653582627218627016190721855287633637416192065891300819825430209176418664124843225511887589509827719138227661323323392121338364584074284279667471933835110753924054662994245311963966964361457025795043910639404857441627410368658564714017763061317328382076670140376810656172016530463299980305538065
    n = 61354328725009110904662716659275242271539889771836075265120152113937032313555999117290122334833702089021667071225349870242496497666062752197929262832754362704460251233727815272161214664274657287725743695980286290326940956179914439969975329836770894979963849511231067481448088547959309648091922398434312801709
    e = 17
    c = 22011744623459587015476758989657795591540714973935702220778301810485641377039292690880523636433974347355987217564188652839703156340079467162221019832714584188409328120116730936373305177007244861904567436971910605633450682185401663405008159575901631275560698871411568347042950918417858563916870405039328058009
    print(long_to_bytes(pow(c, d, n)))

def main():
    # quiz1()
    # # b'Wiener wiener chicken dinner'
    # quiz2()
    # # b'Who came up with this math term anyway?'
    # quiz3()
    # # b'Totally did not mean to put an oracle there'
    quiz4()
    # b'I'll be careful next time to not leak the key'

if __name__ == "__main__":
    main()

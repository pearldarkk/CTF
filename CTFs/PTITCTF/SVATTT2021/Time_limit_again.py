from math import sqrt
from Crypto.Util.number import long_to_bytes, isPrime
from gmpy2 import is_prime
from hashlib import md5
import string


def palind(num):
    my_str = str(num)
    rev_str = reversed(my_str)
    if list(my_str) == list(rev_str):
        return True
    else:
        return False


primes = []


def sieve(n):
    m = [False for i in range(n + 1)]
    primes.append(2)

    for i in range(3, n, 2):
        if not m[i]:
            for j in range(i * i, n, i):
                m[j] = True

    for i in range(3, n, 2):
        primes.append(i)


def isprime(x):
    for p in primes:
        if x % p == 0:
            return False
        if x < p:
            break
    return True


plist = [
    2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 70207, 70507,
    70607, 71317, 71917, 72227, 72727, 73037, 73237, 73637, 74047, 74747,
    75557, 1003001, 1008001, 1022201, 1028201, 1035301, 1043401, 100030001,
    100050001, 100060001, 100111001, 100131001, 100161001, 100404001,
    100656001, 100707001, 100767001, 100888001, 100999001, 101030101,
    101060101, 101141101, 101171101, 101282101, 101292101, 101343101,
    101373101, 101414101, 101424101, 101474101, 101595101, 101616101,
    101717101, 101777101, 101838101, 101898101, 101919101, 101949101,
    101999101, 102040201
]

alphabet = string.printable


def main():
    # sieve(100000)
    # p = 0
    # for i in range(0, 56):
    #     while ((not palind(p)) or (not isprime(p))):
    #         p = p + 1

    #     print(p)
    #     plist.append(p)

    #     if (i == 12):
    #         p = 50000
    #     if (i == 25):
    #         p = 500000
    #     if (i == 31):
    #         p = 500000000
    #     p = p + 1

    # print(plist)
    flag = ''
    with open('cipher.txt', 'r') as f:
        dat = f.read().split('\n')
        for i in range(len(dat)):
            for c in alphabet:
                ci = str(ord(c) ^ plist[i])
                if md5(ci.encode('utf-8')).hexdigest() == dat[i]:
                    flag += c
                    break
    print(flag)


if __name__ == '__main__':
    main()
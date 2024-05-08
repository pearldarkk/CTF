# https://crypto.stackexchange.com/questions/32200/affine-cipher-and-plaintext-attacks-how-to-find-the-base-modulo
# https://crypto.stackexchange.com/questions/31908/affine-cipher-over-an-affine-cipher/31909#31909
from Crypto.Util.number import isPrime, inverse
from math import sqrt


def factorize(x):
    for i in range(2, int(sqrt(x))):
        while (x % i == 0):
            x //= i
    if (x != 1):
        if isPrime(x):
            print(x)


def calc():
    n = (c[b[1] - 1] - c[b[2] - 1]) * (m[b[2] - 1] - m[b[3] - 1]) - (
        m[b[1] - 1] - m[b[2] - 1]) * (c[b[2] - 1] - c[b[3] - 1])
    factorize(abs(n))


def bt(x):
    for i in range(b[x - 1] + 1, 3 + x):
        b[x] = i
        if (x == 3):
            calc()
        else:
            bt(x + 1)


enc = [
    827243256, 1390726993, 514242222, 1828764689, 388796181, 1140244290,
    1359263138, 1108780435, 1766246358, 2486230612, 1359263138, 639278884,
    1453245324, 639278884, 1922746875, 75795147, 545296698, 1265280952,
    2486230612, 1108780435, 1766246358, 1985674585, 1922746875, 1453245324,
    388796181, 514242222, 1265280952, 1453245324, 1922746875, 1954210730,
    1108780435, 1453245324, 1766246358, 1922746875, 75795147, 545296698,
    639278884, 2016729061, 2079247392, 1641209696, 1453245324, 576760553,
    639278884, 75795147, 138313478, 545296698, 1766246358, 1108780435,
    1265280952, 2392248426
]

c = [enc[0], enc[1], enc[2], enc[3], enc[len(enc) - 1]]
m = [ord('K'), ord('M'), ord('A'), ord('{'), ord('}')]

b = [0 for _ in range(4)]

# bt(1)

n = 2504417651

a = (c[0] - c[1]) * inverse(m[0] - m[1], n)

b = (a * m[0] + n - c[0]) % n

a2 = inverse(a, n)

# print(a, b)
# exit()
flag = []

for i in enc:
    flag.append((i - b) * a2 % n)

shift = flag[0] - ord('K')

for i in range(len(flag)):
    flag[i] -= shift
    print(chr(flag[i]), end='')




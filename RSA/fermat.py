from Crypto.Util.number import long_to_bytes, inverse
from gmpy2 import isqrt, square, is_square


def fermat(n):
    assert n % 2 != 0
    a = isqrt(n)
    b = square(a) - n

    while not is_square(b):
        a += 1
        b = square(a) - n

    p = a + isqrt(b)
    q = a - isqrt(b)

    return int(p), int(q)


n = 0xe518e8120341fdef5e4276a475aec606ac0b3438db14684cdfee623ccdf0b332df5a5813fe7f0264004d581b2d1b05ff39968a319f16c16351bc6f262eb282b7

e = 0x10001
c = 0x4f377296a19b3a25078d614e1c92ff632d3e3ded772c4445b75e468a9405de05d15c77532964120ae11f8655b68a630607df0568a7439bc694486ae50b5c0c8507e5eecdea4654eeff3e75fb8396e505a36b0af40bd5011990663a7655b91c9e6ed2d770525e4698dec9455db17db38fa4b99b53438b9e09000187949327980ca903d0eef114afc42b771657ea5458a4cb399212e943d139b7ceb6d5721f546b75cd53d65e025f4df7eb8637152ecbb6725962c7f66b714556d754f41555c691a34a798515f1e2a69c129047cb29a9eef466c206a7f4dbc2cea1a46a39ad3349a7db56c1c997dc181b1afcb76fa1bbbf118a4ab5c515e274ab2250dba1872be0

(p, q) = fermat(n)
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))

# RSA encryption
# C = M^e mod n
# M = C^d mod n
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from base64 import b64decode, b64encode


class RSA:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.n = p * q
        self.e = e
        self.d = inverse(e, (p - 1) * (q - 1))
        pass

    def encryption(self, m):
        c = pow(m, self.e, self.n)
        return c

    def decryption(self, c):
        m = pow(c, self.d, self.n)
        return m


p = 282164587459512124844245113950593348271
q = 366669102002966856876605669837014229419
e = 65537

rsa = RSA(p, q, e)
c = rsa.decryption(0xad939ff59f6e70bcbfad406f2494993757eee98b91bc244184a377520d06fc35)
bytes = []
while True:
    bytes.append(c & 0xFF)
    c >>= 8
    if c == 0:
        break
flag = ''
for i in bytes:
    flag = chr(i) + flag
print(flag)

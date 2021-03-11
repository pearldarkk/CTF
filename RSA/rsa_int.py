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


p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

rsa = RSA(p, q, e)
c = rsa.decryption(77578995801157823671636298847186723593814843845525223303932)
print(c)

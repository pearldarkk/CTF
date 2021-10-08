import string
from Crypto.Util.number import inverse


def decryption(msg):
    ct = []
    k = inverse(123, 256)
    for c in msg:
        ct.append(k * (c - 18) % 256)
    return bytes(ct)


f = open('msg.enc', 'r')
c = bytes.fromhex(f.read())
ct = decryption(c)
print(ct)
f.close()
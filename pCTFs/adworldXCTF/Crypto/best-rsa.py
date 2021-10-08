# https://crypto.stackexchange.com/questions/81807/how-to-recover-a-message-with-shared-modulus-for-textbook-rsa/81829#81829
# Bézout's identity — Let a and b be integers with greatest common divisor d. Then there exist integers x and y such that ax + by = d. More generally, the integers of the form ax + by are exactly the multiples of d.
from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long, GCD
from Crypto.PublicKey import RSA

def GCDExtended(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = GCDExtended(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


f = open('publickey1.pem', 'r')
key1 = RSA.importKey(f.read())
f.close()

f = open('publickey2.pem', 'r')
key2 = RSA.importKey(f.read())
f.close()

f = open('cipher1.txt', 'rb')
c1 = bytes_to_long(f.read())
f.close()

f = open('cipher2.txt', 'rb')
c2 = bytes_to_long(f.read())
f.close()

g, a, b = GCDExtended(key1.e, key2.e)
# print(a, b)
n = key1.n

if (a < 0):
    swap(a, b)

i = inverse(c2, n)
m = (pow(c1, a, n) * pow(i, -b, n)) % n
print(long_to_bytes(m))

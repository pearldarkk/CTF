import binascii
import hashlib
from Crypto.Cipher import AES
import itertools
import string

enc = "9**********b4381646*****01********************8b9***0485******************************0**ab3a*cc5e**********18a********5383e7f**************1b3*******9f43fd66341f3ef3fab2bbfc838b9ef71867c3bcbb"
size = 16


def xor(a: bytes, b: bytes) -> bytes:
    return bytes(a_i ^ b_i for a_i, b_i in zip(a, b))


def pad(msg):
    padding = bytes((size - len(msg) % size) * chr(size - len(msg) % size),
                    encoding='utf-8')
    return msg + padding


for i, j, k in itertools.permutations(string.printable, 3):
    key = i.encode() + b"XhN2" + j.encode() + b"8d%8Slp3" + k.encode() + b"v"
    h = hashlib.sha256(key).hexdigest()
    hidden = binascii.unhexlify(h)[:10]

    message = b'CBC (Cipher Blocker Chaining) is an advanced form of block cipher encryption' + hidden
    message = pad(message)
    aes = AES.new(key, AES.MODE_ECB)
    dec = aes.decrypt(binascii.unhexlify(enc[-32:]))
    if xor(dec[-5:], binascii.unhexlify(enc[-42:-32])) == message[-5:]:
        break

enc_full = binascii.unhexlify(enc[-32:])
while message:
    dec = aes.decrypt(enc_full[:16])
    enc_full = xor(message[-16:], dec) + enc_full
    message = message[:-16]

flag = "TMUCTF{" + enc_full[:16].decode() + "}"
print(flag)
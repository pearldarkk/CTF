from Crypto.Util.number import long_to_bytes
from pwn import xor
import string

f = open('output.txt', 'rb')
l = f.readlines()
klen = int(l[0].split()[-1])
cipher = long_to_bytes(int(l[1].split()[-1], base=16))
f.close()

# xortool -x -l 32 -o -f -p Thomas hex.txt

plain = b'Looked back at his captors, feeling awkward but desperate to ask questions. Captors,'

for i in range(0, 32):
    key = xor(plain[0:32], cipher[0:32])

cipher = xor(key, cipher)

f = open('text.out', 'wb')
f.write((cipher))
f.close()
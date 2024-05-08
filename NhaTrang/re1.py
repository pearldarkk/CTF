import pwn 
import binascii as bin

with open('NhaTrang\enc.txt', 'r') as f:
    enc = f.read().strip()
enc = bin.unhexlify(enc)
dec = pwn.xor(enc, "Fsoft")
print(dec)

# NhaTrang{hello_from_h3ll}
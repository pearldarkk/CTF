#ssh to pem: ssh-keygen -f bruce.pub -m 'PEM' -e > bruce.pem
from Crypto.PublicKey import RSA

f = open('bruce.pem', 'r')
k = RSA.importKey(f.read())
print(k.n)
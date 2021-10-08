from Crypto.PublicKey import RSA

f = open('privacy.pem', 'r')
key = RSA.importKey(f.read())

print(key.d)

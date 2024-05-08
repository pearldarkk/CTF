from Crypto.PublicKey import RSA

f = open('certain.pem', 'r')

key = RSA.importKey(f.read())

print(key.n)

# decode: openssl x509 -inform der -in certain.der -text -noout
# convert to pem: openssl x509 -inform der -in certain.der -out certain.pem
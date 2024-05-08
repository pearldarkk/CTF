from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long

n = 76775333340223961139427050707840417811156978085146970312315886671546666259161
p = 280385007186315115828483000867559983517
q = 273821108020968288372911424519201044333
e = 0x10001

f = open('fllllllag.txt', 'rb')
c = bytes_to_long(f.read())

d = inverse(e, (p - 1) * (q - 1))
m = pow(c, d, n)
print(long_to_bytes(m))

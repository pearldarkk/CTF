def lfsr(R, mask):
    output = (R << 1) & 0xffffff
    i = (R & mask) & 0xffffff
    lastbit = 0
    while i != 0:
        lastbit ^= (i & 1)
        i = i >> 1
    output ^= lastbit
    return (output, lastbit)


f = open("key", "rb")
cipher = f.read()
mask = 0b1010011000100011100

for k in range(2**18, 2**19):
    R = k
    c = b''
    for i in range(3):
        tmp = 0
        for j in range(8):
            (R, out) = lfsr(R, mask)
            tmp = (tmp << 1) ^ out
        c += bytes([tmp])
    if c == cipher[:3]:
        print('flag{', bin(k)[2:], '}', sep='')
        break

f.close()
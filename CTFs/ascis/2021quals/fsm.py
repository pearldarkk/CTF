def __ROR__(num, count, bits=32):
    return ((num >> count) | (num << (bits - count))) & ((0b1 << bits) - 1)

for c in range(256):

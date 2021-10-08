from base64 import b32decode

s = 'MZYVMIWLGBL7CIJOGJQVOA3IN5BLYC3NHI'
b32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'

# x = (5y + 12) % 32
msg = ''.join([b32[(5 * b32.find(x) + 12) % 32] for x in s])

print(b32decode(msg + '=' * (8 - len(msg) % 8)))

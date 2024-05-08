cipher = 'izwhroz""w"v.K".Ni'
key = 0x12
flag = ''
for i in range(0, len(cipher), 3):
    flag += chr((ord(cipher[i]) ^ key) - 6)
    flag += chr((ord(cipher[i + 1]) ^ key) + 6)
    flag += chr((ord(cipher[i + 2]) ^ key) ^ 6)
print(flag)
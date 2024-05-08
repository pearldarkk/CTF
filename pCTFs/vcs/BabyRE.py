from pwn import xor

bytes = [
    98, 100, 110, 112, 81, 97, 105, 124, 110, 117, 102, 105, 109, 110, 117,
    103, 96, 110, 123, 70, 97, 102, 104, 114, 87, 4
]
flag = b"flag{"
key = b""
for i in range(5):
    key += xor(flag[i], bytes[i])[0:1]

for i in range(5, len(bytes)):
    flag += xor(key[i % 5], bytes[i])

print(flag)

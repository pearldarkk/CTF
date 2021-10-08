bytes = [
    7, 9, 19, 5, 262, 182, 33, 112, 134, 12, 136, 55, 309, 33, 239, 84, 405,
    55, 121, 84, 215, 33, 134, 12, 239, 33, 23, 239, 23, 379, 309, 37, 41, 0
]

tri = [0 for _ in range(max(bytes)+1)]
tri[1] = 1
tri[2] = 2

for i in range(3, max(bytes) + 1):
    tri[i] = tri[i - 3] * 17 + 3 * tri[i - 2] + 75 * tri[i - 1]

flag = ''
for i in bytes:
    flag += chr(tri[i] & 0xFF)

print(flag)

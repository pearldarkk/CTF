from base64 import b64decode

semi = 's0ntq3TInhmZnJrFmvnFnf85CJbvuf8WzL9Imu40uNKTnZaTnZn4n18ZtMmWrdfUov9tq0GZttmYFq=='
cipher = ''
for i in range(len(semi)):
    if 'A' <= semi[i] <= 'Z':
        cipher += chr(ord(semi[i]) + 0x20)
    elif 'a' <= semi[i] <= 'z':
        cipher += chr(ord(semi[i]) - 0x20)
    else:
        cipher += semi[i]
print(cipher)
flag = str(b64decode(cipher))
print(flag[2:len(flag) - 1])

a = [118, 104, 102, 120, 117, 108, 119, 124, 48, 123, 101, 120]
token = ''
for i in a:
    token += chr(i - 3)
print(token)
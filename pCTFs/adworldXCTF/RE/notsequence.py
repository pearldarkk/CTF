import hashlib 
# Pascal Triangle
a = []
for i in range(21):
    value = 0
    for j in range(i):
        index = (i-1) * (i-2) // 2 
        if j == 0 or j == i-1: 
            value = 1
        else: 
            value = a[index+j-1] + a[index+j]
        a.append(value)
        # print(value, end=' ')
    # print()

flag = ''
for i in a:
    flag += str(i)
# print(flag)
md = hashlib.md5(flag.encode())
print(md.hexdigest())


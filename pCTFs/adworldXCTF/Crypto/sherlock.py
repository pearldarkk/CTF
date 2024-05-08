f = open("sherlock.txt", "r")
cipher = f.read()
flag = ''

for i in cipher:
    if ord('A') <= ord(i) <= ord('Z'):
        flag += i

print(flag)
print()
flag = flag.replace('ZERO', '0')
flag = flag.replace('ONE', '1')
print(flag)
f.close()

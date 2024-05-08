p = 29
ints = [14, 6, 11]

for i in ints:
    for a in range(p):
        if (a * a) % p == i:
            print(a, i) 
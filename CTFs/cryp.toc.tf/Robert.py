from sympy.ntheory import reduced_totient

n = 1164273510

for i in range(n, 100000000000000):
    if reduced_totient(i) == n:
        print(i)
        break

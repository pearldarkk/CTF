from Crypto.Util.number import inverse
from functools import reduce
# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17
# k = (3 - 2) * inverse(5, 11) % 11
# x = 2 + 5 * k
# k = (5 - x) * inverse(5 * 11, 17) % 17
# x = x + 5 * 11 * k
# print(x)


def crt(a, n):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * inverse(p, n_i) * p
    return sum % prod


A = [2, 3, 5]  # x = a mod x
M = [5, 11, 17]  # x = x mod n
print(crt(A, M))
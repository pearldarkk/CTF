from Crypto.Util.number import inverse
# https://cp-algorithms.com/algebra/module-inverse.html
k = inverse(3, 13)
print(k)

# A modular multiplicative inverse of an integer a is an integer x such that a⋅x is congruent to 1 modular some modulus m. To write it in a formal way: we want to find an integer x so that
# a ⋅ x ≡ 1 (mod m)
# We will also denote x simply with a^−1.
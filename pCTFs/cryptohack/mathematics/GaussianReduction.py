def lagrange(b1, b2):
    mu = 1
    while mu != 0:
        mu = round((b1 * b2) / (b1 * b1))
        b2 -= mu * b1
        if b1 * b1 > b2 * b2:
            b1, b2 = b2, b1
    return b1, b2

if __name__ == '__main__':
    v = (846835985, 9834798552)
    u = (87502093, 123094980)
    print(lagrange(u, v))
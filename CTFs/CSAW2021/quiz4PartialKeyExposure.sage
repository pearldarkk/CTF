# usr/bin/sage

def partial_p(p0, kbits, n):
    PR.<x> = PolynomialRing(Zmod(n))
    nbits = n.nbits()
    f = 2^kbits*x + p0
    f = f.monic()
    roots = f.small_roots(X=2^(nbits//2-kbits), beta=0.3)  # find root < 2^(nbits//2-kbits) with factor >= n^0.3
    if roots:
        x0 = roots[0]
        p = gcd(2^kbits*x0 + p0, n)
        return ZZ(p)
def find_p(d0, kbits, e, n):
    X = var('X')
    for k in range(1, e+1):
        results = solve_mod([e*d0*X - k*X*(n-X+1) + k*n == X], 2^kbits)
        for x in results:
            p0 = ZZ(x[0])
            p = partial_p(p0, kbits, n)
            if p:
                return p
if __name__ == '__main__':
    n = 61354328725009110904662716659275242271539889771836075265120152113937032313555999117290122334833702089021667071225349870242496497666062752197929262832754362704460251233727815272161214664274657287725743695980286290326940956179914439969975329836770894979963849511231067481448088547959309648091922398434312801709
    e = 17
    d = 6393405926571965174437427296225243708127507777129441993689620203971856563385166021940469533780346193122725442072543477661100605090969221838194389428902929
    beta = 0.5
    epsilon = beta^2/7
    nbits = n.nbits()
    # print ("nbits:%d:"%(nbits))
    # kbits = floor(nbits*(beta^2+epsilon))
    kbits = nbits - d.nbits()-1
    # print ("kbits:%d"%(kbits))
    d0 = d & (2^kbits-1)
    # print ("lower %d bits (of %d bits) is given" % (kbits, nbits))
    p = find_p(d0, kbits, e, n)
    # print ("found p: %d" % p)
    q = n//p
    # print (d)
print(inverse_mod(e, (p-1)*(q-1)))
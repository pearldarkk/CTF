
#include <stdio.h>
#include <stdlib.h>

// The number of bits in p and q; this should be a multiple of 64.
#define pbits 512
#define pwords pbits / 64

// We'll use 64-bit limbs.  Only fancy machines need apply.
typedef unsigned int u64 __attribute__((mode(DI)));
typedef unsigned int u128 __attribute__((mode(TI)));

// Low word is low, low bit is low.
static u64 n[2 * pwords];

static u64 e = 65537;

static struct {
    u64 p[2 * pwords];
    u64 q[2 * pwords];
    u64 d[2 * pwords];
    u64 d_p[2 * pwords];
    u64 d_q[2 * pwords];
} dat, known, mask;

static u64 k, k_p, k_q;

// We build up p bit by bit.  We then track:
static struct {
    u64 nn[pwords + 1]; // p*q div 2**bit
    u64 d1[pwords + 1]; // 1+k(p-1)(q-1) div 2**bit
    u64 dp1;            // 1+k_p(p-1) div 2**bit
    u64 dq1;            // 1+k_q(q-1) div 2**bit
    u64 d2;             // d*e div 2**bit
    u64 dp2;            // d_p*e div 2**bit
    u64 dq2;            // d_q*e div 2**bit
} search;

static u64 bit;

// Some bignum utility things.

static u64 getbit(u64 *x, u64 n) {
    return (x[n / 64] >> (n % 64)) & 1;
}

static void setbit(u64 *x, u64 n) {
    x[n / 64] |= (u64)1 << (n % 64);
}

static void clrbit(u64 *x, u64 n) {
    x[n / 64] |= (u64)1 << (n % 64);
    x[n / 64] ^= (u64)1 << (n % 64);
}

// d has an extra limb.
static void bn_add(u64 *d, u64 *a, u64 n) {
    u64 j;

    u128 c = 0;
    for (j = 0; j < n; j++) {
        c = c + d[j] + a[j];
        d[j] = c;
        c >>= 64;
    }

    d[n] += c;
}

static void bn_sub(u64 *d, u64 *a, u64 n) {
    u64 j;

    u128 c = 1;
    for (j = 0; j < n; j++) {
        c = c + d[j] + ~a[j];
        d[j] = c;
        c >>= 64;
    }

    d[n] += c - 1;
}

static void bn_double(u64 *d, u64 n) {
    u64 j;

    u128 c = 0;
    for (j = 0; j < n; j++) {
        c = c + d[j] + d[j];
        d[j] = c;
        c >>= 64;
    }
}

static void bn_halve(u64 *d, u64 n) {
    u64 j;

    u128 c = 0;
    for (j = n - 1; j < n; j--) {
        c = (c << 64) + d[j];
        d[j] = c >> 1;
    }
}

// d += k*(a-1); a is odd, d has an extra limb.
static void bn_update_de(u64 *d, u64 *a, u64 k, u64 n) {
    u64 j;

    u128 c = -(u128)k;
    for (j = 0; j < n; j++) {
        c = c + d[j] + (u128)k * a[j];
        d[j] = c;
        c >>= 64;
    }

    d[n] += c;
}

static void bn_update_de_m(u64 *d, u64 *a, u64 k, u64 n) {
    u64 j;

    u128 c = 2 * k;
    for (j = 0; j < n; j++) {
        c = c + d[j] + (u128)k * ~a[j];
        d[j] = c;
        c >>= 64;
    }

    d[n] += c - k;
}

static void bn_print(u64 *d, u64 n) {
    u64 j, k;

    for (j = n - 1; j < n; j--) {
        u64 x = d[j];

        for (k = 0; k < 16; k++) {
            fputc("0123456789abcdef"[x >> 60], stdout);
            x <<= 4;
        }
    }

    fputc('\n', stdout);
}

// This is where the real work happens.
static void try(void) {
    // Set the bit of d, d_p, d_q if it is needed for its equation
    // to hold.
    if ((search.d1[0] ^ search.d2) & 1) {
        setbit(dat.d, bit);
        search.d2 += e;
    }

    if ((search.dp1 ^ search.dp2) & 1) {
        setbit(dat.d_p, bit);
        search.dp2 += e;
    }

    if ((search.dq1 ^ search.dq2) & 1) {
        setbit(dat.d_q, bit);
        search.dq2 += e;
    }

    // If any bit is prescribed and we don't match that value, prune.
    if (getbit(mask.p, bit) && getbit(dat.p, bit) != getbit(known.p, bit))
        goto out;

    if (getbit(mask.q, bit) && getbit(dat.q, bit) != getbit(known.q, bit))
        goto out;

    if (getbit(mask.d, bit) && getbit(dat.d, bit) != getbit(known.d, bit))
        goto out;

    if (getbit(mask.d_p, bit) && getbit(dat.d_p, bit) != getbit(known.d_p, bit))
        goto out;

    if (getbit(mask.d_q, bit) && getbit(dat.d_q, bit) != getbit(known.d_q, bit))
        goto out;

    // Save our low bits, we'll need them back when backtracking.
    u64 nn_low = search.nn[0] & 1;
    u64 d_low = search.d2 & 1;
    u64 dp_low = search.dp2 & 1;
    u64 dq_low = search.dq2 & 1;

    bit++;

    // Shift the low bits out.
    bn_halve(search.nn, pwords + 1);
    bn_halve(search.d1, pwords + 1);
    search.d2 /= 2;
    search.dp1 /= 2;
    search.dp2 /= 2;
    search.dq1 /= 2;
    search.dq2 /= 2;

    // Oh happy days.
    if (bit == 2 * pbits) {
        printf("=== FOUND IT ===\n");

        bn_print(n, 2 * pwords);
        bn_print(dat.p, pwords);
        bn_print(dat.q, pwords);
        bn_print(dat.d, 2 * pwords);
        bn_print(dat.d_p, pwords);
        bn_print(dat.d_q, pwords);

        goto found;
    }

    // Should the current bits of p and q be equal?  This holds exactly
    // then if the bit of the n we build up matches the real n.
    int pqequal = ((search.nn[0] & 1) == getbit(n, bit));

    // p=0 q=0, recurse.
    if (pqequal)
        try();

    // p=1 q=0, recurse.
    setbit(dat.p, bit);
    bn_add(search.nn, dat.q, pwords);
    bn_update_de(search.d1, dat.q, k, pwords);
    search.dp1 += k_p;

    if (!pqequal)
        try();

    // p=1 q=1, recurse.
    setbit(dat.q, bit);
    bn_add(search.nn, dat.p, pwords);
    bn_update_de(search.d1, dat.p, k, pwords);
    search.dq1 += k_q;

    if (pqequal)
        try();

    // p=0 q=1, recurse.
    clrbit(dat.p, bit);
    bn_sub(search.nn, dat.q, pwords);
    bn_update_de_m(search.d1, dat.q, k, pwords);
    search.dp1 -= k_p;

    if (!pqequal)
        try();

    // And finally restore to pristine state.
    clrbit(dat.q, bit);
    bn_sub(search.nn, dat.p, pwords);
    bn_update_de_m(search.d1, dat.p, k, pwords);
    search.dq1 -= k_q;

found:;
    // Put the low bits back.
    bn_double(search.nn, pwords + 1);
    search.nn[0] += nn_low;
    bn_double(search.d1, pwords + 1);
    search.d1[0] += d_low;
    search.d2 = 2 * search.d2 + d_low;
    search.dp1 = 2 * search.dp1 + dp_low;
    search.dp2 = 2 * search.dp2 + dp_low;
    search.dq1 = 2 * search.dq1 + dq_low;
    search.dq2 = 2 * search.dq2 + dq_low;

    bit--;

out:;
    // Restore d, d_p, d_q.
    if (getbit(dat.d, bit)) {
        clrbit(dat.d, bit);
        search.d2 -= e;
    }

    if (getbit(dat.d_p, bit)) {
        clrbit(dat.d_p, bit);
        search.dp2 -= e;
    }

    if (getbit(dat.d_q, bit)) {
        clrbit(dat.d_q, bit);
        search.dq2 -= e;
    }

    return;
}

// Try everything for a fixed k.
static void try_k(void) {
    // Compute k/e*n.  Let's use the dumb and simple way, with
    // a big fat division.
    u64 d[2 * pwords];
    u64 j;

    u128 c = 0;
    for (j = 0; j < 2 * pwords; j++) {
        c += (u128)k * n[j];
        d[j] = c;
        c >>= 64;
    }
    for (j = 2 * pwords - 1; j < 2 * pwords; j--) {
        c = (c << 64) + d[j];
        d[j] = c / e;
        c %= e;
    }

    // This should agree with d in the top half minus one of the bits,
    // except when carries happen.  Leave a full word of slack, that
    // should be enough for all practical purposes.  We *could* also
    // detect which bits can carry and not compare them.
    for (j = pwords + 1; j < 2 * pwords; j++)
        if ((d[j] ^ known.d[j]) & mask.d[j])
            return;

    // Our k is good.  Now find p, q, k_p, k_q mod e.

    // Find k^{-1} mod e.
    u64 kinv;
    for (kinv = 1; kinv < e; kinv++)
        if (kinv * k % e == 1)
            break;

    // Find n mod e.  This uses the fact that 2^64 = 1 mod e.
    u64 ne = 0;
    for (j = 0; j < 2 * pwords; j++)
        ne += (n[j] % e);
    ne %= e;

    // de = 1 + k(p-1)(q-1)  so  p + q = n + 1 + k^{-1} mod e.
    // Loop over all such pairs p,q mod e.
    u64 pe, qe = (kinv + ne) % e;
    for (pe = 1; pe < e; pe++) {
        // Does that satisfy pq = n?
        if ((pe * qe) % e == ne) {
            // Find k_p, k_q.
            // d_p e = 1 + k_p(p-1)  so  k_p p = k_p - 1 mod e.
            for (k_p = 1; k_p < e; k_p++)
                if ((k_p * pe) % e == k_p - 1)
                    break;

            for (k_q = 1; k_q < e; k_q++)
                if ((k_q * qe) % e == k_q - 1)
                    break;

            //printf("k=%d k_p=%d k_q=%d\n", (int)k, (int)k_p, (int)k_q);

            // Both p and q start at 1.
            dat.p[0] = dat.q[0] = 1;
            search.nn[0] = search.d1[0] = search.dp1 = search.dq1 = 1;

            // Work!
            try();
        }

        qe = (qe + e - 1) % e;
    }
}

// All I/O is ugly.
static void read_number(u64 *num, u64 nwords) {
    u64 j, k;
    for (k = nwords - 1; k < nwords; k--) {
        for (j = 0; j < 16; j++) {
            u64 c = fgetc(stdin);
            if (c >= '0' && c <= '9')
                num[k] = 16 * num[k] + c - '0';
            else if (c >= 'a' && c <= 'f')
                num[k] = 16 * num[k] + c - 'a' + 10;
            else
                goto fail;
        }
    }
    if (fgetc(stdin) != '\n')
    fail : {
        fprintf(stderr, "bad input, you lose.\n");
        exit(1);
    }
}

int main(void) {
    read_number(n, 2 * pwords);

    read_number(known.p, pwords);
    read_number(known.q, pwords);
    read_number(known.d, 2 * pwords);
    read_number(known.d_p, pwords);
    read_number(known.d_q, pwords);

    read_number(mask.p, pwords);
    read_number(mask.q, pwords);
    read_number(mask.d, 2 * pwords);
    read_number(mask.d_p, pwords);
    read_number(mask.d_q, pwords);

    u64 j;
    for (j = pwords; j < 2 * pwords; j++) {
        mask.p[j]--;
        mask.q[j]--;
        mask.d_p[j]--;
        mask.d_q[j]--;
    }

    for (k = 1; k < e; k++)
        try_k();

    return 0;
}
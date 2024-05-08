#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define P(x) printf("%d", x)
#define S(x) scanf("%d", &x)
#define EL printf("\n")
#define Fill(a, x) memset(a, x, sizeof a)
#define MOD 1000000007LL
#define INF 1e9
#define LINF 1e18
#define ld long double
#define ll long long
#define ull unsigned long long

int main() {
    freopen("text.inp", "r", stdin);
    //freopen("text.out", "w", stdout);
    char v[16];
    v[2] = 102;
    v[3] = 109;
    v[4] = 99;
    v[5] = 100;
    v[6] = 127;
    v[7] = 107;
    v[8] = 55;
    v[9] = 100;
    v[10] = 59;
    v[11] = 86;
    v[12] = 96;
    v[13] = 59;
    v[14] = 110;
    v[15] = 112;
    for (int i = 2; i < 17; ++i) {
        v[i] ^= i - 2;
        printf("%c", v[i]);
    }
    return 0;
}
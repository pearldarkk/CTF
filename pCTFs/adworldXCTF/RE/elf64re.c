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
    char v3[3][9] = {"Dufhbmf", "pG`imos", "ewUglpt"};
    char buf[12];
    for (int i = 0; i <= 11; ++i)
        *(char *)(i + buf) = v3[i % 3][2 * (i / 3)] - 1;
    puts(buf);
    return 0;
}
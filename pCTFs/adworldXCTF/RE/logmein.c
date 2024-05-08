#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    char v8[] = {":\"AL_RT^L*.?+6/46"};
    char v7[] = {0x68, 0x61, 0x72, 0x61, 0x6D, 0x62, 0x65};
    for (int i = 0; i < strlen(v8); ++i)
        v8[i] ^= v7[i % 7];
    puts(v8);
    return 0;
}
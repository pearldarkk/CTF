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
    char s[32];
    s[0] = 95 ^ 20;
    s[1] = 87 ^ 20;
    s[2] = 'S';
    s[3] = 71 ^ 4;
    s[4] = 60 ^ 71;
    //
    s[5] = 60 ^ 80;
    s[6] = 59 ^ 15;
    s[7] = 100 ^ 47;
    s[8] = 27 ^ 47;
    s[9] = 127 ^ 27;
    s[11] = 32 ^ 109;
    s[10] = s[11] ^ 127 ^ 109;
    s[12] = 89 ^ 109;
    s[13] = 45 ^ 89;
    s[15] = 76 ^ 56;
    s[16] = 56 ^ 12;
    s[17] = 107 ^ 12;
    s[18] = 93 ^ 107;
    s[20] = 32 ^ s[17];
    s[21] = s[18] ^ 75;
    s[19] = 93 ^ s[20] ^ s[21];
    s[14] = s[21] ^ s[20] ^ s[19] ^ s[18] ^ s[17] ^ s[16] ^ s[15] ^ 45;
    s[22] = 0;
    puts(s);
    return 0;
}
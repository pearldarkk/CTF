#include <stdio.h>
#include <math.h>
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
    char Buf1[0x18];
    Buf1[0] = -124;
    Buf1[1] = -116;
    Buf1[2] = -100;
    Buf1[3] = -116;
    Buf1[4] = -76;
    Buf1[5] = -112;
    Buf1[6] = -112;
    Buf1[7] = -69;
    Buf1[8] = -93;
    Buf1[9] = -6;
    Buf1[10] = -112;
    Buf1[11] = -112;
    Buf1[12] = -84;
    Buf1[13] = -82;
    Buf1[14] = -125;
    Buf1[15] = -125;
    Buf1[16] = -9;
    Buf1[17] = -114;
    Buf1[18] = -116;
    Buf1[19] = -73;
    Buf1[20] = -112;
    Buf1[21] = -112;
    Buf1[22] = -78;
    for (int i = 0; i <= 22; ++i)
        printf("%c", Buf1[i] ^ 0xCF);
    EL;
    return 0;
}
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
    int a2[] = {0x01, 0x02, 0x03, 0x04, 0x05, 0};
    int s[] = {0x3A, 0x36, 0x37, 0x3B, 0x80, 0x7A, 0x71, 0x78, 0x63, 0x66, 0x73, 0x67, 0x62, 0x65, 0x73, 0x60, 0x6B, 0x71, 0x78, 0x6A, 0x73, 0x70, 0x64, 0x78, 0x6E, 0x70, 0x70, 0x64, 0x70, 0x64, 0x6E, 0x7B, 0x76, 0x78, 0x6A, 0x73, 0x7B, 0x80, 0};

    for (int i = 0; i < 38; ++i) {
        s[i] -= a2[i % 5];
        printf("%c", (char)s[i]);
    }

    return 0;
}
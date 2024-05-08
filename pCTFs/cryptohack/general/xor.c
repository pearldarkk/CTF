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
    char c[] = "label";
    for (int i = 0; i < strlen(c); ++i)
        printf("%c", c[i] ^ 13);
    return 0;
}
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
    int v2[] = {0xBB, 0xAA, 0xCC, 0xDD};
    char byte[] = "\xbb\xcc\xa0\xbc\xdc\xd1\xbe\xb8\xcd\xcf\xbe\xae\xd2\xc4\xab\x82\xd2\xd9\x93\xb3\xd4\xde\x93\xa9\xd3\xcb\xb8\x82\xd3\xcb\xbe\xb9\x9a\xd7\xcc";
    for (int i = 0; i < 36; ++i){
        byte[i] ^= v2[i % 4];
        printf("%c", byte[i]);
    }
    return 0;
}
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define EL printf("\n")
#define MOD 1000000007LL
#define INF 1e9
#define LINF 1e18
#define ld long double
#define ll long long
#define ull unsigned long long

int main() {
    freopen("text.inp", "r", stdin);
    //freopen("text.out", "w", stdout);
    char s[] = "WikwaMgss[9}?_}>~VMZgJ%Wk`g";
    for (int i = 0; i < strlen(s); ++i)
        s[i] ^= i;
    puts(s);
    return 0;
}
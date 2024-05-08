#include <stdio.h>
#include <math.h>
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
    //func lol anti decompile, must patch cmp     [ebp+var_C], 1 -> 0 to make it right
    char v2[8]; // [esp+15h] [ebp-13h] BYREF
    char a1[] = "69800876143568214356928753";
    v2[0] = 2 * a1[1];
    v2[1] = a1[4] + a1[5];
    v2[2] = a1[8] + a1[9];
    v2[3] = 2 * a1[12];
    v2[4] = a1[18] + a1[17];
    v2[5] = a1[10] + a1[21];
    v2[6] = a1[9] + a1[25];
    v2[8] = 0;
    printf("%s", v2);
    return 0;
}
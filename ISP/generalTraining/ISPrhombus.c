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
    // freopen("text.inp", "r", stdin);
    freopen("text.out", "w", stdout);

    char isp[] = {"ISP"};
    int k;
    int n;
    scanf("%d", &n);
    for (int i = 1; i < 2 * n; ++i) {
        k = abs(n - i) + 1;
        for (int j = 1; j < 2 * n; ++j)
            if (j < k || j > 2 * n - k)
                printf(" ");
            else if (j <= n)
                printf("%c", isp[(j - k) % 3]);
            else
                printf("%c", isp[(2 * n - k - j) % 3]);
        printf("\n");
    }

    return 0;
}
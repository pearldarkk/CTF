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

char buf[129];
char buf2[128 * 3], buf3[128 * 3];
int pos[128 * 2];
int tt = 0;
char const ca[] = "0123456789abcdef";

void dfs(int x) {
    if (x >= 128 * 2)
        return;
    dfs(x * 2 + 1);
    pos[tt++] = x;
    dfs(++x * 2);
}

int main() {
    freopen("flag.enc", "r", stdin);
    freopen("text.out", "w", stdout);
    buf[128] = 0;
    buf2[128 * 2] = 0;
    buf3[128 * 2] = 0;

    fgets(buf3, 128 * 2, stdin);

    dfs(0);
    // for (int i = 0; i < 128*2; ++i)
    //     printf("%d:%d\n", i, pos[i]);

    for (int i = 0; i < 128 * 2; ++i)
        buf2[pos[i]] = buf3[i];

    //c2w
    for (int i = 0; i < 128; ++i) {
        for (int j = 0; j < 2; ++j)
            if (buf2[i * 2 + j] <= '9')
                buf2[i * 2 + j] -= '0';
            else
                buf2[i * 2 + j] -= 'a' - 10;
        buf[i] = (buf2[i * 2] << 4) + buf2[i * 2 + 1];
    }
    // for (int i = 0; i < 128 * 2; ++i)
    //     printf("%x ", buf2[i]);
    // EL;

    //encode
    for (int i = 128 - 1; i >= 0; --i) {
        if (i % 8 != 0)
            buf[i] ^= buf[i - 1];
        if (i / 8 != 0)
            buf[i] ^= buf[i - 8];
    }
    // for (int i = 0; i < 128; ++i)
    //     printf("%x ", buf[i]);

    //mInit
    char brute[128];
    for (int len = 1; len < 128; ++len) {
        memset(brute, 0, 128);
        for (int i = 0; i < len; ++i)
            brute[i] = len ^ buf[i];
        puts(brute);
    }
    //Th15_lS_@_easy_ASM
    return 0;
}
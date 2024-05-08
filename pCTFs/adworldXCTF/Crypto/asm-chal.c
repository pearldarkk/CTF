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
int len;
int tt;

void mInit() {
    len = strlen(buf);
    for (int i = 0; i < 128; ++i)
        buf[i] = buf[i % len] + i / len;
    for (int i = 0; i < 128; ++i)
        buf[i] ^= len;
}

void Encode() {
    for (int i = 0; i < 128; ++i) {
        if (i % 8 != 0)
            buf[i] ^= buf[i - 1];
        if (i / 8 != 0)
            buf[i] ^= buf[i - 8];
    }
}

char ca[] = "0123456789abcdef";
void c2w() {
    for (int i = 0; i < 128; ++i) {
        buf2[i * 2] = ca[(buf[i] & 0b11110000) >> 4];
        buf2[i * 2 + 1] = ca[buf[i] & 0b1111];
    }
}

void dfs(int x) {
    if (x >= 128 * 2)
        return;
    dfs(x * 2 + 1);
    buf3[tt++] = buf2[x];
    dfs(++x * 2);
}

int main() {
    // freopen("text.inp", "r", stdin);
    // freopen("test.out", "w", stdout);
    fgets(buf, 128, stdin);

    buf[128] = 0;
    buf2[128 * 2] = 0;
    buf3[128 * 2] = 0;
    mInit();
    // for (int i = 0; i < 128; ++i)
    //     printf("%x ", buf[i]);
    puts(buf);

    Encode();
    // for (int i = 0; i < 128; ++i)
    //     printf("%x ", buf[i]);
    // EL;

    c2w();
    // for (int i = 0; i < 128*2; ++i)
    //     printf("%x ", buf2[i]);
    // puts(buf2);
    dfs(0);
    puts(buf3);
    return 0;
}
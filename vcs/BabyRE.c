#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ROR(x, y) ((unsigned)(x) >> (y) | (unsigned)(x) << (32 - (y)))
#define EL printf("\n")
#define MOD 1000000007LL
#define INF 1e9
#define LINF 1e18
#define ld long double
#define ll long long
#define ull unsigned long long

char buf[6];
char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

void backtrack(int pos) {
    if (pos == 5) {
        char v8[] = {0x4, 0x57, 0x72, 0x68, 0x66, 0x61, 0x46, 0x7b, 0x6e, 0x60, 0x67, 0x75, 0x6e, 0x6d, 0x69, 0x66, 0x75, 0x6e, 0x7c, 0x69, 0x61, 0x51, 0x70, 0x6e, 0x64, 0x62};
        int v6;
        char *v5;
        for (int j = 24; j >= 0; j -= 2) {
            v5 = (char *)&v8 + j;
            *v5 ^= buf[j % 5u];
            // if (*v5 <= '0' || *v5 >= 'z')
            //     return;
            v6 = j;
            v5[1] ^= buf[v6 - 5 * ((j + 1) / 5) + 1];
            // if (v5[1] <= '0' || v5[1] >= 'z')
            //     return;
        }
        if (!strncmp("flag{", v8, 5))
            printf("%s: %s\n", buf, v8);
        return;
    }
    for (char i = 0; i < 63; ++i) {
        buf[pos] = charset[i];
        backtrack(pos + 1);
    }
}

int main() {
    // freopen("text.inp", "r", stdin);
    freopen("text.out", "w", stdout);
    backtrack(0);
    return 0;
}
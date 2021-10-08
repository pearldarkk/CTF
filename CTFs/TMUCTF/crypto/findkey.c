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
    int a[4];
    a[1] = 0xF23A4BDA;
    a[2] = 0xD5EAE2D4;
    // int flg = 0;
    // for (a[0] = 0x11111111; a[0] <= 0xFFFFFFFF; ++a[0]) {
    //     a[3] = (0x455D304E - 2 * a[0]) / 2;
    //     if (2 * (2 * a[3] + 2 * a[0]) + a[0] == 0xE429D014 && 4 * (a[0] - 0xA85474B) + 2 * (2 * a[3] + 2 * a[0]) == 0xC6630150) {
    //         flg = 1;
    //         break;
    //     }
    // }

    // for (int i = 0; i < 4; ++i)
    //     printf("%x\n", a[i]);
    a[0] = 0x596f6f78;
    a[3] = 0xc93f28af; //0xc93f28af 0x493f28af
    
    int v5[4];
    v5[0] = 0x5a06d37b;
    v5[1] =  0xda50d53c;
    v5[2] =  0x9482d063;
    v5[3] =  0xc61e42ca; //461e42ca
    // for (int j = 0; j < 4; ++j)
    //     for (unsigned int i = 0xFFFFFFFF; i >= 0x30303030; --i) {
    //         int v8 = i ^ (i << 7);
    //         int v7 = (unsigned char)(v8 >> 1) + v8;
    //         if (a[j] == v7) {
    //             v5[j] = i;
    //             break;
    //         }
    //     }
    // for (int i = 0; i < 4; ++i)
    //     printf("%x\n", v5[i]);
    // exit(0);

    int flag[4] = {};
    int tmp[4];
    for (int i = 0; i < 4; ++i)
        for (unsigned int j = 0x20202020; j <= 0x7d7d7d7d; ++j) {
            tmp[3] = (((j >> 3) & 0x20000000) + 32 * j) ^ j;
            tmp[2] = tmp[3] ^ (tmp[3] << 7);
            tmp[1] = (unsigned char)(tmp[2] >> 1) + tmp[2];
            tmp[0] = tmp[1] ^ (((tmp[1] >> 3) & 0x20000000) + 32 * tmp[1]);
            if (v5[i] == tmp[0]) {
                flag[i] = j;
                break;
            }
        }
    for (int i = 3; i >= 0; --i)
        printf("%x", flag[i]);
    // flag in hex form, reversed
    return 0;
}
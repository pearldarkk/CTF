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
    char s[] = {0xF3, 0x04, 0x05, 0x10, 0x01, 0xE4, 0xFD, 0x10, 0x17, 0xE0, 0xCF, 0xFF, 0x0E, 0x15, 0x0C, 0x10, 0xFB, 0x09, 0x01, 0xFB, 0xFD, 0x04, 0x05, 0x04, 0x05, 0x19};
    char bytes[] = {0x64, 0x64, 0x9C, 0x64};
    for (int i = 0; i < strlen(s); ++i)
        s[i] ^= bytes[i % 4];
    puts(s);
    return 0;
}
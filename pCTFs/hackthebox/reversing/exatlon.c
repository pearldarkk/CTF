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
    int c[] = {1152, 1344, 1056, 1968, 1728, 816, 1648, 784, 1584, 816, 1728, 1520, 1840, 1664, 784, 1632, 1856, 1520, 1728, 816, 1632, 1856, 1520, 784, 1760, 1840, 1824, 816, 1584, 1856, 784, 1776, 1760, 528, 528, 2000};
    for (int i = 0; i < 36; ++i) {
        //c[i] -= 0x20;
        c[i] >>= 4;
        printf("%c", c[i]);
    }


    return 0;
}
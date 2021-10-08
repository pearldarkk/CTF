#include <malloc.h>
#include <stdio.h>
#include <string.h>
// #include <windows.h>

char f[200];

char fib(char c) {
    return f[(int)c];
}

int main() {
    char str[11] = "NinjnlZyWN";
    str[10] = 0x89;
    char buf[11];
    unsigned char bytes[] = {0, 188, 126, 104, 33, 243, 204, 64, 178, 16, 160, 49, 135, 72, 78, 22, 165, 252, 70, 236, 5, 160, 54, 218, 95, 72, 17, 248, 237, 74, 181, 79, 244, 115, 195, 30, 27, 87, 176, 184, 31, 247, 84, 242, 122, 206, 27, 80};

    f[0] = 1;
    f[1] = 1;
    for (int i = 2; i < 200; ++i)
        f[i] = f[i - 1] + f[i - 2];

    char flag[] = "BKSEC{";

    //223 175 196 143 35 125
    for (int j = 0; j < 5; ++j)
        for (int i = 0x30; i <= 0x7a; ++i)
            if (fib(i) == (char)(flag[j] ^ bytes[j])) {
                buf[j] = i;
                break;
            }

    int j = 0LL;
    for (int i = 1;
         *(char *)((i + 1) % 11 + buf) = (char)str[j] - str[j + buf - str] + *(char *)(i % 11 + buf); ++i)
        if (++j >= 11)
            break;
    //Dissneeland
    j = 11;
    for (int i = 0; i < 48; ++i) {
        *(char *)(bytes + i) ^= fib(*(char *)(buf + i % j));
    }
    for (int i = 0; i < 48; ++i)
        printf("%c", (char) bytes[i]);
    return 0;
}
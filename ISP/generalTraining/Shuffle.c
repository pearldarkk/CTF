#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    time_t t;
    char tmp;
    int tmp1, tmp2;
    char s[41]; //char s[] = "pl4y1ng5huffl3_5ur3ly_n33d5_l075_0f_luck";
    s[0] = 112;
    s[7] = 53;
    s[14] = 95;
    s[21] = 95;
    s[28] = 108;
    s[35] = 95;
    s[1] = 108;
    s[8] = 104;
    s[15] = 53;
    s[22] = 110;
    s[29] = 48;
    s[36] = 108;
    s[2] = 52;
    s[9] = 117;
    s[16] = 117;
    s[23] = 51;
    s[30] = 55;
    s[37] = 117;
    s[3] = 121;
    s[10] = 102;
    s[17] = 114;
    s[24] = 51;
    s[31] = 53;
    s[38] = 99;
    s[4] = 49;
    s[11] = 102;
    s[18] = 51;
    s[25] = 100;
    s[32] = 95;
    s[39] = 107;
    s[5] = 110;
    s[12] = 108;
    s[19] = 108;
    s[26] = 53;
    s[33] = 48;
    s[40] = 0;
    s[6] = 103;
    s[13] = 51;
    s[20] = 121;
    s[27] = 95;
    s[34] = 102;

    srand(t);
    for (int i = 0; i < 100; ++i) {
        tmp1 = rand() % 41;
        tmp2 = rand() % 41;
        tmp = s[tmp1];
        s[tmp1] = s[tmp2];
        s[tmp2] = tmp;
    }
    puts(s);
    return 0;
}
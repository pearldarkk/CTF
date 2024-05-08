#include <stdio.h>
#include <string.h>
char enflag[] = {0x4b, 0x55, 0x26, 0x42, 0x15, 0x7d, 0x5c, 0x16, 0x7e, 0x5d, 0x54, 0x2e};
unsigned int key = 12;
const unsigned int truesize = 30u;

void encode(const char *buf, char* cipher) {
    char tmp1[30], tmp2[30], tmp3[30];
    for (int i = 0; i < key; i += 3) {
        tmp3[i] = buf[i] - 26 ^ key;
        tmp1[i] =  (buf[i + 1] - 26) ^ key;
        tmp2[i +1] =  buf[i + 2] ^ 26 ^ key;
        cipher[i+1] = tmp1[i];
        cipher[i+2] = tmp2[i + 1];
        cipher[i] = tmp3[i];
    }
}

int main() {
    char buf[truesize];
    char cipher[truesize];
    memset(cipher, 0, 30uLL);
    printf("Key: ");
    scanf("%s", buf);
    if (strlen(buf) != key) 
        return 0;
    encode(buf, cipher);

    if (strncmp(cipher, enflag, key))
        puts("flag{d4y14_f149_ph483}");
    else
        puts("Right!");
    return 0;
}


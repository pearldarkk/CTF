#include <stdio.h>
#include <string.h>

int checkPassword(char *buf) {
    int len = strlen(buf);
    if ((len ^ 0xF))
        return 0;

    if (strncmp(buf, "CTF{", 4))
        return 0;

    if (buf[14] != '}')
        return 0;

    const char *content = buf + 4; //noi dung flag
    if (content[0] != '0')
        return 0;

    if (((int)content[1] + 162))
        return 0;

    if (((int)content[2] + (int)content[3] ^ 0xDB)) //flag2 + flag3 ^ 0xDB = 0
        return 0;                                   //flag2 + flag2^0xF^0xDB = 0 -> flag2 + flag2 ^ 212 = 0

    if (((int)content[3] - (int)content[2] ^ 0xF)) //flag3 - flag2^0xF = 0 -> flag3 = flag2^0xF
        return 0;

    if (content[4] - content[3] != (char)(-18))
        return 0;

    if (((content[5] ^ '0') ^ 0x4))
        return 0;

    char buf3 = (char)content[6] * (char)content[5];
    if ((char)(content[6] * content[5]) != -112)
        return 0;

    if ((10 * (int)content[7] - 12 * (int)content[8] + 19 * (int)content[9] ^ 0x7D4))
        return 0;

    if ((28 * (int)content[7] - (int)content[8] + 69 * (int)content[9] ^ 0x22D2))
        return 0;

    if ((113 * (int)content[7] - 126 * (int)content[8] + 999 * (int)content[9] ^ 0x1AB43))
        return 0;

    return 1;
}

int main() {
    char password[128];
    printf("[+] Hay~ nhap password: ");
    fgets(password, 15, stdin);
    if (0 != checkPassword(password))
        printf("[+] Password dung, flag la %s\n", password);
    else
        printf("[+] Ban da nhap sai password\n");
    return 0;
}

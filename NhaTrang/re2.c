#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <key>\n", argv[0]);
        return 1;
    }
    char *key = argv[1];
    // key = "r3v3rs1ng_1s_3asy_4s_l0ng_4s_y0u_h4v3_t00ls"

    // char str[] = "r3v3rs1ng_1s_3asy_4s_l0ng_4s_y0u_h4";
    if (strncmp(key, "r3v3rs1ng_1s", 12) != 0) {
        goto fail;
    }
    if (strncmp(key + 35, "v3_t00ls", 8) != 0) {
        goto fail;
    }

    if (key[12] != '_' || key[25] != '_') {
        goto fail;
    }

    if (strncmp(key + 17, "_4s_l0ng", 8) != 0) {
        goto fail;
    }

    if (strncmp(key + 26, "4s_y0u_h4", 9) != 0) {
        goto fail;
    }

    if (strncmp(key + 13, "3asy", 4) != 0) {
        goto fail;
    }

    printf("Correct key!\nYour flag is: NhaTrang{%s}!\n", key);
    return 0;

fail:
    printf("Wrong key!\n");
    return 1;
}
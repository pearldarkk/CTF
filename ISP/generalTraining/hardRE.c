#include <stdio.h>
#include <string.h>
int main() {
    printf("What is the password?\n");
    char s[13];
    fgets(s, 13, stdin);
    if (!strcmp(s, "the password"))
        puts("true true true, flag is ispclub{fajskfjlksajfiw}");
    else    
        puts("wrong!");
    return 0;
    
}
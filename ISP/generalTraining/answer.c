#include <stdio.h>

void isthisflag(int n) {
    if (n ^ 0x26)
        puts("No, you got it the wrong way!");
    else
        puts("Yes yes yes, submit this:\nLuckinessdoesnthelpusmuchsometimes");
}

int main() {
    int n;
    printf("Give me the number? ");
    scanf("%d", &n);
    isthisflag(n);
}
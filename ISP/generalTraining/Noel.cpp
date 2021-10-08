#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>
int main() {
    int n;
    do {
        scanf("%d", &n);
    } while (n % 2 == 0);
    printf("\nMerry Christmas!");
    Sleep(500);
    system("CLS");


    int cnt = 0;
    while (1) { //bling bling khoảng 20p
        system("CLS");
        for (int i = 1; i <= 2 * n; i++) {
            if (i % 2 == 1) {
                for (int j = n - (i / 2 + 1); j > 0; j--)
                    printf("  ");
                for (int j = 1; j <= i; j++)
                    if (j - cnt & 1)
                        printf("* ");
                    else
                        printf("  ");
                printf("\n");
            } else {
                for (int j = 1; j <= 2 * n - 1; j++) {
                    int gi = abs(n - i / 2);
                    int gj = abs(n - j);
                    int x = n - gi - gj;
                    if (x < 1)
                        printf("  ");
                    else
                        printf("%d ", x);
                }
                printf("\n");
            }
        }
        for (int i = 1; i <= n / 2 + 1; i++) {
            for (int j = 1; j <= n; j++) {
                if (j == n)
                    printf("* ");
                else
                    printf("  ");
            }
            printf("\n");
        }
        Sleep(100);
        ++cnt;
        if (cnt == 200)
            break;
    }
}

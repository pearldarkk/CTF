#include <iostream>
using namespace std;

int main() {
    // reverse
    int r[] = { 38, 3, 46, 5, 59, 62, 76, 90, 41, 28, 0, 83, 13, 117 };
    char s[] = "n0biTax4m";
    for (int i = 0; i < 14; ++i) {
        char t = r[i] ^ s[i % 9];
        printf("%d ", t);
    }

    //source code
    int a[] = { 72, 51, 76, 108, 111, 95, 52, 110, 68, 114, 48, 49, 100, 33 };
    char s[] = "n0biTax4m";
    char t;
    for (int j = 0; j < 14; ++j) {
        for (int i = 0; i < 8; i++) {
            if (((a[j] >> i) & 1) == ((s[j % 9] >> i) & 1))
                t = ((1 << i) ^ -1) & a[j] & 255;
            else
                t = ((1 << i) & 255) | a[j];
            a[j] = t;
        }
        printf("%d ", t);
    }

}
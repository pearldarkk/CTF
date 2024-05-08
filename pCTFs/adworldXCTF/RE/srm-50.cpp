#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main() {
    char v11[4];
    v11[4] = 0;
    char v[13];
    v[12] = 0;
    v11[0] = 'C';
    v[23 - 12] = 'X';
    v11[1] = 'Z';
    v[22 - 12] = 155 - v11[1];
    v11[2] = '9';
    v[21 - 12] = 155 - v11[2];
    v11[3] = 'd';
    v[20 - 12] = '7';
    v[12 - 12] = 'm';
    v[19 - 12] = 'G';
    v[13 - 12] = 'q';
    v[18 - 12] = 170 - v[13 - 12];
    v[14 - 12] = '4';
    v[17 - 12] = 'g';
    v[15 - 12] = 'c';
    v[16 - 12] = '8';
    printf("%s", v11);

}

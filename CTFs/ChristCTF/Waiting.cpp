#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define EL printf("\n")
#define pY printf("YES\n")
#define pN printf("NO\n")
#define Fill(a, x) memset(a, x, sizeof a)
#define fill(a, x) fill(a.begin(), a.end(), x)
#define Sort(v) sort(v.begin(), v.end())
#define sortd(v) sort(v.begin(), v.end(), greater<int>())
#define pb push_back
#define mt make_tuple
#define fi first
#define se second
#define MOD 1000000007LL
#define INF 1e9
#define LINF 1e18
#define ld long double
#define ll long long
#define ull unsigned long long
typedef pair<int, int> ii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;

int main() {
    freopen("text.inp", "r", stdin);
    //freopen("text.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int keyCode[] = {0x97, 0x0D1, 0x0DF, 0x0CE, 0x93, 0x0DC, 0x0A4, 0x0C7, 0x66, 0x0EB, 0xB8, 0x0D4, 0x0A4, 0x0D9, 0x95, 0x8E, 0x0DE, 0x0C8, 0x0E8, 0x98, 0x0CE, 0x0E3, 0x0A7, 0x97, 0x0CC, 0x0DE, 0x94, 0x0CF, 0x0DB, 0x0EB};
    char Messenge[] = "Time has passed without meaning, I want today to be the first day of 2021.\0";
    for (int i = 0; i < 30; ++i)
        printf("%c", keyCode[i] - Messenge[i]);
     return 0;
}
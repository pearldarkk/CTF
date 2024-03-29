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

    int key[27];
    key[0] = 7;
    key[1] = 7;
    key[2] = 82;
    key[3] = 16;
    key[4] = 28;
    key[5] = 1;
    key[6] = 99;
    key[7] = 60;
    key[8] = 39;
    key[9] = 13;
    key[10] = 40;
    key[11] = 19;
    key[12] = 1;
    key[13] = 29;
    key[14] = 20;
    key[15] = 58;
    key[16] = 44;
    key[17] = 6;
    key[18] = 23;
    key[19] = 17;
    key[20] = 21;
    key[21] = 27;
    key[22] = 31;
    key[23] = 65;
    key[24] = 7;
    key[25] = 73;
    key[26] = 20;

    char Messenger[] = "Do you have someone for this Christmas?\0";
    for (int i = 0; i < 27; ++i)
        printf("%c", key[i] ^ Messenger[i]);
     return 0;
}
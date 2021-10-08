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

    char temp[] = "X1t`E1toc`Em3H^\"xxxSPFeaHA^I\0";
    char v1;
    int i, j;

    for (i = 0; i <= 15; ++i) {
        if (i & 1)
            v1 = temp[i] - 1;
        else
            v1 = temp[i] + 1;
        temp[i] = v1;
    }
    temp[16] = '_';
    temp[18] = 'x';
    temp[17] = '0';

    for (j = 19; j < strlen(temp); ++j) {
        if (temp[j] > 'I' || temp[j] <= '?')
            temp[j] += 17;
        else
            temp[j] -= 16;
    }
    cout << temp << endl;
    return 0;
}
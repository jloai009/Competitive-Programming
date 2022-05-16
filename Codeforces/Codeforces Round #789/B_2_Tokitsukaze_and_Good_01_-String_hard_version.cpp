// Codeforces 1678B1  Tokitsukaze and Good 01-String (hard version)
// https://codeforces.com/contest/1678/problem/B2

#include "bits/stdc++.h"
using namespace std;

void solve() {
    int n; cin >> n;
    string s; cin >> s;
    int minOps = 0;
    int minSegs = 0;
    int last = -1;
    for (int i = 0; i < n; i += 2) {
        if (s[i] != s[i+1]) {
            minOps++;
        } else {
            if (s[i]!=last) {
                minSegs++;
            }
            last = s[i];
        }
    }
    cout << minOps << " " << max(1, minSegs) << endl;
}


int main() {
    int t; cin >> t;
    while (t--){
        solve();
    }
}
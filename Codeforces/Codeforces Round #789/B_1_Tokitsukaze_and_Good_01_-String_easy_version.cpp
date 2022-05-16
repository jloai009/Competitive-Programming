// Codeforces 1678B1  Tokitsukaze and Good 01-String (easy version)
// https://codeforces.com/contest/1678/problem/B1

#include "bits/stdc++.h"
using namespace std;


int solve() {
    int n; cin >> n;
    string s; cin >> s;
    int ans = 0;
    for (int i = 0; i < n; i += 2) {
        if (s[i] != s[i+1]) {
            ans++;
        }
    }
    return ans;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cout << solve() << endl;
    }
}
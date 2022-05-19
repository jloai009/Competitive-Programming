// CodeChef CLOSEVOWEL Closest Vowels
// https://www.codechef.com/problems/CLOSEVOWEL

#include "bits/stdc++.h"
using namespace std;
const int MOD = 1000000007;

void solve() {
    int N; cin >> N;
    string S; cin >> S;

    long long ans = 1;
    vector<char> special_chars = {'c', 'g', 'l', 'r'};

    for (char c: S) {
        if (find(special_chars.begin(), special_chars.end(), c) != special_chars.end()) {
            ans = (ans * 2) % MOD;
        }
    }

    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T; cin >> T;
    while(T--) {
        solve();
    }
    

}

//  Codeforces 126B Password
// https://codeforces.com/problemset/problem/126/B

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s; cin >> s;

    int len_s = s.size();

    vector<int> LPS(len_s);
    int k = 0;
    for(int i = 1; i < len_s; ++i) {
        while(k > 0 and s[i] != s[k]) {
            k = LPS[k - 1];
        }
        k += s[i] == s[k];
        LPS[i] = k;
    }

    int len_boundary = LPS[len_s-1];

    if (len_boundary == 0) {
        cout << "Just a legend\n";
        return 0;
    }

    for( int i = 0; i < len_s-1; ++i) {
        if (LPS[i] == len_boundary) {
            cout << s.substr(0, len_boundary) << endl;
            return 0;
        }
    }



    if (LPS[len_boundary-1] == 0) {
        cout << "Just a legend\n";
        return 0;
    }

    cout << s.substr(0, LPS[len_boundary-1]) << endl;
}

//  Kattis - Power Strings
//  https://open.kattis.com/problems/powerstrings

#include "bits/stdc++.h"
using namespace std;

int main() {
    while (true) {
        string s;
        cin >> s;
        if (s ==".") {
            break;
        }
        int n = s.size();
        vector<int> f(n);
        int k = 0;
        for (int i = 1; i < n; i ++) {
            while (s[k] != s[i] and k > 0) {
                k = f[k-1];
            }
            if (s[k]==s[i]) {
                k++;
            }
            f[i] = k;
        }

        if (n%(n-f[n-1])==0) {
            cout << n/(n-f[n-1]) << endl;
        } else {
            cout << 1 << endl;
        }
        
    }
}

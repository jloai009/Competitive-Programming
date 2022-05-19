// Kattis - Casting Spells
// https://open.kattis.com/problems/castingspells

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s; cin >> s;
    if (s.empty()) {
        cout << 0 << endl;
        return 0;
    }

    string t = "$#";
    for(char c: s){
        t.push_back(c);
        t.push_back('#');
    }
    t.push_back('^');

    int c = 1, d =1;
    vector<int> p(t.size());

    for(int i = 2; i< t.size()-1; ++i) {
        int mirror = c - (i-c);
        p[i] = max(0, min(d-i, p[mirror]));
        while(t[i+p[i]+1] == t[i-p[i]-1]) {
            p[i]++;
        }
        if(i+p[i] > d) {
            c = i;
            d = i+p[i];
        }
    }
    
    int ans = 0;

    for(int i = 1; i < p.size()-1; ++i) {
        if (p[i] % 2== 0 and p[i] > ans) {
            int goodRad = (p[i]/4)*2;
            int offset = ans/2 + 2;
            while (offset <= goodRad) {
                if(p[i+offset] >= offset) {
                    ans = max(ans, offset*2);
                }
                offset += 2;
            }
        }
    }

    cout << ans << endl;
}
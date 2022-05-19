// SPOJ - LPS - Longest Palindromic Substring
// https://www.spoj.com/problems/LPS/

#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N; cin >> N;
    string s; cin >> s;

    string t = "$#";
    for (char c: s) {
        t.push_back(c);
        t.push_back('#');
    }
    t.push_back('^');
    vector<int> p(t.size());
    int c = 1, d = 1;

    for(int i = 2; i < t.size()-1; ++i){
        int mirror = c-(i-c);
        p[i] = max(0, min(p[mirror], d-i));
        while (t[i-p[i]-1] == t[i+p[i]+1]) {
            p[i]++;
        }
        if (i+p[i] > d) {
            c = i;
            d = i+p[i];
        }
    }

    int center = 1, radius = p[1];
    for(int i =1; i < t.size()-1; ++i){
        if (p[i] > radius) {
            radius = p[i];
            center = i;
        }
    }

    int start = (center-radius) / 2;
    int end = (center+radius) / 2;

    cout << end-start << endl;
}

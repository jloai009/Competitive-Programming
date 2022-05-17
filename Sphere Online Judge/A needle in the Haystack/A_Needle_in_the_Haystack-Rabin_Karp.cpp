//  SPOJ - NHAY - A Needle in the Haystack
//  https://www.spoj.com/problems/NHAY/

#include <bits/stdc++.h>
using namespace std;
const long long DOM = 128;
const unsigned long long PRIME = 72057594037927931;


vector<int> find_ocurrences_rabin_karp(string &s, string&t, int len_t) {
    unsigned long long hash_s = 0, hash_t = 0;
    int len_s = s.size();
    vector<int> ocurrences;
    if (len_s < len_t) {
        return ocurrences;
    }

    long long last_pos = 1;
    for(int i = 0; i < len_t-1; ++i) {
        last_pos = (last_pos * DOM) % PRIME;
    }

    for(long long i = 0; i < len_t; ++i) {
        hash_t = (hash_t*DOM + int(t[i]) ) % PRIME;
        hash_s = (hash_s*DOM + int(s[i]) ) % PRIME;
    }

    for(long long i = 0; i < len_s-len_t+1; ++i) {
        
        if (hash_s == hash_t) {
            ocurrences.push_back(i);
        }

        hash_s = (hash_s - int(s[i]) * last_pos + PRIME*DOM)  % PRIME;
        hash_s = (hash_s * DOM) % PRIME;
        hash_s = (hash_s + int(s[i+len_t]) ) % PRIME;
    }


    return ocurrences;
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int len_t;
    string t;
    string s;

    while (cin >> len_t) {
        cin >> t;
        cin >> s;
        vector<int> ocurrences = find_ocurrences_rabin_karp(s, t, len_t);
        for (int i : ocurrences) {
            cout << i << '\n';
        }
        cout << "\n";
    }
}
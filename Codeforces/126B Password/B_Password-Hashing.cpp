//  Codeforces 126B Password
// https://codeforces.com/problemset/problem/126/B

#include "bits/stdc++.h"
using namespace std;

const int DOM = 26;
const int PRIME = INT_MAX;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s; cin >> s;
    int n = s.size();

    vector<long long> pows(n), hashes(n+1);

    pows[0] = 1;
    for(int i = 1; i < n; ++i) {
        pows[i] = (pows[i-1] * DOM) % PRIME;
    }

    for ( int i = 0; i < hashes.size()-1; ++i) {
        hashes[i+1] = ( hashes[i] + (s[i]-95)*pows[i] ) % PRIME;
    }

    vector<pair<int, long long>> boundaries;

    for (int i = 1; i < n; ++i) {
        long long suffix_hash = (hashes[n] - hashes[n-i] + PRIME) % PRIME;
        long long prefix_hash = (hashes[i]*pows[n-i] ) % PRIME;
        if (suffix_hash == prefix_hash) {
            boundaries.push_back({i, suffix_hash});
        }
    }

    function<bool(int, long long)> find = [&] (int k, long long target_hash) {
        for(int i = 1; i+k < hashes.size()-1; ++i) {
            long long hash = (hashes[i+k] - hashes[i] +PRIME) % PRIME;
            hash = (hash*pows[n-(i+k)]) % PRIME;
            if (hash == target_hash) {
                return true;
            }
        }
        return false;
    };

    int low = 0;
    int longest_found = 0;
    int high = boundaries.size()-1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        int k = boundaries[mid].first;
        int target_hash = boundaries[mid].second;
        if (find(k , target_hash)) {
            longest_found = k;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }


    if (longest_found == 0) {
        cout << "Just a legend\n";
        return 0;
    }

    cout << s.substr(0, longest_found) << endl;


}

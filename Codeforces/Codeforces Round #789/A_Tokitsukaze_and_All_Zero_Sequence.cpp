// Codeforces 1678A Tokitsukaze and All Zero Sequence
// https://codeforces.com/contest/1678/problem/A

// Tokitsukaze has a sequence a of length n.
// For each operation, she selects two numbers ai and aj (i≠j; 1≤i,j≤n).

//     If ai=aj, change one of them to 0.
//     Otherwise change both of them to min(ai,aj). 

// Tokitsukaze wants to know the minimum number of operations to change all numbers in the sequence to 0.
// It can be proved that the answer always exists.

#include "bits/stdc++.h"
using namespace std;


int solve() {
    int n; cin >> n;
    map<int, int> mp;
    int temp = n;
    while (temp--) {
        int num; cin >> num;
        if (mp.count(num)) {
            mp[num]++;
        } else {
            mp[num] = 1;
        }
    }
    if (mp.count(0)) {
        return n - mp[0];
    }
    for (auto kv : mp) {
        if (kv.second >= 2) {
            return n;
        }
    }
    return n+1;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cout << solve() << endl;
    }
}
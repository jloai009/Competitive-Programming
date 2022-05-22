// CodeChef - INTEST - Enormous Input Test
// https://www.codechef.com/LP0TO101/problems/INTEST

#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    int ans = 0;
    for(int i = 1; i <= n;  ++i){
        int t;
        cin >> t;
        ans += t % k == 0;
    }
    cout << ans << endl;
}

// CodeChef - TWODISH - Two Dishes
// https://www.codechef.com/LP1TO201/problems/TWODISH

#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    while(T--){
        int N, A, B, C;
        cin >> N >> A >> B >> C;

        string ans = A+C >= N && B >= N ? "YES" : "NO";
        cout << ans << "\n";
    }

}

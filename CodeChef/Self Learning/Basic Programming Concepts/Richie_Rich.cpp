// CodeChef - CHFRICH - Richie Rich
// https://www.codechef.com/LP1TO201/problems/CHFRICH

#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    int A, B, X;
    for(int i = 1; i <= T; ++i){
        cin >> A >> B >> X;
        int needed_growth = B - A;
        int ans = needed_growth / X;
        cout << ans << endl;
    }

}

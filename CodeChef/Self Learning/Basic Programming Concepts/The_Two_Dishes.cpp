// CodeChef - MAX_DIFF - The Two Dishes
// https://www.codechef.com/LP1TO201/problems/MAX_DIFF

#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    int N, S;
    while(T--){
        cin >> N >> S;
        int ans = N >= S ? S : N-(S-N);
        cout << ans << endl;
    }

}

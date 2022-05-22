// CodeChef - LUCKFOUR - Lucky Four
// https://www.codechef.com/LP0TO101/problems/LUCKFOUR

#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for(int i = 1; i <= T; ++i){
        string N;
        cin >> N;

        int ans = count(N.begin(), N.end(), '4');
        cout << ans << "\n";
    }


}
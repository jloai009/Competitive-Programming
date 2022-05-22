// CodeChef - VDATES - Vaccine Dates
// https://www.codechef.com/LP1TO201/problems/VDATES

#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    int D, L, R;
    while(T--){
        cin >> D >> L >> R;
        string ans = "Too Late";
        if(D <= R) {
            ans = "Take second dose now";
        }
        if(D < L) {
            ans = "Too Early";
        }
        cout << ans << endl;
    }

}

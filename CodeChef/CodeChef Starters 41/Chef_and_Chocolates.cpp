#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    while(T--){
        int X, Y, Z;
        cin >> X >> Y >> Z;
        int ans = (X*5 + Y*10) / Z;
        cout << ans << '\n';
    }

}

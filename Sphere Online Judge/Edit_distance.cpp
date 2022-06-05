#include <bits/stdc++.h>
using namespace std;

void solve(){
    string A, B;
    cin >> A >> B;
    int n = A.length();
    int m = B.length();

    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));

    for(int i = 0; i < m+1; i++)
        dp[0][i] = i;

    for(int i = 0; i < n+1; i++)
        dp[i][0] = i;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            dp[i+1][j+1] = dp[i+1][j]+1;
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1]+1);
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+(A[i]!=B[j]));
        }
    }

    cout << dp[n][m] << endl;

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    while(T--){
        solve();
    }

}

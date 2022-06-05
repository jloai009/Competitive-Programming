#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string A; cin >> A;
    string B; cin >> B;

    int n = A.length();
    int m = B.length();

    vector<vector<int>> dp(n+1, vector<int>(m+1,0));

    int answer = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if (A[i] == B[j]){
                dp[i+1][j+1] = dp[i][j] + 1;
            }else{
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]);
            }
            answer = max(answer, dp[i+1][j+1]);
        }


    }

    cout << answer << endl;

}
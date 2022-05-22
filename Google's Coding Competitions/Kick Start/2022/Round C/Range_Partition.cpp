// Google Kickstart Round C 2022 - Range Partition
// https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20deb

#include "bits/stdc++.h"
using namespace std;

void solve(){
    int N, X, Y;
    cin >> N >> X >> Y;
    long long total_sum = N*(N+1)/2;
    if(total_sum % (X + Y) != 0){
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    cout << "POSSIBLE" << endl;
    long long target = X * total_sum / (X + Y);
    long long curr_sum = 0;

    vector<int> answer;

    long long sum = 0;
    for(int i = N; i > 0; --i){
        if(curr_sum + i <= target){
            curr_sum += i;
            answer.push_back(i);
        }
        if(curr_sum == target){
            break;
        }
    }
    cout << answer.size() << '\n';
    reverse(answer.begin(), answer.end());
    for(int n : answer){
        cout << n << " ";
    }
    cout << '\n';
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        cout << "Case #" << t << ": ";
        solve();
    }

}

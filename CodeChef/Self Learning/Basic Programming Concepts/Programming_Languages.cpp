#include <bits/stdc++.h>
using namespace std;

void solve(){
    int A, B, A1, B1, A2, B2;

    cin >> A >> B >> A1 >> B1 >> A2 >> B2;
    set<int> one = {A1, B1};
    set<int> two = {A2, B2};

    int answer = 0;
    if(one.count(A) && one.count(B)){
        answer = 1;
    } else if(two.count(A) && two.count(B)){
        answer = 2;
    }
    cout << answer << '\n';
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}
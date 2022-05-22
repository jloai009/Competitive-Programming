#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        string N;
        cin >> N;
        reverse(N.begin(), N.end());
        int j = 0;
        while (N[j] == '0' && j < N.length()){
            ++j;
        }
        cout << N.substr(j, N.length()-j) << endl;
    }
    

}

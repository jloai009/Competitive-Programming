#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    while(T--) {
        string N;
        cin >> N;
        int sum_digits = 0;
        for(char d: N){
            sum_digits += d - '0';
        }
        cout << sum_digits << endl;
    }

}

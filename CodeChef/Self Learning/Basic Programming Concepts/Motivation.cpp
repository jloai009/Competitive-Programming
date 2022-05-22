// CodeChef - IMDB - Motivation
// https://www.codechef.com/LP1TO201/problems/IMDB

#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    while(T--){
        int N, X;
        cin >> N >> X;
        int highest_rating = INT_MIN;
        while(N--){
            int S, R;
            cin >> S >> R;
            if(S <= X){
                highest_rating = max(highest_rating, R);
            }
        }
        cout << highest_rating << endl;
    }

}

//  SPOJ - PERIOD - Period
//  https://www.spoj.com/problems/PERIOD/
//  For each prefix of a given string S with N characters
//  (each character has an ASCII code between 97 and 126, inclusive),
//  we want to know whether the prefix is a periodic string. That is,
//  for each i (2 <= i <= N) we want to know the largest K > 1 (if there is one)
//  such that the prefix of S with length i can be written as AK ,
//  that is A concatenated K times, for some string A.
//  Of course, we also want to know the period K. 

#include "bits/stdc++.h"
using namespace std;

void solve(int i) {
    int N;
    cin >> N;
    string S;
    cin >> S;

    int k = 0;
    vector<int> f(N);
    
    for ( int i = 1; i < N; ++i ) {
        while ( k > 0 and S[i] != S[k] ) {
            k = f[k-1];
        }
        if (S[i] == S[k]) {
            k ++;
        }
        f[i] = k;
    }

    cout << "Test case #" << i << endl;

    for ( int i = 1; i < N; ++i ) {
        int lenSubstr = i+1;
        int lenBoundary = f[i];
        int lenShift = lenSubstr - lenBoundary;
        if (lenBoundary != 0 and lenSubstr % lenShift == 0) {
            cout << lenSubstr << " "<< lenSubstr / lenShift << endl;
        }
    }

    cout << endl;

}

int main() {
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        solve(i);
    }
}

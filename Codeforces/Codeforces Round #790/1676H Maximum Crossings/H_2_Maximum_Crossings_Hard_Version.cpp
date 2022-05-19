// Codeforces 1676H2 Maximum Crossings
// https://codeforces.com/contest/1676/problem/H2

#include "bits/stdc++.h"
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> vec(n);
    
    for(int i = 0; i < n; i++) {
        cin >> vec[i];
    }

    long long inversions = 0;
    
    function<vector<int>(vector<int>&)> mergeSort = [&] (vector<int> &arr) {
        if (arr.size() < 2) {
            return arr;
        }
        int mid = arr.size()/2;
        vector<int> L = vector<int>(arr.begin(), arr.begin()+mid);
        vector<int> R = vector<int>(arr.begin()+mid, arr.end());
        mergeSort(L);
        mergeSort(R);
        int l = 0;
        int r = 0;
        for(int i = 0; i < arr.size(); i++) {
            if (r == R.size() or l < L.size() and L[l] < R[r]) {
                arr[i] = L[l];
                inversions += r;
                l++;
            } else {
                arr[i] = R[r];
                r++;
            }
        }
        return arr;
    };


    mergeSort(vec);


    cout << inversions << endl;
}

int main() {

    int t;
    cin >> t;
    while(t--) {
        solve();
    }

}

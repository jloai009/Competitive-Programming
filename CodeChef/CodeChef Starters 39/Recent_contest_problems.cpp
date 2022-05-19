#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T; cin >> T;
    while(T--) {
        int N; cin >> N;
        map<string, int> count;

        while(N--){
            string s; cin >> s;
            count[s]++;
        }

        cout << count["START38"] << " " << count["LTIME108"] << endl;

    }

}

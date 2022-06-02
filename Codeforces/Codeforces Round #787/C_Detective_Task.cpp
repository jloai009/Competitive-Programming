#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        int answer = 0;
        int first_zero = s.find('0');

        if(first_zero != -1)
            answer += 1;
        else
            first_zero = s.length();
        
        int last_one = s.rfind('1');
        if(last_one != -1)
            answer += 1;
        
        answer += first_zero - last_one - 1;
        cout << answer << '\n';
    }

}

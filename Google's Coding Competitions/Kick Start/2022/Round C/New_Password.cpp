// Google Kickstart Round C 2022 - New Password
// https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20f15

#include "bits/stdc++.h"
using namespace std;

string fix_password(){
        int N;
        cin >> N;
        string old_password;
        cin >> old_password;

        bool has_upper = false, has_lower = false, has_digit = false, has_special = false;
        const set<char> SPECIAL_CHARS = {'#', '@', '*', '&'};

        for(char c : old_password){
            has_lower |= islower(c);
            has_upper |= isupper(c);
            has_digit |= isdigit(c);
            has_special |= SPECIAL_CHARS.count(c);
        }

        string new_tail = "";
        if(!has_upper){
            new_tail += "A";
        }
        if(!has_lower){
            new_tail += "a";
        }
        if(!has_digit){
            new_tail += "1";
        }
        if(!has_special){
            new_tail += "#";
        }
        while(old_password.length() + new_tail.length() < 7){
            new_tail += "#";
        }
        string new_password = old_password + new_tail;
        return new_password;

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i){
        cout << "Case #" << i << ": " << fix_password() << '\n';
        
    }

}

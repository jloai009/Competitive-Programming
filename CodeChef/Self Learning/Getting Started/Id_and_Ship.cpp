// CodeChef - FLOW010 - Id and Ship
// https://www.codechef.com/LP0TO101/problems/FLOW010

#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    char id;
    for(int i = 1; i <= T; ++i){
        cin >> id;
        id = tolower(id);
        string ship_id;
        switch(id) {
            case 'b':
                ship_id = "BattleShip";
                break;
            case 'c':
                ship_id = "Cruiser";
                break;
            case 'd':
                ship_id = "Destroyer";
                break;
            case 'f':
                ship_id = "Frigate";
                break;
        }

        cout << ship_id << endl;
    }

}

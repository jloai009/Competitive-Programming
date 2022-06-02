#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--){
        int a, b, c, x, y;
        cin >> a >> b >> c >> x >> y;
        int needed_dog_food = max(0, x-a);
        int needed_cat_food = max(0, y-b);
        string ans = c >= needed_cat_food + needed_dog_food ? "YES" : "NO";
        cout << ans <<"\n";
    }

}

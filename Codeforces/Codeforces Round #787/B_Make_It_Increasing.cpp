#include "bits/stdc++.h"
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> nums(n);
        for(int &num : nums)
            cin >> num;
        
        int min_ops = 0;
        for(int i = n-2; i >= 0; --i){
            if(nums[i+1] == 0){
                min_ops = -1;
                break;
            }
            while(nums[i] >= nums[i+1]){
                nums[i] /= 2;
                min_ops++;
            }
        }
        cout << min_ops << '\n';
    }

}

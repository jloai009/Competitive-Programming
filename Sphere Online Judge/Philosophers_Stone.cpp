#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    
    while(T--){
        int h, w;
        cin >> h >> w;
        
        vector<vector<int>> A(h);
        
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                int num;
                cin >> num;
                A[i].push_back(num);
            }
        }


        for(int i = 1; i < h; i++){
            for(int j = 0; j < w; j++){
                int prev = A[i-1][j];
                if (j > 0){
                    prev = max(prev, A[i-1][j-1]);
                }
                if (j < w-1){
                    prev = max(prev, A[i-1][j+1]);
                }
                A[i][j] += prev;
            }
        }


        int answer = 0;
        for(int n : A[h-1]){
            answer = max(answer, n);
        }

        cout << answer << endl;

    }

}
